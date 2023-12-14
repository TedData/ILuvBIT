class aaa(object):
	z=60
	c=35
	def __init__(self):
		self.z=aaa.z+5
		self.x=60
	def bbb(self):
		self.y=50

	def __new__(cls):
		c=40
		return object.__new__(cls)
class bbb(object):
	def __init__(self,aaa):
		self.aaa=aaa
	def printd(self):
		print(self.aaa.x)
a=aaa()
print(a.z)
b=bbb(a)
b.printd()



import random

x=random.randint(1,6)
print(x)
print(type(x))
r=1
while x-r:
	print('hello')
	x-=1



