'''
__init__
__str__
__del__
__new__'''

class aa(object):
	name='kelvin'
	def __str__(self):
		return 'nihao %s'%aa.name
	def __init__(self):
		self.name='ted'
		self.password="123456"
		print('name is %s, password is %s'%(self.name,self.password))

	def __del__(self):
		print('def'*5)
	#new方法是当对象构建时由解释器自动回调的方法，该方法必须返回当前类的对象
	def __new__(cls):
		print(aa.name)
		aa.name='lily'
		return object.__new__(cls)
a=aa()

print(a)