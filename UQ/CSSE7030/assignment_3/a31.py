import tkinter as tk
import random
from tkinter import messagebox
import time
import ast
from tkinter import filedialog as fd
import os

# Change the TASK in the class PokemonGame.
TASK_ONE = 1
TASK_TWO = 2
UNEXPOSED = "~"
BOMB = "*"
FLAG = "!"
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"
DIRECTIONS = (UP, DOWN, LEFT, RIGHT,
              f"{UP}-{LEFT}", f"{UP}-{RIGHT}",
              f"{DOWN}-{LEFT}", f"{DOWN}-{RIGHT}")
SQUARE_SIZE = 60


class BoardModel:
    """The method of the game to make the game running."""
    def __init__(self, grid_size, num_pokemon):
        """The method of the game to make the game running.

        Parameters:
            grid_size(int): The number of rows and columns.
            num_pokemon(int): The number of pokemons that generated.
        """
        self._grid_size = grid_size
        self._num_pokemon = num_pokemon
        self._game_board = UNEXPOSED * grid_size ** 2
        self._pokemons = self.generate_pokemons()
        self._neighbours = []

    def get_grid_size(self):
        """To get the number of rows and columns.

        Return:
            self._grid_size(int): The number of rows and columns.
        """
        return self._grid_size

    def get_num_pokemon(self):
        """To get the number of pokemons.

        Return:
            self._num_pokemon(int): The number of pokemons.
        """
        return self._num_pokemon

    def get_game(self):
        """To get the game string.

        Return:
            self._game_board(str): The game string.
        """
        return self._game_board

    def check_pokemon(self, index):
        """To check the index position if has pokemons

        Parameter:
            index (int): The index in the game string where the character is replaced.

        Return:
            (bool): True if the index position has pokemon, false if not.
        """
        return index in self._pokemons

    def replace_character_at_index(self, index, character):
        """A specified index in the game string at the specified index is replaced by
        a new character.

        Parameters:
            index (int): The index in the game string where the character is replaced.
            character (str): The new character that will be replacing the old character.

        Returns:
            self._game_board(str): The updated game string.
        """
        self._game_board = self._game_board[:index] + character + self._game_board[index + 1:]

    def generate_pokemons(self):
        """Pokemons will be generated and given a random index within the game.

        Returns:
            pokemon_locations(tuple<int>): A tuple containing  indexes where the pokemons are
            created for the game string.
        """
        cell_count = self._grid_size ** 2
        pokemon_locations = ()

        for _ in range(self._num_pokemon):
            if len(pokemon_locations) >= cell_count:
                break
            index = random.randint(0, cell_count-1)

            while index in pokemon_locations:
                index = random.randint(0, cell_count-1)

            pokemon_locations += (index,)

        return pokemon_locations

    def pixel_to_position(self, pixel:tuple):
        """Convert the pixel coordinate in the window to the row, column coordinate in the grid.

        Return:
            (tuple<int, int>): The row, column position of a cell.
        """
        return pixel[0] // SQUARE_SIZE, pixel[1] // SQUARE_SIZE

    def index_in_direction(self, index, direction):
        """The index in the game string is updated by determining the
        adjacent cell given the direction.
        The index of the adjacent cell in the game is then calculated and returned.

        For example:
          | 1 | 2 | 3 |
        A | i | j | k |
        B | l | m | n |
        C | o | p | q |

        The index of m is 4 in the game string.
        if the direction specified is "up" then:
        the updated position corresponds with j which has the index of 1 in the game string.

        Parameters:
            index (int): The index in the game string.
            direction (str): The direction of the adjacent cell.

        Returns:
            (int): The index in the game string corresponding to the new cell position
            in the game.

            None for invalid direction.
        """
        # convert index to row, col coordinate
        col = index % self._grid_size
        row = index // self._grid_size
        if RIGHT in direction:
            col += 1
        elif LEFT in direction:
            col -= 1
        # Notice the use of if, not elif here
        if UP in direction:
            row -= 1
        elif DOWN in direction:
            row += 1
        if not (0 <= col < self._grid_size and 0 <= row < self._grid_size):
            return None
        return self.position_to_index((row, col))

    def position_to_index(self, position):
        """Convert the row, column coordinate in the grid to the game strings index.

        Parameters:
            position (tuple<int, int>): The row, column position of a cell.

        Returns:
            (int): The index of the cell in the game string.
        """
        x, y = position
        return x * self._grid_size + y

    def neighbour_directions(self, index):
        """Seek out all direction that has a neighbouring cell.

        Parameters:
            index (int): The index in the game string.

        Returns:
            (list<int>): A list of index that has a neighbouring cell.
        """
        neighbours = []
        for direction in DIRECTIONS:
            neighbour = self.index_in_direction(index, direction)
            if neighbour is not None:
                neighbours.append(neighbour)

        return neighbours

    def number_at_cell(self, pokemon_locations, index):
        """Calculates what number should be displayed at that specific index in the game.

        Parameters:
            pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
            index (int): Index of the currently selected cell

        Returns:
            (int): Number to be displayed at the given index in the game string.
        """
        if self._game_board[index] != UNEXPOSED:
            return int(self._game_board[index])

        number = 0
        for neighbour in self.neighbour_directions(index):
            if neighbour in pokemon_locations:
                number += 1

        return number

    def reveal_cells(self, pokemon_locations, index):
        """Reveals all neighbouring cells at index and repeats for all
        cells that had a 0.

        Does not reveal flagged cells or cells with Pokemon.

        Parameters:
            pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
            index (int): Index of the currently selected cell

        Returns:
            (str): The updated game string
        """
        number = self.number_at_cell(pokemon_locations, index)
        self.replace_character_at_index(index, str(number))
        clear = self.big_fun_search(pokemon_locations, index)
        for i in clear:
            if self._game_board[i] != FLAG:
                number = self.number_at_cell(pokemon_locations, i)
                self.replace_character_at_index(i, str(number))

    def big_fun_search(self, pokemon_locations, index):
        """Searching adjacent cells to see if there are any Pokemon"s present.

        Using some sick algorithms.

        Find all cells which should be revealed when a cell is selected.

        For cells which have a zero value (i.e. no neighbouring pokemons) all the cell"s
        neighbours are revealed. If one of the neighbouring cells is also zero then
        all of that cell"s neighbours are also revealed. This repeats until no
        zero value neighbours exist.

        For cells which have a non-zero value (i.e. cells with neighbour pokemons), only
        the cell itself is revealed.

        Parameters:
            pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.
            index (int): Index of the currently selected cell

        Returns:
            (list<int>): List of cells to turn visible.
        """
        queue = [index]
        discovered = [index]
        visible = []

        if self._game_board[index] == FLAG:
            return queue

        number = self.number_at_cell(pokemon_locations, index)
        if number != 0:
            return queue

        while queue:
            node = queue.pop()
            for neighbour in self.neighbour_directions(node):
                if neighbour in discovered:
                    continue

                discovered.append(neighbour)
                if self._game_board[neighbour] != FLAG:
                    number = self.number_at_cell(pokemon_locations, neighbour)
                    if number == 0:
                        queue.append(neighbour)
                visible.append(neighbour)
        return visible

    def flag_cell(self, index):
        """Toggle Flag on or off at selected index. If the selected index is already
        revealed, the game would return with no changes.

        Parameters:
            index (int): The index in the game string where a flag is placed.
        Returns
            (str): The updated game string.
        """
        if self._game_board[index] == FLAG:
            self.replace_character_at_index(index, UNEXPOSED)

        elif self._game_board[index] == UNEXPOSED:
            self.replace_character_at_index(index, FLAG)

    def left_pokemon(self):
        """Show the number of left pokeballs that player can use.

        Return:
            (int): The number of left pokeballs.
        """
        return self._num_pokemon - self.catches()

    def catches(self):
        """Show the number of catches.

        Return:
            catches(int): The number of catches.
        """
        catches = 0
        for d in self._game_board:
            if d == "!":
                catches += 1
        return catches

    def check_win(self, pokemon_locations):
        """Checking if the player has won the game.

        Parameters:
            pokemon_locations (tuple<int, ...>): Tuple of all Pokemon's locations.

        Returns:
            (bool): True if the player has won the game, false if not.

        """
        return UNEXPOSED not in self._game_board and self._game_board.count(FLAG) == len(pokemon_locations)

    def new_board(self):
        """Initialize the game board."""
        self._game_board = UNEXPOSED * self._grid_size ** 2


class BoardView(tk.Canvas):
    """View of the Pokemon game board"""
    def __init__(self, master, grid_size, board_width=600, task=1, *args, **kwargs):
        """Construct a board view from a board_layout.

        Parameters:
            master (tk.Widget): Widget within which the board is placed.
            grid_size(int): The number of rows and columns.
            board_width: The width of the widget.
            task (callable): Callable to call when set the task.
        """
        super().__init__(master, *args, **kwargs)
        self._master = master
        self._grid_size = grid_size
        self._board_width = board_width
        self["width"] = board_width
        self["height"] = board_width
        self._model = None
        self._bar = None
        self._img_ref = []
        self._image = None
        self._state = True
        self._task = task

        self.bind("<Button-1>", lambda e: self.left_click((e.y, e.x)))
        self.bind("<Button-2>", lambda e: self.right_click((e.y, e.x)))
        self.bind("<Button-3>", lambda e: self.right_click((e.y, e.x)))

    def draw_board(self, board: BoardModel):
        """Construct how to draw the game board. Create the view of the game.

        Parameter:
            board(BoardModel): A BoardModel which is instantiated.

        The content of the position should be draw.
        """
        self._model = board
        self.delete(tk.ALL)
        for i in range(self._grid_size):
            for j in range(self._grid_size):
                char = self._model.get_game()[self._model.position_to_index((i, j))]
                x1 = j * SQUARE_SIZE
                y1 = i * SQUARE_SIZE
                x2 = x1 + SQUARE_SIZE
                y2 = y1 + SQUARE_SIZE
                if char == UNEXPOSED:
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="dark green")
                    elif self._task == 2:
                        self._image = get_image("images/unrevealed")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "*":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="yellow")

                    elif self._task == 2:
                        self._image = get_image("images/pokemon_sprites/" + random_image("images/pokemon_sprites"))
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "!":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="red")

                    elif self._task == 2:
                        self._image = get_image("images/pokeball")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)


                elif char == "0":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="0")

                    elif self._task == 2:
                        self._image = get_image("images/zero_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)


                elif char == "1":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="1")

                    elif self._task == 2:
                        self._image = get_image("images/one_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)


                elif char == "2":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="2")

                    elif self._task == 2:
                        self._image = get_image("images/two_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "3":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="3")

                    elif self._task == 2:
                        self._image = get_image("images/three_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "4":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="4")

                    elif self._task == 2:
                        self._image = get_image("images/four_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "5":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="5")

                    elif self._task == 2:
                        self._image = get_image("images/five_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "6":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="6")

                    elif self._task == 2:
                        self._image = get_image("images/six_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "7":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="7")

                    elif self._task == 2:
                        self._image = get_image("images/seven_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

                elif char == "8":
                    if self._task == 1:
                        self.create_rectangle(x1, y1, x2, y2, fill="#6DE44E")
                        self.create_text((x1 + x2) / 2, (y1 + y2) / 2, text="8")

                    elif self._task == 2:
                        self._image = get_image("images/eight_adjacent")
                        self.create_image((x1 + x2) / 2, (y1 + y2) / 2, image=self._image)
                        self._img_ref.append(self._image)

    def right_click(self, click):
        """Construct the right click event

        Parameter:
            click(pixel(x, y)): The pixel of the mouse click position.

        Return:
            The way to handle the right click event.
        """
        if self._state == True:
            position = self._model.pixel_to_position(click)
            index = self._model.position_to_index(position)
            if self._model.left_pokemon() >= 1:
                self._model.flag_cell(index)
                self.draw_board(self._model)
                self._model.left_pokemon()
                self._model.catches()

        if self._model.check_win(self._model._pokemons):
            for a in self._model._pokemons:
                self._model.replace_character_at_index(a, "*")
                self.draw_board(self._model)
            if self._task == 2:
                self.win_the_game()
                self.update_bar(self._bar)

    def update_bar(self, bar):
        """To update the status bar

        Parameter:
            bar(StatusBar): A StatusBar which is instantiated.

        Return:
            A status bar that was updated.
        """
        self._bar = bar
        self._bar.updatebar()

    def left_click(self, click):
        """Construct the left click event

        Parameter:
            click(pixel(x, y)): The pixel of the mouse click position.

        Return:
            The way to handle the left click event.
        """
        if self._state == True:
            position = self._model.pixel_to_position(click)
            index = self._model.position_to_index(position)
            if self._model.check_pokemon(index):
                for a in self._model._pokemons:
                    self._model.replace_character_at_index(a, "*")
                self.draw_board(self._model)
                self._state = False
                if self._task == 2:
                    self.lose_the_game()
            elif self._model.get_game()[index] == "!":
                pass
            else:
                self._model.reveal_cells(self._model._pokemons, index)
                self.draw_board(self._model)
                if self._model.check_win(self._model._pokemons):

                    for a in self._model._pokemons:
                        self._model.replace_character_at_index(a, "*")
                        self.draw_board(self._model)

                    if self._task == 2:
                        self.win_the_game()

    def lose_the_game(self):
        """To tell the player lose the game.

        A message box to tell the player lose the game."""
        self._bar.stoptime()
        self.draw_board(self._model)
        self._master.update_idletasks()

        answer = messagebox.askyesno("Game over", "You lose! Would you like to play again?")

        if answer:

            self._state = True
            self._bar.new_game()

        else:
            self._master.destroy()

    def win_the_game(self):
        """To tell the player win the game.

        A message box to tell the player win the game."""
        self._master.update_idletasks()
        self._bar.stoptime()
        messagebox.showinfo("Congratulations", "Congratulations! You win!")
        self.input_name()

    def input_name(self):
        """When player's time record in top three let the player input their name to save their record."""
        self._bar.stoptime()
        self._tl1 = tk.Toplevel()
        self._tl1.title("You Win!")
        self._won = tk.Label(self._tl1, text='You won in ' + self._bar._last + '! Enter your name:').pack(fill=tk.X)
        self.Varmin = tk.StringVar()
        self.entryname = tk.Entry(self._tl1, textvariable=self.Varmin)
        self.entryname.pack()
        self._ent = tk.Button(self._tl1, text='Entry', command=self.entry_fun).pack()

    def entry_fun(self):
        """The widget let player input their name."""
        with open("recording.txt", 'a') as rc:
            self._recording = str(str(self.entryname.get()) + ':' + str(self._bar._last) + '\r\n')
            rc.write(self._recording)
        self._tl1.destroy()
        self._bar.stoptime()


class PokemonGame:
    """PokemonGame that manages communication between the board model, board view and status bar."""
    def __init__(self, master, grid_size=10, num_pokemon=15, task=TASK_TWO):
        """Create a new pokemon game within a master widget"""
        self._master = master
        master.title("Pokemon: Got 2 Find Them All!")
        self._grid_size = grid_size
        self._num_pokemon = num_pokemon
        self._task = task
        self._filename = None
        self._tl = None
        self._li = ["","",""]

        self._model = BoardModel(grid_size, num_pokemon)
        #self._game = PokemonGame(self._master, self._grid_size, self._num_pokemon, self._task)

        self._view = None
        self._image = None
        self._bar = None
        self.draw()
        self.menu()
        #self.find_top3()
        ####################I tried to finish this task, but I failed.#####################

    def draw(self):
        """Create the interface of the game in the master widget."""
        label = tk.Label(self._master, text="Pokemon: Got 2 Find Them All!", bg="#CD5C5C", fg="white",
                         font=('Chalkboard', 20, 'bold'))
        label.pack(fill=tk.X)
        self._view = BoardView(self._master, self._grid_size, self._grid_size * SQUARE_SIZE, self._task)
        self._view.pack()
        if self._task == 2:
            self._bar = StatusBar(self._master, self._model, self._view, self._model.get_game(), self._grid_size, self._num_pokemon)
            self._bar.pack()
            self._view.update_bar(self._bar)
            self._view.pack()
        self._view.draw_board(self._model)
        self._view.pack()

    def menu(self):
        """Create the menu bar of the game."""
        menubar = tk.Menu(self._master)
        self._master.config(menu=menubar)
        filemenu = tk.Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="Save game", command=self.save_game)
        filemenu.add_command(label="Load game", command=self.load_game)
        filemenu.add_command(label="Restart game", command=self._bar.restart_game)
        filemenu.add_command(label="New game", command=self._bar.new_game)
        filemenu.add_command(label="High scores", command=self.high_score)
        filemenu.add_command(label="Quit", command=self.quit)

    def save_game(self):
        """Prompt the user for the location to save their file.
        Save information to replicate the current state of the game.
        """
        filename = fd.asksaveasfilename()
        if filename:
            self._filename = filename
        if self._filename:
            with open(self._filename, 'w') as sv:
                self._record = str({'grid_size': str(self._grid_size),
                                    'num_pokemon': str(self._num_pokemon),
                                    'time': str(self._bar._last),
                                    'game_board': str(self._model.get_game())})
                sv.write(self._record)
                sv.close()

    def load_game(self):
        """Prompt the user for the location of the file to load a game from and load the game described in that file."""
        filename = fd.askopenfilename()
        if filename:
            self._filename = filename
            with open(self._filename, 'r') as ld:
                for line in ld:
                    dic = line
                    diction = ast.literal_eval(dic)
                    self._grid_size = diction['grid_size']
                    self._num_pokemon = diction['num_pokemon']
                    self._bar._last = diction['time']
                    self._model._game_board = diction['game_board']
            ld.close()
            self._view.draw_board(self._model)
            self._bar.updatebar()

###############I tried this task, but I was stucked, really don't know how to solve it.###########
    def high_score(self):
        """The interface of the high score of top three record."""
        self._tl = tk.Toplevel()
        self._tl.title("Top 3")
        self._top = tk.Label(self._tl, text='High Scores', bg="#CD5C5C", fg="white",
                         font=('Chalkboard', 20, 'bold')).pack(fill=tk.X)
        self._1 = tk.Label(self._tl, text=self._li[0]).pack()
        self._2 = tk.Label(self._tl, text=self._li[1]).pack()
        self._3 = tk.Label(self._tl, text=self._li[2]).pack()
        self._done = tk.Button(self._tl, text="Done", command=self.done).pack()

    def grades(self):
        pass

    def input_name(self):
        """When player's time record in top three let the player input their name to save their record."""
        self._bar.stoptime()
        self._tl1 = tk.Toplevel()
        self._tl1.title("You Win!")
        self._won = tk.Label(self._tl1, text='You won in ' + self._bar._last + '! Enter your name:').pack(fill=tk.X)
        self.Varmin = tk.StringVar()
        self.entryname = tk.Entry(self._tl1, textvariable=self.Varmin)
        self.entryname.pack()
        self._ent = tk.Button(self._tl1, text='Entry', command=self.entry_fun).pack()

    def entry_fun(self):
        """The widget let player input their name."""
        with open("recording.txt", 'a') as rc:
            self._recording = str(str(self.entryname.get()) + ':' + str(self._bar._last) + '\r\n')
            rc.write(self._recording)
        self._tl1.destroy()
        self._bar.stoptime()

    def find_top3(self):
        """Find the top three record."""
        top1 = float("inf")
        top2 = float("inf")
        top3 = float("inf")
        with open("recording.txt", 'r') as fin:
            for line in fin:
                name, _, line = line.partition(":")
                time, _, _, = line.partition('\n')
                #print(name,time)
        for a in time:
            if int(a) < top1:
                top1 = a
            if int(a) >= top2:
                top2 = a
            if int(a) >= top3:
                top3 = a

    def showtop(self):
        """Show the top."""
        self._li = []
        with open("recording.txt", 'r') as fin:
            for lin in fin:
                self._li.append(lin)
        return self._li



    def done(self):
        """When press done, the window close."""
        self._tl.destroy()

    def quit(self):
        """To quit the game."""
        answer = messagebox.askyesno("Quit the game", "Are you sure to quit the game?")
        if answer:
            self._master.quit()


class StatusBar(tk.Frame):
    """Statusbar display relevent game information and function buttons.
    Show the number of attemped catches and pokeballs left. The time of playing game.
    And one of the button is to start a new game. The other one is to restart the game
    """
    def __init__(self, master, model, view, game_board, grid_size, num_pokemon, paused = True,
                 stop = False, *args, **kwargs):
        """
        Construct a new status bar frame.

        Parameters:
            master (tk.Widget): Widget within which to place the status bar.
            game_board (list<grid>): The grid content in a board.
            grid_size (int): The number of rows and columns
            num_pokemon (int): The number of the pokemons.
            model (BoardModel): A BoardModel which is instantiated.
            view (BoardView): A BoardView which is instantiated.
            paused (bool): The status of the time.
        """
        super().__init__(master, *args, **kwargs)
        self._master = master
        self.pack()
        self._game_board = game_board
        self._grid_size = grid_size
        self._num_pokemon = num_pokemon
        self._model = model
        self._view = view
        self._paused = True
        self._stop = stop

        self.createWidget()
        self.start()

    def createWidget(self):
        """create component"""

        self._frame = tk.Frame(self._master)
        self._frame.pack(side=LEFT)

        global image
        image = get_image("images/full_pokeball")
        self.label1 = tk.Label(self._frame, image=image)
        self.label1.pack(side=tk.LEFT)
        self._label3 = tk.Label(self._frame, text=f"{self._model.catches()} attemped catches")
        self._label3.pack()
        self._label4 = tk.Label(self._frame, text=f"{self._model.left_pokemon()} pokeballs left")
        self._label4.pack()

        self._frame1 = tk.Frame(self._master)
        self._frame1.pack(side=tk.LEFT)

        global image1
        image1 = get_image("images/clock")
        self.label5 = tk.Label(self._frame1, image=image1)
        self.label5.pack(side=tk.LEFT)

        self._label6 = tk.Label(self._frame1, text="Time elapsed")
        self._label6.pack()
        self._display = tk.Label(self._frame1, text='0m 0s')
        self._display.pack()

        self._frame2 = tk.Frame(self._master)
        self._frame2.pack(side=tk.LEFT)

        self._button1 = tk.Button(self._frame2, text="New game", command=self.new_game)
        self._button1.pack()
        self._button2 = tk.Button(self._frame2, text="Restart game", command=self.restart_game)
        self._button2.pack()

    def updatebar(self):
        """Update the information of the status bar."""
        self._label3.config(text=f"{self._model.catches()} attemped catches")
        self._label4.config(text=f"{self._model.left_pokemon()} pokeballs left")
        self._display.config(text=self._last)

    def start(self):
        """Record the start time."""
        if self._paused:
            self._starttime = time.time()
            self._paused = False
            self.run_timer()

    def run_timer(self):
        """Record the time of the game."""
        self._delta = time.time() - self._starttime
        self._last = '{:.0f}m {:.0f}s'.format(*divmod(self._delta, 60))
        self.updatebar()
        if self._stop == False:
            self._display.after(1000, self.run_timer)

    def retime(self):
        """Initialize the time into 0m 0s."""
        self._display.config(text="0m 0s")
        self._paused = True
        self.start()

    def stoptime(self):
        """Stop recording the time."""
        self._stop = True

    def restart_game(self):
        """Restart the game on the current level."""
        self._model.new_board()
        self._view.draw_board(self._model)
        self._frame.destroy()
        self._frame1.destroy()
        self._frame2.destroy()
        self.__init__(self._master, self._model, self._view, self._model.get_game(), self._grid_size, self._num_pokemon)


    def new_game(self):
        """To start a new game."""
        #self._view.destroy()
        self._frame.destroy()
        self._frame1.destroy()
        self._frame2.destroy()
        self._model.__init__(self._grid_size, self._num_pokemon)
        self._view.draw_board(self._model)
        self.__init__(self._master, self._model, self._view, self._model.get_game(), self._grid_size, self._num_pokemon)
        self._view._state = True
        print("new game1")
        print(self._view._state)


def get_image(image_name):
    """(tk.PhotoImage) Get a image file based on capability.

    If a .png doesn't work, default to the .gif image.
    """
    try:
        image = tk.PhotoImage(file=image_name + ".png")
    except tk.TclError:
        image = tk.PhotoImage(file=image_name + ".gif")
    return image


def random_image(file):
    """Random choose a image from the file.

    Parameter:
        file: The path of the file.

    Return:
        randomtu(str): The name of the file.
    """
    for dir_info in os.walk(file):
        dir_name, _, file_names = dir_info
        temp = []
        for file_name in file_names:
            temp.append(file_name)
        if len(temp) == 0:
            continue
        randomfile = random.choice(temp)
        randomtu = (randomfile.split(".", 1))[0]

        return randomtu


def main():
    root = tk.Tk()
    PokemonGame(root)
    root.update()
    root.mainloop()

if __name__ == "__main__":
    main()
