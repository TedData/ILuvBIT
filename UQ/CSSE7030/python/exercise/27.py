
class User:
	def __init__(self):
		print("初始化")
	def __del__(self):
		print('=======del====')
	def __str__(self):
		return '==str=='
class Name:
	def __init__(self):
		print("初始化123")
	def __del__(self):
		print('=======del123====')

n=Name()		
u1=User()

u2=u1
print(u2)
del u1
print('++++')
del u2
print('****')
for i in range(6):
	print(i)
print('-------')
#继承
class Dog:
	def __init__(self):
		print('flaw')
		self.age='5'
	def eat(self):
		print('like meat')
	def sleep(self):
		print('image')

class potato(Dog):
	
	def __init__(self):
		
		print('dict')
		self.age='10'
		super().__init__()
	
	def sleep (self):
		super().sleep()
		print("imagine")

class ZangAo(Dog):
	def fight(self):
		print('potable')

a=potato()
#print(a.sleep())
a.eat()
a.sleep()
print(a.age)
a1=ZangAo()
a1.eat()
