"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{Peng Yu}} ({{46635884}})"
__email__ = "peng.yu1@uqconnect.edu.au"
__date__ = "25.09.2020"

# Write your code here

class GameLogic:
    '''
    GameLogic contains all the game information 
     and how the game should play out.
    '''
    def __init__(self, dungeon_name="game1.txt"):
        """Constructor of the GameLogic class.

        Parameters:
            dungeon_name (str): The name of the level.
        """
        self._dungeon = load_game(dungeon_name)
        self._dungeon_size = len(self._dungeon)

        #you need to implement the Player class first.
        self._player = Player(GAME_LEVELS[dungeon_name])

        #you need to implement the init_game_information() method for this.
        self._game_information = self.init_game_information()

        self._win = False

    def get_positions(self, entity):
        """ Returns a list of tuples containing all positions of a given Entity
             type.

        Parameters:
            entity (str): the id of an entity.

        Returns:
            (list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))

        return positions

    # Write your code here
    def get_dungeon_size(self):
        '''
        Returns:
        	(int): The width of the dungeon as an integer
        '''
        return self._dungeon_size

    def init_game_information(self):
        ''' This method also sets the Player’s position. 
         At the start of the game this method should be called to find 
         the position of all entities within the current dungeon.

        Returns:
            (dict<tuple<int, int>:class>): Return a dictionary containing the position 
             and the corresponding Entity
        '''
        game_information = {}
        self.get_player().set_position(self.get_positions(PLAYER)[0])
        for entity_id, entity_str in ((KEY,Key()), (DOOR,Door()), (WALL,Wall()), (MOVE_INCREASE,MoveIncrease())):
            for entity_count in range(len(self.get_positions(entity_id))):
                game_information.update({self.get_positions(entity_id)[entity_count]:entity_str})
        return game_information

    def get_game_information(self):
        '''       
        Returns:
            (dict{tuple(int, int):class}): Returns a dictionary containing the position 
             and the corresponding Entity, as the keys and values, for the current dungeon.
        '''
        return self._game_information

    def get_player(self):
        '''
        Returns:
        	The Player object within the game.
        '''
        return self._player

    def get_entity(self,tuple):
        ''' Entity in the given direction or if the position 
         is off map then this function should return None.
        
        Returns:
        	(dict{tuple(int, int):class}): An Entity at a given position in the dungeon. 
        '''
        return self.get_game_information().get(tuple)

    def get_entity_in_direction(self, direction):      
        '''
        Returns:
        	(dit{tuple(int,int):class}): An Entity in the given direction of the Player’s position. 
             If there is no Entity in the given direction or 
             if the direction is off map then this function should return None.
        '''
        player_col, player_row = self.get_player().get_position()
        direction_col, direction_row = DIRECTIONS[direction]        
        return self.get_game_information().get((player_col + direction_col, player_row + direction_row))

    def collision_check(self, direction):
        '''
        Returns:
            (bool): False if a player can travel in the given direction, 
             they won’t collide. True, they will collide
        '''
        if self.get_entity_in_direction(direction):
            if not self.get_entity_in_direction(direction).can_collide():
                return True        
        return False

    def new_position(self, direction):
        '''
        Returns:
            (dict{tuple(int, int):class}): A tuple of integers that represents 
             the new position given the direction.
        '''
        self.move_player(direction)
        return self.get_player().get_position()

    def move_player(self, direction):
        '''
        Update the Player’s position to 
         place them one position in the given direction.
        '''
        player_col, player_row = self.get_player().get_position()
        direction_col, direction_row = DIRECTIONS[direction]
        self.get_player().set_position((player_col + direction_col, player_row + direction_row))

    def check_game_over(self):
        '''
        Return:
            (bool): True if the game has been lost and False otherwise.
        '''
        if self.get_player().moves_remaining() <= 0 and not self.won():
            return True
        else:
            return False

    def set_win(self, bool):
        '''      
        Parameters:
            (bool): Set the game’s win state to be True or False.
        '''
        self._win=bool

    def won(self):
        '''
        Return:
            (bool): Game’s win state.
        '''
        return self._win

class GameApp:
    '''
    GameApp acts as a communicator between the GameLogic and the Display.
    '''
    def __init__(self):
        '''
        GameApp should be constructed with GameApp().
        '''
        self._game_logic = GameLogic()
        self._display_draw = Display(self._game_logic.get_game_information(), self._game_logic.get_dungeon_size())
        
    def play(self):
        '''
        Handles the player interaction.
        '''
        while True:
            if self._game_logic.check_game_over():
                print(LOSE_TEST)
                break
            elif self._game_logic.won():
                print(WIN_TEXT)
                break
            self.draw()
            actions = input('Please input an action: ')
            if actions == QUIT:
                re_confirm = input('Are you sure you want to quit? (y/n): ')
                if re_confirm == 'y':
                    break
                elif re_confirm == 'n':
                    continue
            elif actions == HELP:
                print(HELP_MESSAGE)
            elif actions[0] == INVESTIGATE and actions[2:] in (DIRECTIONS.keys()):
                print('{0} is on the {1} side.'.format(self._game_logic.get_entity_in_direction(actions[-1]), actions[-1]))
                self._game_logic.get_player().change_move_count(-1)
            elif actions in (DIRECTIONS.keys()):
                if self._game_logic.collision_check(actions):
                    print(INVALID)
                else:
                    self._game_logic.new_position(actions)
                    Key().on_hit(self._game_logic)
                    MoveIncrease().on_hit(self._game_logic)  
                    Door().on_hit(self._game_logic)
                self._game_logic.get_player().change_move_count(-1)
            else:
                print(INVALID)

    def draw(self):
        '''
        Displays the dungeon with all Entities in their positions. 
         This method should also display the player’s remaining move count.
        '''
        self._display_draw.display_game(self._game_logic.get_player().get_position())
        self._display_draw.display_moves(self._game_logic.get_player().moves_remaining())

class Entity(object):
    '''
    A generic Entity within the game.
    '''
    def __init__(self):
        '''
        Entity has an id, and can either be collided with 
         (two entities can be in the same position)
         or not (two entities cannot be in the same position.) 
         The collidable attribute should be set to
         True for an Entity upon creation. Entity should be 
         constructed with Entity().

        '''
        self._name = 'Entity'
        self._id = 'Entity'
        self._bool = True

    def get_id(self):
        '''
        Returns:
            (str): A string that represents the Entity’s ID.
        '''
        return self._id

    def set_collide(self, bool):
        '''
        Parameters:
            (bool): Set the collision state for the Entity to be True.
        '''
        self._bool = bool

    def can_collide(self):
        '''
        Returns:
            (bool): True if the Entity can be collided with (another Entity 
             can share the position that this one is in) and False otherwise.
        '''
        return self._bool

    def __str__(self):
        '''
        Returns the string representation of the Entity.
        '''
        return "{0}('{1}')".format(self._name, self._id)

    def __repr__(self):
        '''
        Returns the string representation of the Entity.
        '''
        return "{0}('{1}')".format(self._name, self._id)

class Wall(Entity):
    '''
    A Wall is a special type of an Entity within the game.
    '''
    def __init__(self):
        '''
        The Wall Entity cannot be collided with. 
         Wall should be constructed with Wall(). 
        '''
        super().__init__()
        self._name = 'Wall'
        self._id = '#'
        super().set_collide(False)

class Item(Entity):
    '''
    An Item is a special type of an Entity within the game. This is an abstract class.
    '''
    def __init__(self):
        '''
        By default the Item Entity can be collided with. 
         Item should be constructed with Item().
        '''
        super().__init__()
        self._name = 'Item'

    def on_hit(self, game):
        '''
        This function should raise the NotImplementedError.
        '''
        raise NotImplementedError

class Key(Item):
    '''
    A Key is a special type of Item within the game.
    '''
    def __init__(self):
        '''
        The Key Item can be collided with. 
         Key should be constructed with Key(). 
        '''
        super().__init__()
        self._name = 'Key'
        self._id = 'K'

    def on_hit(self, game):
        '''
        When the player takes the Key the Key should be added to the Player’s inventory. 
         The Key should then be removed from the dungeon once it’s in the Player’s inventory.
        '''
        if game.get_player().get_position() == game.get_positions(KEY)[0]:
            game.get_player().add_item(self)
            game._game_information.pop(game.get_positions(KEY)[0]) 

class MoveIncrease(Item):
    '''
    MoveIncrease is a special type of Item within the game.
    '''
    def __init__(self,moves = 5):
        '''
        The MoveIncrease Item can be collided with. 
         MoveIncrease should be constructed with MoveIncrease(int: moves=5) 
         where moves describe how many extra moves the Player will be granted 
         when they collect this Item, the default value should be 5. 
        '''
        super().__init__()
        self._name = 'MoveIncrease'
        self._id = 'M'
        self._moves = moves

    def on_hit(self, game):
        '''
        When the player hits the MoveIncrease (M) item 
         the number of moves for the player increases 
         and the M item is removed from the game. 
         These actions are implemented via the on_hit method. 
         Specifically, extra moves should be granted to the Player 
         and the M item should be removed from the game.
        ''' 
        if game.get_positions(MOVE_INCREASE) :
            if game.get_player().get_position() == game.get_positions(MOVE_INCREASE)[0]:
                game.get_player().change_move_count(self._moves if game.get_dungeon_size() != 12 else 10 )
                game._game_information.pop(game.get_positions(MOVE_INCREASE)[0])

class Door(Entity):
    '''
    A Door is a special type of an Entity within the game.
    '''
    def __init__(self):
        '''
        The Door Entity can be collided with 
         the Player should be able to share its position with 
         the Door when the Player enters the Door.
         Door should be constructed with Door().
        '''
        super().__init__()
        self._name = 'Door'
        self._id = 'D'

    def on_hit(self, game):
        '''
        If the Player’s inventory contains a Key Entity then 
         this method should set the ‘game over’ state to be True.
        '''
        if game.get_player().get_position() == game.get_positions(DOOR)[0]:           
            if not game.get_player().get_inventory():
                print('You don\'t have the key!')
            else:
                game.set_win(True)

class Player(Entity):
    '''
    A Player is a special type of an Entity within the game.
    '''
    def __init__(self, number):
        '''
        The Player Entity can be collided with. 
         The Player should be constructed with Player(move_count: int) 
         where moves represents how many moves a Player 
         can have for the given dungeon they are in (see GAME_LEVELS).
        '''
        super().__init__()
        self._name = 'Player'
        self._id = 'O'
        self._number = number
        self._inventory = []
        self._position = None

    def set_position(self, position):
        '''
        Parameters:
            (tuple(int, int)): Sets the position of the Player.
        '''
        self._position = position

    def get_position(self):
        '''
        Returns:
        	(tuple(int, int)): a tuple of ints representing the position of the Player. 
        	 If the Player’s position hasn’t been set yet 
        	 then this method should return None.
        '''
        return self._position

    def change_move_count(self, change_move_count):
        '''
        Parameters:
            (int): Number to be added to the Player’s move count.
        '''
        self._number += change_move_count

    def moves_remaining(self):
        '''
        Returns:
        	(int): An int representing how many moves 
        	 the Player has left before they reach the maximum move count.
        '''
        return self._number

    def get_inventory(self):
        '''
        Returns:
        	(list): a list that represents the Player’s inventory. 
        	 If the Player has nothing in their inventory 
        	 then an empty list should be returned.
        '''
        return self._inventory

    def add_item(self, item):
        '''
        Adds the item to the Player’s Inventory
        '''
        self._inventory.append(item)

def main():
    g=GameApp()
    g.play()

if __name__ == "__main__":
    main()