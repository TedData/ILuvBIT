#!/usr/bin/env python3
# ###################################################
# A Model View Controller (MVC) application for a simple adventure game
#
# The Model class requires the following interface:
# Constructor : Model()
# Methods:
#  get_player() - get the player object
#  get_monsters() - get the list of monsters
#  get_items() - get the items
#  player_take_item() - find an item that is sufficiently close to the player
#      and if one found the player takes that item, otherwise do nothing
#
# The Character class requires the following interface:
# Constructor :  Character(x, y, name)
# Methods:
#  move(deltax, deltay) - offset the (x,y) position by (deltax, deltay)
#  get_health() - get the health
#  update_health(delta) - add delta to health
#  get_armour() - get the armour strength
#  update_armour(delta) - add delta to armour
#
# The Player class (inherit from Character) requires the following interface:
# Constructor : Player(x, y, name)
# Methods:
#  get_inventory() - get the players inventory
#  take(item) - add item to inventory
#  drop(index) - drop the item at given index (in inventory) - do nothing if 
#          index out of range
#  hold(index) - hold the item at given index (in inventory) - do nothing if 
#          index out of range
#  get_holding() - get the item being held (None if nothing held)
#  use() - use the item being held (do nothing if nothing held)
#
# The Monster class (inherit from Character) requires the following interface:
# Constructor : Monster(x, y, name, model)
# Methods:
#  attack() - if the player is sufficiently close then attack
#  step() - What the monster does in the next time step
#
# The Item class requires the following interface:
# Constructor : Item(x, y, name)
# Methods:
#  set_position(x, y) - put the item at location (x,y)
#  is_taken() - return True iff player has the item
#  set_taken(t) - set the taken flag to the boolean t
#
####################################################
#
# WARNING: This code uses some more advanced features which we will see
# later in the course. We will work on GUIs shortly. 
# There is also a use of list comprehension taht we will see in the last 
# section of the course.
#
#####################################################


# imports for the GUI
import tkinter as tk
from tkinter import messagebox

# import the model from model2.py
from model2 import *

# the dimensions of the canvas
WIDTH = 550#750
HEIGHT = 550#750

# the distance (in pixels) travelled by the player when an arrow key is pressed
DELTA = 15

# The timer time step for annimation in millisecs
TIME_STEP = 400

# The size of the rectangle in which the monsters health level is displayed
HEALTH_BOX_LENGTH = 20
HEALTH_BOX_WIDTH = 5

# The offset of the above rectangle from the centre of the monster
X_HEALTH_BOX_OFFSET = 0
Y_HEALTH_BOX_OFFSET = 20

# Typically to make your own widgets you inherit from a frame (a container)
# and add widgets to that frame
class Status(tk.Frame):
    """The status bar widget for the player"""

    def __init__(self, master, parent, player):
        super().__init__(master)

        self.parent = parent
        self.player = player

        # A label to list the inventory (as text)
        tk.Label(self, text="Inventory: ").pack(side=tk.LEFT)
        self.inventory = tk.Label(self, text="")
        self.inventory.pack(side=tk.LEFT, fill=tk.X)

        # Note: the following are packed from the right and so are in
        # "reverse order"

        # a lable to show the armour strength 
        self.armour = tk.Label(self, text="      ")
        self.armour.pack(side=tk.RIGHT)
        tk.Label(self, text="  Armour: ").pack(side=tk.RIGHT)

        # a label to show the health
        self.health = tk.Label(self, text="      ")
        self.health.pack(side=tk.RIGHT)
        tk.Label(self, text="Health: ").pack(side=tk.RIGHT)

    def update_inventory(self):
        """Update the inventory label with the current inventory

        update_inventory() -> None
        """
        # the text includes the index so the user can choose an item
        # the item being held is prefixed by a '*'
        text = ' '.join("{0}:{1}{2}". \
                            format(i,
                                   ("*" if self.player.get_holding() == item \
                                        else ""),
                                   str(item)) \
                        for i, item in enumerate(self.player.get_inventory()))

        # update the inventory label with the new inventory text
        self.inventory.configure(text=text)

    def update_health(self, health):
        """Update the health lable with the current health

        update_health(int) -> None
        """
        self.health.configure(text="{0:>6}".format(health))

    def update_armour(self, armour):
        """Update the armour lable with the current armour

        update_health(int) -> None
        """
        self.armour.configure(text="{0:>6}".format(armour))


class GameApp(object):
    """The application"""

    def __init__(self, master):
        master.title("Game2")
        self._master = master

        # Create the model
        self.model = Model()

        # extract the player object from the model
        self.player = self.model.get_player()

        # Create the canvas where game objects will be drawn
        self._canvas = tk.Canvas(master, bg='grey100',
                                 width=WIDTH, height=HEIGHT)
        self._canvas.pack(expand=1, fill=tk.BOTH)

        # Bind a key press event to teh key_press method - i.e. call
        # key_press each time a key is pressed
        self._canvas.bind_all("<Key>", self.key_press)

        # create the player status bar
        self.status_bar = Status(master, self, self.player)
        self.status_bar.pack(expand=1, fill=tk.X, padx=20, pady=10)

        # the following 2 flags are used for keyboard interaction
        self.doing_drop = False
        self.doing_hold = False

        # for efficiency the GIFs are preloaded into a dictionary
        self.load_images()

        player_image_name = self.player.get_name()

        # the player image doesn't change so preload for efficiency
        self.player_image = self.images[player_image_name]

        # display all game objects and update the player status info
        self.show()

        # set the timer going (for annimation) - self.update
        # is called when the timer expires
        self._master.after(TIME_STEP, self.update)

    def load_images(self):
        """Load images files into memory.

        load_images() -> None
        """
        self.images = {
            "player": tk.PhotoImage(file='data/player.gif'),
            "balloon": tk.PhotoImage(file='data/balloon.gif'),
            "purple": tk.PhotoImage(file='data/purple.gif'),
            "triangle": tk.PhotoImage(file='data/triangle.gif'),
            "sword": tk.PhotoImage(file='data/sword.gif'),
            "dagger": tk.PhotoImage(file='data/dagger.gif'),
            "potion": tk.PhotoImage(file='data/potion.gif'),
        }

    def update(self):
        """Do a time step in the game.

        update() -> None
        """
        # Each moster does a step
        for monster in self.model.get_monsters():
            monster.step()

        # (re)display everything
        self.show()

        # check to see if the player should die
        if self.player.get_health() == 0:
            messagebox.showinfo("Game End", "   You Die!   ")
            self._master.destroy()
            return

        # if not (re)start the timer 
        self._master.after(TIME_STEP, self.update)

    def draw_health_box(self, x, y, health):
        """Draw a health box for a monster at position (x,y) with the
        given health.

        draw_health_box(int, int, int) -> None
        """
        x += X_HEALTH_BOX_OFFSET
        y += Y_HEALTH_BOX_OFFSET
        self._canvas.create_rectangle(x, y,
                                      x + HEALTH_BOX_LENGTH, y + HEALTH_BOX_WIDTH,
                                      fill="white",
                                      outline="black")
        length = health * HEALTH_BOX_LENGTH // 100
        self._canvas.create_rectangle(x, y,
                                      x + length, y + HEALTH_BOX_WIDTH,
                                      fill="red",
                                      outline="black")

    def show(self):
        """Show all the game objects and update the player status bar

        show() -> None
        """
        # The simplest approach to displaying the current state of the game
        # on the canvas is to delete everything and redraw everything
        self._canvas.delete(tk.ALL)

        items = self.model.get_items()
        # draw all the items (not in player inventory)
        for item in items:
            if item.is_taken():
                # don't draw the item if the player has the item
                continue
            x, y = item.get_position()
            name = item.get_name()
            image = self.images[name]
            self._canvas.create_image(x, y, image=image)

        # draw all the monsters
        for monster in self.model.get_monsters():
            x, y = monster.get_position()
            image_name = monster.get_name()
            monster_image = self.images[image_name]
            self._canvas.create_image(x, y, image=monster_image)
            self.draw_health_box(x, y, monster.get_health())

        # draw the player
        x, y = self.player.get_position()
        self._canvas.create_image(x, y, image=self.player_image)
        item_held = self.player.get_holding()

        # if the player is holding an item draw that
        if item_held is not None:
            name = item_held.get_name()
            image = self.images[name]
            self._canvas.create_image(x + 10, y - 10, image=image)

        # update the play status info
        self.status_bar.update_inventory()
        self.status_bar.update_health(self.player.get_health())
        self.status_bar.update_armour(self.player.get_armour())

    def key_press(self, e):
        """Modify game based on key pressed

        key_press(KeyObject) -> None

        Arrow keys: move player in that direction by a given amount
        Spacebar : use held item (once per press)
        't' : take the item near player
        'd' followed by number key (index) : drop that item
        'h' followed by number key (index) : hold that item
        """
        key = e.keysym

        if self.doing_drop:
            # 'd' was previous key pressed
            self.doing_drop = False
            if key in "0123456789":
                self.player.drop(int(key))
                self.show()
                return
        if self.doing_hold:
            # 'h' was previous key pressed
            self.doing_hold = False
            if key in "0123456789":
                self.player.hold(int(key))
                self.show()
                return

        self.doing_drop = False
        self.doing_hold = False

        if key == 'Up':
            self.player.move(0, -DELTA)
        elif key == 'Down':
            self.player.move(0, DELTA)
        elif key == 'Left':
            self.player.move(-DELTA, 0)
        elif key == 'Right':
            self.player.move(DELTA, 0)
        elif key == 't':
            self.model.player_take_item()
        elif key == 'd':
            self.doing_drop = True
        elif key == 'h':
            self.doing_hold = True
        elif key == 'space':
            self.player.use()

        self.show()


def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
