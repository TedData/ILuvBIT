#单例模式
class aa(object):
	__bb=None
	def __init__(self,name):
		self.name=name
	'''
	@classmethod
	def cc(cls,name):
		if not cls.__bb:
		cls.__bb=aa(name)
		return cls.__bb
	'''

	def __new__(cls,name):
		if not cls.__bb:
			cls.__bb=object.__new__(cls)
		return cls.__bb


a1=aa('ted')
a2=aa('kelvin')
a3=aa('lily')
'''
a1=aa.cc('lily')
a2=aa.cc('hunter')
'''
print(a1.name)
print(a2.name)
print(a3.name)
print(a1==a2)

