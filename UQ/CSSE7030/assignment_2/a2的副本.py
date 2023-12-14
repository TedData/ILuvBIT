"""
CSSE1001 Assignment 2
Semester 2, 2020
"""
from a2_support import *

# Fill these in with your details
__author__ = "{{user.name}} ({{user.id}})"
__email__ = ""
__date__ = ""

# Write your code here

class GameLogic:
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
            )list<tuple<int, int>>): Returns a list of tuples representing the 
            positions of a given entity id.
        """
        positions = []
        for row, line in enumerate(self._dungeon):
            for col, char in enumerate(line):
                if char == entity:
                    positions.append((row,col))
            #要删除，list里是所有的点
        return positions

    # Write your code here
    def get_dungeon_size(self):
        return self._dungeon_size
    def init_game_information(self):
        game_information={}
        try:
            for i, j in ((KEY,Key()),(DOOR,Door()),(WALL,Wall()),(MOVE_INCREASE,MoveIncrease())):#,
                for length in range(len(self.get_positions(i))):
                    game_information.update({self.get_positions(i)[length]:j})
        except :
            pass
        #self._player.set_position(self.get_positions(PLAYER)[0]) 
        return game_information
    def get_game_information(self):
        return self._game_information
    def get_player(self):
        return self._player
    def get_entity(self,tuple1):
        return self.get_game_information().get(tuple1)
    def get_entity_in_direction(self, direction1):       
        i,j=self.get_player().get_position()
        m,n=DIRECTIONS[direction1]
        new_position=(i+m,j+n)
        return self.get_game_information().get(new_position)
    def collision_check(self, direction1):
        if str(self.get_entity_in_direction(direction1))==repr(Wall()):
            return True
        else:
            return False
    def new_position(self, direction1):
        self.move_player(direction1)
        return self.get_player().get_position()
    def move_player(self, direction1):
        m,n=self.get_player().get_position()
        i,j=DIRECTIONS[direction1]
        new_position=(m+i,n+j)
        self.get_player().set_position(new_position)           
    def check_game_over(self):        
        if self.get_player().get_position() == self.get_positions(DOOR)[0]:           
            if self.get_player().get_inventory():
                return True 
        if self.get_player().moves_remaining() <= 1:
            return False
    def set_win(self, bool1):
        if bool1==True:            
            print(WIN_TEXT)
        elif bool1 == False: 
            print(LOSE_TEST)
    def won(self,bool1):
        self._win = bool1
        return self._win

class GameApp:
    def __init__(self):
        self._game_logic=GameLogic()
        self._entity=Entity()
        self._key=Key()
        self._wall=Wall()
        self._item=Item()
        self._move_increase=MoveIncrease()
        self._door=Door()
        self._display=Display(self._game_logic.get_game_information(),self._game_logic._dungeon_size)
        self._game_logic.get_player().set_position(self._game_logic.get_positions(PLAYER)[0])
        self.play()
    def play(self):
        while True:
            self.draw()
            s=input('Please input an action: ')
            if s==QUIT:
                break
            elif s[0]==INVESTIGATE:
                if s[-1] in (DIRECTIONS.keys()):
                    print('{0} is on the  {1} side.'.format(self.entity_in_direction(s[-1]),s[-1]))
                    self._game_logic.get_player().change_move_count(-1)
            elif s==HELP:
                print(HELP_MESSAGE)
            elif s in (DIRECTIONS.keys()):
                if not self._game_logic.collision_check(s):
                    self._game_logic.new_position(s)
                    self._door.on_hit(self._game_logic)
                    if self._game_logic.check_game_over() != None:
                        self._game_logic.set_win(self._game_logic.won(self._game_logic.check_game_over()))
                        break                    
                else:
                    print(INVALID)
                self._game_logic.get_player().change_move_count(-1)
                self._key.on_hit(self._game_logic)
                self._move_increase.on_hit(self._game_logic)             
    def entity_in_direction(self, direction1):
        return self._game_logic.get_entity_in_direction(direction1)   
    def draw(self):
        self._display.display_game(self._game_logic.get_player().get_position())
        self._display.display_moves(self._game_logic.get_player().moves_remaining())

class Entity(object):
	def __init__(self):
		self._name = 'Entity'
		self._id = 'Entity'
		self._bool1 = True
	def get_id(self):
		return self._id
	def set_collide(self,bool1):
		self._bool1 = bool1
	def can_collide(self):
		return self._bool1	
	def __str__(self):
		x = "{0}('{1}')".format(self._name, self._id)
		return x
	def __repr__(self):
		x = "{0}('{1}')".format(self._name, self._id)
		return x

class Wall(Entity):
	def __init__(self):
		self._name = 'Wall'
		self._id = '#'
		#self._bool1 = False

class Item(Entity):
    def __init__(self):
        super().__init__()
        self._name = 'Item'
        self._id = 'Entity'
        #self._bool1 = True
        #self._position1 = None
    def on_hit(self, game1):        
            raise NotImplementedError

class Key(Item):
    def __init__(self):
        super().__init__()
        self._name = 'Key'
        self._id = 'K'
        #self._bool1 = True
        #self._position1 = None
    def on_hit(self, game1):#继承出错
        try:
            if game1.get_player().get_position()==game1.get_positions(KEY)[0]:
                game1.get_player().add_item(str(Key()))
                game1._game_information.pop(game1.get_positions(KEY)[0])

        except:
             pass 
        '''
        if game1._player.get_position()==game1.get_positions(KEY)[0]:
            game1._player.add_item(str(Key()))
            game1._game_information.pop(game1.get_positions(KEY)[0])
            '''
            
class MoveIncrease(Item):
    def __init__(self):
        super().__init__()
        self._name = 'MoveIncrease'
        self._id = 'M'
        #self._bool1 = True
        #self._position1 = None
    def on_hit(self, game1): 
        '''
        if game1.get_positions(MOVE_INCREASE):
            if game1._player.get_position()==game1.get_positions(MOVE_INCREASE)[0]:
              game1._player.change_move_count(5)'''
        try:
            if game1.get_player().get_position()==game1.get_positions(MOVE_INCREASE)[0]:
                game1.get_player().change_move_count(5)
                game1._game_information.pop(game1.get_positions(MOVE_INCREASE)[0])

        except:
            pass#raise NotImplementedError 

class Door(Entity):
    def __init__(self):
        super().__init__()
        self._name = 'Door'
        self._id = 'D'
        self._bool1 = True
        self._position1 = None
    def on_hit(self, game1):
        if game1.get_player().get_position() == game1.get_positions(DOOR)[0]:           
            if not game1.get_player().get_inventory():
                print('You don\'t have the key!')
        #game1.set_win(game1.won(game1.check_game_over()))

class Player(Entity):
    def __init__(self, number1):
        super().__init__()
        self._name = 'Player'
        self._id = 'O'
        self._bool1 = True
        self._number1 = number1
        self._inventory1 = []
        self._position1 = None
    def set_position(self, position1):
        self._position1 = position1
    def get_position(self):
        return self._position1
    def change_move_count(self, change_num):
        self._change_num = change_num
        self._number1 += self._change_num
    def moves_remaining(self):
        return self._number1
    def get_inventory(self):
        return self._inventory1
    def add_item(self,item):
        self._inventory1.append(item)

def main():
    GameApp()
    
if __name__ == "__main__":
    main()