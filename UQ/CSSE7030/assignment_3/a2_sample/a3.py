"""
CSSE7030 Assignment 3
Semester 2, 2020
"""

# Fill these in with your details
__author__ = "{{Peng Yu}} ({{46635884}})"
__email__ = "peng.yu1@uqconnect.edu.au"
__date__ = "29.10.2020"


try:
    from a2_solution import *
except:          
    GAME_LEVELS = {
        # dungeon layout: max moves allowed
        "game1.txt": 7,
        "game2.txt": 12,
        "game3.txt": 19,
    }

    PLAYER = "O"
    KEY = "K"
    DOOR = "D"
    WALL = "#"
    MOVE_INCREASE = "M"
    SPACE = " "

    DIRECTIONS = {
        "W": (-1, 0),
        "S": (1, 0),
        "D": (0, 1),
        "A": (0, -1)
    }

    INVESTIGATE = "I"
    QUIT = "Q"
    HELP = "H"

    VALID_ACTIONS = [INVESTIGATE, QUIT, HELP, *DIRECTIONS.keys()]

    HELP_MESSAGE = f"Here is a list of valid actions: {VALID_ACTIONS}"

    INVALID = "That's invalid."

    WIN_TEXT = "You have won the game with your strength and honour!"

    LOSE_TEST = "You have lost all your strength and honour."
    LOSE_TEXT = "You have lost all your strength and honour."


    class Display:
        """Display of the dungeon."""

        def __init__(self, game_information, dungeon_size):
            """Construct a view of the dungeon.

            Parameters:
                game_information (dict<tuple<int, int>: Entity): Dictionary 
                    containing the position and the corresponding Entity
                dungeon_size (int): the width of the dungeon.
            """
            self._game_information = game_information
            self._dungeon_size = dungeon_size

        def display_game(self, player_pos):
            """Displays the dungeon.
            
            Parameters:
                player_pos (tuple<int, int>): The position of the Player
            """
            dungeon = ""

            for i in range(self._dungeon_size):
                rows = ""
                for j in range(self._dungeon_size):
                    position = (i, j)
                    entity = self._game_information.get(position)

                    if entity is not None:
                        char = entity.get_id()
                    elif position == player_pos:
                        char = PLAYER
                    else:
                        char = SPACE
                    rows += char
                if i < self._dungeon_size - 1:
                    rows += "\n"
                dungeon += rows
            print(dungeon)

        def display_moves(self, moves):
            """Displays the number of moves the Player has left.
            
            Parameters:
                moves (int): THe number of moves the Player can preform. 
            """
            print(f"Moves left: {moves}\n")


    def load_game(filename):
        """Create a 2D array of string representing the dungeon to display.
        
        Parameters:
            filename (str): A string representing the name of the level.

        Returns:
            (list<list<str>>): A 2D array of strings representing the 
                dungeon.
        """
        dungeon_layout = []

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                dungeon_layout.append(list(line))

        return dungeon_layout

    class Entity:
        """ """

        _id = "Entity"

        def __init__(self):
            """
            Something the player can interact with
            """
            self._collidable = True

        def get_id(self):
            """ """
            return self._id

        def set_collide(self, collidable):
            """ """
            self._collidable = collidable

        def can_collide(self):
            """ """
            return self._collidable

        def __str__(self):
            return f"{self.__class__.__name__}({self._id!r})"

        def __repr__(self):
            return str(self)


    class Wall(Entity):
        """ """

        _id = WALL
        
        def __init__(self):
            """ """
            super().__init__()
            self.set_collide(False)


    class Item(Entity):
        """ """
        def on_hit(self, game):
            """ """
            raise NotImplementedError


    class Key(Item):
        """ """

        _id = KEY

        def on_hit(self, game):
            """ """
            player = game.get_player()
            player.add_item(self)
            game.get_game_information().pop(player.get_position())


    class MoveIncrease(Item):
        """ """

        _id = MOVE_INCREASE

        def __init__(self, moves=5):
            """ """
            super().__init__()
            self._moves = moves

        def on_hit(self, game):
            """ """
            player = game.get_player()
            player.change_move_count(self._moves)
            game.get_game_information().pop(player.get_position())


    class Door(Entity):
        """ """
        _id = DOOR

        def on_hit(self, game):
            """ """
            player = game.get_player()
            for item in player.get_inventory():
                if item.get_id() == KEY:
                    game.set_win(True)
                    return

            print("You don't have the key!")


    class Player(Entity):
        """ """

        _id = PLAYER

        def __init__(self, move_count):
            """ """
            super().__init__()
            self._move_count = move_count
            self._inventory = []
            self._position = None

        def set_position(self, position):
            """ """
            self._position = position

        def get_position(self):
            """ """
            return self._position

        def change_move_count(self, number):
            """
            Parameters:
                number (int): number to be added to move count
            """
            self._move_count += number

        def moves_remaining(self):
            """ """
            return self._move_count

        def add_item(self, item):
            """Adds item (Item) to inventory
            """
            self._inventory.append(item)

        def get_inventory(self):
            """ """
            return self._inventory


    class GameLogic:
        """ """
        def __init__(self, dungeon_name="game2.txt"):
            """ """
            self._dungeon = load_game(dungeon_name)
            self._dungeon_size = len(self._dungeon)
            self._player = Player(GAME_LEVELS[dungeon_name])
            self._game_information = self.init_game_information()
            self._win = False

        def get_positions(self, entity):
            """ """
            positions = []
            for row, line in enumerate(self._dungeon):
                for col, char in enumerate(line):
                    if char == entity:
                        positions.append((row, col))

            return positions

        def init_game_information(self):
            """ """
            player_pos = self.get_positions(PLAYER)[0]
            key_position = self.get_positions(KEY)[0]
            door_position = self.get_positions(DOOR)[0]
            wall_positions = self.get_positions(WALL)
            move_increase_positions = self.get_positions(MOVE_INCREASE)
            
            self._player.set_position(player_pos)

            information = {
                key_position: Key(),
                door_position: Door(),
            }

            for wall in wall_positions:
                information[wall] = Wall()

            for move_increase in move_increase_positions:
                information[move_increase] = MoveIncrease()

            return information

        def get_player(self):
            """ """
            return self._player

        def get_entity(self, position):
            """ """
            return self._game_information.get(position)

        def get_entity_in_direction(self, direction):
            """ """
            new_position = self.new_position(direction)
            return self.get_entity(new_position)

        def get_game_information(self):
            """ """
            return self._game_information

        def get_dungeon_size(self):
            """ """
            return self._dungeon_size

        def move_player(self, direction):
            """ """
            new_pos = self.new_position(direction)
            self.get_player().set_position(new_pos)

        def collision_check(self, direction):
            """
            Check to see if a player can travel in a given direction
            Parameters:
                direction (str): a direction for the player to travel in.

            Returns:
                (bool): False if the player can travel in that direction without colliding otherwise True.
            """
            new_pos = self.new_position(direction)
            entity = self.get_entity(new_pos)
            if entity is not None and not entity.can_collide():
                return True
            
            return not (0 <= new_pos[0] < self._dungeon_size and 0 <= new_pos[1] < self._dungeon_size)

        def new_position(self, direction):
            """ """
            x, y = self.get_player().get_position()
            dx, dy = DIRECTIONS[direction]
            return x + dx, y + dy

        def check_game_over(self):
            """ """
            return self.get_player().moves_remaining() <= 0

        def set_win(self, win):
            """ """
            self._win = win

        def won(self):
            """ """
            return self._win


    class GameApp:
        """ """
        def __init__(self):
            """ """
            self._game = GameLogic()
            self._display = None

        def play(self):
            """ """
            player = self._game.get_player()
            while True:
                self.draw()
                action = input("Please input an action: ")

                # Quit
                if action == QUIT:
                    confirm = input("Are you sure you want to quit? (y/n): ")
                    if confirm == 'y':
                        return

                # Help
                elif action == HELP:
                    print(HELP_MESSAGE)

                # Investigate
                elif action.startswith('I ') and len(action) == 3:
                    direction = action[2]
                    if direction not in DIRECTIONS:
                        print(INVALID)
                        continue

                    entity = self._game.get_entity_in_direction(direction)
                    print(f'{entity} is on the {direction} side.')
                    player.change_move_count(-1)

                # Move Player
                elif action in DIRECTIONS:
                    direction = action
                    # if player does not collide move them
                    if not self._game.collision_check(direction):
                        self._game.move_player(direction)
                        entity = self._game.get_entity(player.get_position())

                        # process on_hit and check win state
                        if entity is not None:
                            entity.on_hit(self._game)
                            if self._game.won():
                                print(WIN_TEXT)
                                return
                    else:
                        print(INVALID)

                    player.change_move_count(-1)

                else:
                    print(INVALID)

                if self._game.check_game_over():
                    print(LOSE_TEST)
                    return

        def draw(self):
            """ """
            game_information = self._game.get_game_information()
            dungeon_size = self._game.get_dungeon_size()
            player = self._game.get_player()
            player_pos = player.get_position()
            moves = player.moves_remaining()

            self._display = Display(game_information, dungeon_size)
            self._display.display_game(player_pos)
            self._display.display_moves(moves)


    def main():
        app = GameApp()
        #app.play()


    if __name__ == "__main__":
        main()





















# Write your code here

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog

TASK_ONE = 1
TASK_TWO = 2


'''
Parameters that can be modified
'''
window_size = 600
dungeon_name = "game2.txt"
task_choose = TASK_TWO





class AbstractGrid(tk.Canvas):
    '''
    The following methods may be useful to include in the AbstractGrid class.
    '''
    def __init__(self, master, rows, cols, width, height, **kwargs):
        '''
        Set the size
        '''
        super().__init__(master, width = width, height = height, **kwargs)
        self._rows = rows
        self._cols = cols
        self._width = width
        self._height = height
        self._row_size = self._height / self._rows
        self._col_size = self._width / self._cols
        self.load_images()

    def load_images(self):
        '''
        Load the image and store it as a dict
        '''
        self.images = {}
        size = GameLogic(dungeon_name).get_dungeon_size()
        resize_size = (window_size // size, window_size // size)
        for entity in ("wall", "key", "player", "empty", "door", "moveIncrease"):
            self.images.update({entity:self.change_images(entity, resize_size)})
        self.images.update({'clock':self.change_images('clock', (window_size // 15, window_size // 12))})
        self.images.update({'lightning':self.change_images('lightning', (window_size // 20, window_size // 12))})
        self.images.update({'lives':self.change_images('lives', (window_size // 12, window_size // 12))})

    def get_images(self,entity):
        '''
        entity: str: the key of dict
        return: the value of dict
        '''
        return self.images[entity]

    def get_bbox(self, postiton):
        '''
        The tuples are the coordinates, 
            and you get the coordinates of the top left and bottom right
        postiton: (int, int): the coordinates of the square
        returns: int, int, int, int: The upper left coordinates, the lower right coordinates
        '''
        col, row = postiton
        x1 = col * self._col_size
        y1 = row * self._row_size
        x2 = x1 + self._col_size
        y2 = y1 + self._row_size
        return x1, y1, x2, y2

    def pixel_to_position(self, pixel):
        '''
        Get the coordinates of the square from the coordinates of the pixel
        pixel: (int, int): the coordinates of the graph
        return: int, int: the coordinates of the square
        '''
        row = pixel[1] // self._row_size
        col = pixel[0] // self._col_size
        return col, row

    def get_position_center(self, position):
        '''
        Get the center of the square by coordinates
        position: (int, int): the coordinates of the square
        return: int, int: the coordinates of the center of the square
        '''
        x1, y1, x2, y2 = self.get_bbox(position)
        x = (x1 + x2) / 2
        y = (y1 + y2) / 2
        return x, y

    def annotate_position(self, position, text):
        '''
        Annotates the cell at the given (row, col) position with the
            provided text.
        '''
        center_position = self.get_position_center(position)
        self.create_text(center_position, text = text)

    def change_images(self, name, resize_size):
        '''
        Modify the original image size
        name: str: Name of picture 
        resize_size: (int, int): Size of picture
        '''
        try:
            images_name = Image.open('images/{0}.gif'.format(name))
        except tk.TclError:
            images_name = Image.open('images/{0}.png'.format(name))
        return ImageTk.PhotoImage(images_name.resize(resize_size))

class DungeonMap(AbstractGrid):
    '''
    Draws the dungeon map
    '''
    def __init__(self, master, size, width = window_size, task = task_choose, **kwargs):
        '''
        Set the size of dungeon map
        '''
        super().__init__(master, rows = size, cols = size, width = width, height = width, **kwargs)
        self._size = size
        self._task = task

    def draw_graid(self, dungeon, player_position):
        '''
        Draws the dungeon on the DungeonMap based on dungeon,
            and draws the player at the specified (row, col) position.
        '''
        if self._task == 2:
            for row in range(self._size):
                for col in range(self._size):
                    self.create_image(self.get_position_center((col, row)), image = self.get_images('empty'))
        for entity in dungeon:
            x1, y1, x2, y2 = self.get_bbox(entity[::-1])
            if str(dungeon[entity]) == str(Key()):
                if self._task == 1:
                    self.create_rectangle(self.get_bbox(entity[::-1]), fill = 'yellow')
                    self.annotate_position(entity[::-1], 'Trash')
                elif self._task == 2:                   
                    self.create_image(self.get_position_center((entity[::-1])), image = self.get_images('key'))
            elif str(dungeon[entity]) == str(Door()):
                if self._task == 1:
                    self.create_rectangle(self.get_bbox(entity[::-1]), fill = 'red')
                    self.annotate_position(entity[::-1], 'Nest')
                elif self._task == 2:                   
                    self.create_image(self.get_position_center((entity[::-1])), image = self.get_images('door'))
            elif str(dungeon[entity]) == str(MoveIncrease()):
                if self._task == 1:
                    self.create_rectangle(self.get_bbox(entity[::-1]), fill = 'orange')
                    self.annotate_position(entity[::-1], 'Banana')
                elif self._task == 2:                   
                    self.create_image(self.get_position_center((entity[::-1])), image = self.get_images('moveIncrease'))
            elif str(dungeon[entity]) == str(Wall()):
                if self._task == 1:
                    self.create_rectangle(self.get_bbox(entity[::-1]), fill = 'dark grey')
                elif self._task == 2:                   
                    self.create_image(self.get_position_center((entity[::-1])), image = self.get_images("wall"))
        if self._task == 1:
            self._player = self.create_rectangle(self.get_bbox((player_position[1], player_position[0])), fill = 'medium spring green')
            self.annotate_position((player_position[1], player_position[0]), 'Ibis')
        elif self._task == 2:   
            self.create_image(self.get_position_center((player_position[1], player_position[0])), image = self.get_images("player"))

class KeyPad(AbstractGrid):
    '''
    Draws the keypad
    '''
    def __init__(self, master, width = window_size//3, height = window_size // 6, **kwargs):
        '''
        set the size of keypad
        '''
        super().__init__(master, rows = 2, cols = 3, width = width, height = height, **kwargs)
        self._width = width
        self._height = height

    def pixel_to_direction(self,pixel):
        '''
        Converts the x, y pixel position to the direction of the arrow depicted
            at that position.
        '''
        position = self.pixel_to_position(pixel)
        if position == (1,0):
            return 'W'
        elif position == (0,1):
            return 'A'
        elif position == (1,1):
            return 'S'
        elif position == (2,1):
            return 'D'

    def draw_keypad(self):
        '''
        Given the square coordinates, draw the four arrow keys
        '''
        self.create_rectangle(self.get_bbox((1,0)), fill = 'dark gray')
        self.annotate_position((1,0),'N')
        self.create_rectangle(self.get_bbox((0,1)), fill = 'dark gray')
        self.annotate_position((0,1),'W')
        self.create_rectangle(self.get_bbox((1,1)), fill = 'dark gray')
        self.annotate_position((1,1),'S')
        self.create_rectangle(self.get_bbox((2,1)), fill = 'dark gray')
        self.annotate_position((2,1),'E')

class Appendix(AbstractGrid):
    '''
    Draws the appendix
    '''
    def __init__(self, master, time = 0, **kwargs):
        '''
        set the size of appendix
        '''
        super().__init__(master, rows = 1, cols = 11, width = window_size//10, height = window_size//60, **kwargs)
        self._frame2 = tk.Frame(master)
        self._frame2.pack(side = tk.LEFT, padx = 15)
        self._frame3 = tk.Frame(master)
        self._frame3.pack(side = tk.LEFT, padx = 30)
        self._frame4 = tk.Frame(master)
        self._frame4.pack(side = tk.LEFT)
        self._time = time
        self._time_stop = False

    def display_show(self, start_move_left):
        '''
        Draw the frames for the second to fourth parts
            clock and time elapsed, lightning and moves left, lives 
        start_move_left: int
        '''
        label_clock = tk.Label(self._frame2, image = self.get_images("clock"))
        label_clock.pack(side = tk.LEFT)
        time_elapsed = tk.Label(self._frame2, text = 'Time elapsed', font = ('Arial', 15))
        time_elapsed.pack(side = tk.TOP, pady = 3)
        self._show_time = tk.Label(self._frame2, text = '0m 0s', font = ('Arial', 15))
        self._show_time.pack(side = tk.TOP, pady = 3)
        label_lightning = tk.Label(self._frame3, image = self.get_images("lightning"))
        label_lightning.pack(side = tk.LEFT)
        moves_left = tk.Label(self._frame3, text = 'Moves left', font = ('Arial', 15))
        moves_left.pack(side = tk.TOP, pady = 3)
        self._show_moves_left = tk.Label(self._frame3, font = ('Arial', 15), text = '{0} moves remaining'.format(start_move_left))
        self._show_moves_left.pack(side = tk.TOP, pady = 3)
        label_lives = tk.Label(self._frame4, image = self.get_images("lives"))
        label_lives.pack(side = tk.RIGHT)

    def change_moves_remaining(self, moves_remaining):
        '''
        Modify and display the remaining move steps in the frame
        moves_remaining: int
        '''
        self._show_moves_left.config(text = '{0} moves remaining'.format(moves_remaining))
    
    def run_time(self):
        '''
        Display and refresh time per second
        '''
        if not self._time_stop:
            self._time += 1
            self._show_time.config(text = '{:.0f}m {:.0f}s'.format(self._time // 60, self._time % 60))
            self.after(1000, self.run_time)

    def get_time(self):
        '''
        Get timekeeping time
        '''
        return self._time

class SampleApp(object):
    '''
    Integrate all the modules
    '''
    def __init__(self, master):
        '''
        Add the main window
        '''
        self._master = master
        self._master.title('Key cave Adventure Game')
        self.menuapp()

    def new_game(self):
        '''
        Delete the previous frame and restart the game
        '''
        self._frame_top.destroy()
        self._frame_bottom.destroy()
        self.start()

    def start(self):    
        '''
        Start the game
        '''
        self._game = GameLogic(dungeon_name)
        self._time = 0
        self._lives_left = 3
        self._player_history = list()
        self.add_frame()

    def add_frame(self):
        '''
        Add the main frame
        '''
        self._start_move_left = self._game.get_player().moves_remaining()
        self._frame_top = tk.Frame(self._master)
        self._frame_top.pack(side = tk.TOP)
        self._frame_bottom = tk.Frame(self._master)
        self._frame_bottom.pack(side = tk.BOTTOM)     
        self.add_frame_top()
        self.add_frame_bottom()

    def add_frame_top(self):
        '''
        Add the top frame, including tital, kungeon map and keypad
        '''
        self._total = tk.Label(self._frame_top, text = 'Key Cave Adventure Game', bg = 'medium spring green',font=('Arial',35))
        self._total.pack(fill = tk.X)
        self._dungeon = DungeonMap(self._frame_top, self._game.get_dungeon_size())
        self._dungeon.draw_graid(self._game.get_game_information(), self._game.get_player().get_position())
        self._dungeon.pack(side = tk.LEFT, anchor = tk.N)
        self._key = KeyPad(self._frame_top)
        self._key.draw_keypad()
        self._key.pack(side = tk.LEFT)
        self._key.bind("<Button-1>", self.press_mouse)
        self._key.bind_all("<Key>", self.press_keyboard)

    def add_frame_bottom(self):
        '''
        Add the bottom frame, including new game and quit, appendix, use life
        '''        
        self._frame1 = tk.Frame(self._frame_bottom) 
        self._frame1.pack(side = tk.LEFT, padx = 25)
        self._button_new_game = tk.Button(self._frame1, font = ('Arial', 15),text = 'New game', command = self.new_game)
        self._button_new_game.pack(pady = 3)
        self._button_quit = tk.Button(self._frame1, font = ('Arial', 15), text = 'Quit', command = self.quit)
        self._button_quit.pack(pady = 3)
        self._appendix = Appendix(self._frame_bottom, time = self._time)
        self._appendix.display_show(self._start_move_left)
        self._appendix.run_time()
        self._appendix.pack(side = tk.RIGHT)
        self._frame5 = tk.Frame(self._frame_bottom) 
        self._frame5.pack(side = tk.RIGHT, padx=10)
        self._lives_remaining = tk.Label(self._frame5, text = 'Lives remaining: {0}'.format(self._lives_left), font=('Arial', 15))
        self._lives_remaining.pack(side = tk.TOP, pady = 3)
        self._use_lives = tk.Button(self._frame5, font = ('Arial', 15),text = 'Use life', command = self.use_life)
        self._use_lives.pack(side = tk.TOP, pady = 3)

    def use_life(self):
        '''
        Player can return to the previous location
        '''
        if self._lives_left > 0 and len(self._player_history) > 0:
            self._time = self._appendix.get_time()
            self._game.get_player().set_position(self._player_history[-1])          
            self._game.get_player().change_move_count(1)
            self._player_history = self._player_history[:-1]
            self._lives_left -= 1
            self._frame_top.destroy()
            self._frame_bottom.destroy()
            self.add_frame()

    def press_mouse(self,e):
        '''
        Click the mouse to get the direction of the player movement
        '''
        if self._key.pixel_to_direction((e.x,e.y)) in DIRECTIONS:
            self._direction = self._key.pixel_to_direction((e.x,e.y))
            self.redraw()

    def press_keyboard(self,e):
        '''
        Get the player movement direction from the keyboard
        '''
        if e.keysym in DIRECTIONS:
            self._direction = e.keysym
            self.redraw()

    def redraw(self):
        '''
        Moving player on hit with other entities and gets the corresponding result
        '''
        self._player_history.append(self._game.get_player().get_position())
        if not self._game.collision_check(self._direction):
            self._game.move_player(self._direction)
            entity = self._game.get_entity(self._game.get_player().get_position())
            if entity is not None:
                entity.on_hit(self._game)
                if self._game.won():
                    self._appendix._time_stop = True
                    self.win_text()
            self._dungeon.delete(tk.ALL)
            self._dungeon.draw_graid(self._game.get_game_information(), self._game.get_player().get_position())
        self._game.get_player().change_move_count(-1)
        self._appendix.change_moves_remaining(self._game.get_player().moves_remaining())
        if self._game.check_game_over():
            self._appendix._time_stop = True        
            ans_lost = messagebox.askquestion('You lost!', 'You have finished the level with a score of {0}.\nWould you like to play again?'.format(self._appendix.get_time()))
            if ans_lost == 'yes':
                self.new_game()
            elif ans_lost == 'no':
                self.quit()

    def quit(self):
        '''
        Quit the game
        '''
        ans = messagebox.askokcancel('Verify exit', 'Really quit?')
        if ans:
            self._master.destroy()

    def win_text(self):
        '''
        Pop up the winning window and fill in the name
        '''
        self._score = self._appendix.get_time()
        self._window = tk.Tk()
        self._window.title('You Win!')
        self._window.geometry()
        self._label = tk.Label(self._window, text = 'You won in {0}m and {1}s! Enter your name: '.format(self._score // 60, self._score % 60))
        self._label.pack()
        self.entry = tk.Entry(self._window, show = None)
        self.entry.pack()
        def temp_text():
            self._entry_text = self.entry.get()
            self.enter_text()
        self._button_text = tk.Button(self._window, text = 'Enter', command = temp_text)
        self._button_text.pack()

    def enter_text(self):
        '''
        Add the winner's name and score to the document
        '''
        self._window.destroy()    
        if self._score // 60 == 0:
            self._score_str = '{0}s'.format(self._score%60)
        else:
            self._score_str = '{0}m {1}s'.format(self._score // 60, self._score % 60)
        self._text = '{0}: {1}\n'.format(self._entry_text, self._score_str)
        with open("high_score.txt", 'a') as rc:
            rc.write(self._text)
        self.top_3()

    def top_3(self):
        '''
        Pop up the three player names and times with the shortest time
        '''
        self._window_top_3 = tk.Tk()
        self._window_top_3.title('Top 3')
        self._window_top_3.geometry()
        self._label_title = tk.Label(self._window_top_3, text = 'High Scores', font = ('Arial', 45), bg='medium spring green')
        self._label_title.pack()
        try:
            self._label_high_scores = tk.Label(self._window_top_3, text = self.high_score())
            self._label_high_scores.pack()
        except:
            pass
        self._button_play_again = tk.Button(self._window_top_3, text = 'Done', command = self.play_again)
        self._button_play_again.pack()

    def play_again(self):
        '''
        After winning, a pop up window asks if you want to play again
        '''
        self._window_top_3.destroy()
        if self._appendix._time_stop:
            ans_win = messagebox.askquestion('You won!', 'You have finished the level with a score of {0}.\nWould you like to play again?'.format(self._appendix.get_time()))
            if ans_win == 'yes':
                self.new_game()
            elif ans_win == 'no':
                self.quit()

    def high_score(self):
        '''
        In comparison of time, only the first three players 
            with the shortest duration will be retained, 
            but only one player with the same name 
            and same time will be retained
        return: str
        '''
        output_text = str()
        temp = dict()
        score = dict()
        with open("high_score.txt", 'r') as fin:
            for line in fin:
                name = line.partition('\n')
                time = name[0].partition(':')
                clock = time[-1].partition('s')
                clock = clock[0].partition('m')
                if clock[1]:
                    time = int(clock[0]) * 60 + int(clock[-1])
                else:
                    time = int(clock[0])
                score.update({name[0]:time})
        high_scores = list(score.values())
        high_scores.sort()
        for length in range(len(high_scores)):
            for score_name, score_time in score.items():
                if high_scores[length] == score_time and len(temp) < 3:
                    temp.update({score_name:length + 1})
        for score_name in temp.keys():
            output_text += score_name + '\n'
        with open("high_score.txt", 'w') as rc:
            rc.write(output_text)
        return output_text[:-1]

    def menuapp(self):
        '''
        Add menu function
        '''
        self._menubar = tk.Menu(self._master)
        self._master.config(menu = self._menubar)
        self._filemenu = tk.Menu(self._menubar)
        self._menubar.add_cascade(label = "File", menu = self._filemenu)
        self._filemenu.add_command(label = "New", command = self.new_game)
        self._filemenu.add_command(label = "Save", command = self.save_file)
        self._filemenu.add_command(label = "Load", command = self.load_file)
        self._filemenu.add_command(label = "High Scores", command = self.top_3)
        self._filemenu.add_command(label = "Quit", command = self.quit)
        self._filename = None

    def save_file(self):
        '''
        Important data is added to the dict, 
            and finally converted to str format for storage in the document
        '''
        if self._filename is None:
            filename = filedialog.asksaveasfilename()
            if filename:
                self._filename = filename
        if self._filename:
            with open(self._filename, 'w') as fd:
                text = {}
                text['time'] = self._appendix.get_time()
                text['use_life'] = self._lives_left
                text['player_history'] = self._player_history
                text['moves_left'] = self._game.get_player().moves_remaining()
                text['player_position'] = self._game.get_player().get_position()
                text['key'] = str(self._game.get_entity(self._game.get_positions(KEY)[0]))
                text['moveIncrease'] = str(self._game.get_entity(self._game.get_positions(MOVE_INCREASE)[0]))
                fd.write(str(text))

    def load_file(self):
        '''
        The stored data is read out and 
            the value is paid to each important data. 
            If the data is not correct, starts the new game
        '''
        filename = filedialog.askopenfilename()
        if filename:
            self._filename = filename
            with open(filename, 'r') as fd:          
                try:
                    self._game = GameLogic(dungeon_name)
                    for line in fd:
                        line = eval(line)               
                    self._time = line['time']
                    self._player_history = line['player_history']
                    self._lives_left = line['use_life']
                    self._start_move_left = line['moves_left']
                    moves_remaining = line['moves_left'] - self._game.get_player().moves_remaining() 
                    self._game.get_player().change_move_count(moves_remaining) 
                    self._game.get_player().set_position(line['player_position'])
                    if line['key'] == 'None':
                        self._game.get_game_information().pop(self._game.get_positions(KEY)[0])
                        self._game.get_player().add_item(Key())
                    if line['moveIncrease'] == 'None':
                        self._game.get_game_information().pop(self._game.get_positions(MOVE_INCREASE)[0])
                    self._frame_top.destroy()
                    self._frame_bottom.destroy()
                    self.add_frame()
                except:
                    messagebox.showerror('maining','Please choose a right file!')

def main():

       
    root=tk.Tk()
    app = SampleApp(root)
    app.start()
    root.mainloop()


if __name__ == "__main__":
    main()


