import tkinter as tk 
from tkinter import messagebox
from model1 import *

WIDTH = 550 #750
HEIGHT = 550 #750

DELTA = 10

class Status(tk.Frame):
    def __init__(self, master, parent, char):
        super().__init__(master)
        self.parent = parent
        self.char = char

        tk.Label(self, text= "Inventory: ").pack(side=tk.LEFT)
        self.inventory = tk.Label(self, text= "")
        self.inventory.pack(side=tk.LEFT,fill=tk.X)

    def update_inventory(self):
        text = ' '.join("{0}:{1}{2}".\
                        format(i,
                               ("*" if self.char.get_holding() == item else ""),
                               str(item)) \
                        for i,item in enumerate(self.char.get_inventory()))

        self.inventory.configure(text=text)


class GameApp(object):
    def __init__(self, master):   
        master.title("Game1")
        self._master = master
        self.model = Model()
        self.char = self.model.get_character()
        self._canvas = tk.Canvas(master, bg='grey100', 
                                 width=WIDTH, height=HEIGHT)
        self._canvas.pack(expand=1, fill=tk.BOTH)
        self._canvas.bind_all("<Key>", self.key_press)
        self.status_bar = Status(master, self, self.char)
        self.status_bar.pack(expand=1, fill=tk.X, padx=20, pady = 10)
        self.doing_drop = False
        self.doing_hold = False
        self.images = { 
            "player":tk.PhotoImage(file = 'data/player.gif'),
            "sword":tk.PhotoImage(file = 'data/sword.gif'),
            "dagger":tk.PhotoImage(file = 'data/dagger.gif'),
            "potion":tk.PhotoImage(file = 'data/potion.gif'),
        }
        char_image_name = self.char.get_name()
        self.char_image = self.images[char_image_name]
        self.show()


    def show(self):
        self._canvas.delete(tk.ALL)

        items = self.model.get_items()

        for item in items:
            if item.is_taken():
                continue
            x, y = item.get_position()
            name = item.get_name()
            image = self.images[name]
            self._canvas.create_image(x, y, image = image)

        x, y = self.char.get_position()
        self._canvas.create_image(x, y, image = self.char_image)
        item_held = self.char.get_holding()
        # if the character is holding an item draw that
        if item_held is not None:
            name = item_held.get_name()
            image = self.images[name]
            self._canvas.create_image(x+10, y-10, image = image)
        self.status_bar.update_inventory()


    def key_press(self, e):
        """Modify game based on key pressed

        key_press(KeyObject) -> None

        Arrow keys: move character in that direction by a given amount
        't' : take the item near character
        'd' followed by number key (index) : drop that item
        'h' followed by number key (index) : hold that item
        """
        key = e.keysym
        
        if self.doing_drop:
            # 'd' was previous key pressed
            self.doing_drop = False
            if key in "0123456789":
                self.char.drop(int(key))
                self.show()
                return
        if self.doing_hold:
            # 'h' was previous key pressed
            self.doing_hold = False
            if key in "0123456789":
                self.char.hold(int(key))
                self.show()
                return

        self.doing_drop = False
        self.doing_hold = False

        if key == 'Up':
            self.char.move(0,-DELTA)
        elif key == 'Down':
            self.char.move(0,DELTA)
        elif key == 'Left':
            self.char.move(-DELTA,0)
        elif key == 'Right':
            self.char.move(DELTA,0)
        elif key == 't':
            self.model.character_take_item()
        elif key == 'd':
            self.doing_drop = True
        elif key == 'h':
            self.doing_hold = True
        
        self.show()

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
