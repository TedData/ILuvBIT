'''
class Car:#定义了一个类
	def start(self):
		print('car启动')
	def information(self):
		print('car_s name is %s,and color is %s'%(self.name,self.color))

c=Car()#构建一个对象
c.name='nissan'#属性
c.color='white'
c.start()
c.information()
'''
#Car是类，c就是对象，name和color是属性
#nissan，white是数据，函数(变量为‘self’)是调用方法
#面向对象特征：继承，封装，多态
'''
class Person:
	def __init__(self):
		self.name='ted'
		self.age=18
		print('对象初始化')

	def work(self):
		print('%%s也不知道写什么%%s')
p1=Person()
p1.work()
print(p1.name)
'''
'''
class Cat(object):
	"""docstring for Cat"""
	def __init__(self, name,age):
		super(Cat, self).__init__()
		self.name = name
		self.age = age
	def __str__(self):
		return ('name is %s,age is %s'%(self.name,self.age))

p1=Cat('lily',18)
print(p1)
'''
import random
class Game:
	def __init__(self,player1,player2):
		self.player1=player1
		self.player2=player2
		print('游戏初始化成功')
	def start_game(self):
		self.player1.cast()
		self.player2.cast()
		#play1_dice_count_list=[self.player1.dices[0].count,self.player1.dices[1].count,self.player1.dices[2].count]
		#play2_dice_count_list=[self.player2.dices[0].count,self.player2.dices[1].count,self.player2.dices[2].count]
		#print('player1%s'%str(play1_dice_count_list))
		#print('player2%s'%str(play2_dice_count_list))
		print(self.player1)
		print(self.player2)
class playeR:
	def __init__(self,name,sex,*dice):
		self.name=name
		self.sex=sex
		self.dices=dice#dice为tuple
	
	def cast (self):
		for dice in self.dices:
			dice.move()
	'''
	def guess (self):
		return(401,10)
	'''
	def __str__(self):
		play_dice_count_list=[self.dices[0].count,self.dices[1].count,self.dices[2].count]
		return '姓名为%s投出的骰子为%s'%(self.name,str(play_dice_count_list))
class Dice:
	def __init__(self):
		self.count=0
	
	def move(self):
		self.count=random.randint(1,6)
d1=Dice()
d2=Dice()
d3=Dice()
d4=Dice()
d5=Dice()
d6=Dice()
p1=playeR('ted','m',d1,d2,d3)
p2=playeR('lily','f',d4,d5,d6)
for i in range(0,5):
	game=Game(p1,p2)
	game.start_game()
	print('='*5)