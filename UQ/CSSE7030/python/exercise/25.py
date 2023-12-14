#1.一切皆对象
#2.知道每一个对象的职责
class User:

	def __init__(self,username,password):
		self.username=username
		if len(password)>=6:
			self.__password=password
		else:
			print('长度不够')

	def __str__(self):
		self.__abc()
		return '用户名为%s,密码为%s'%(self.username,self.__password)
	def Set(self,pw):
		if len(pw)>=6:
			self.password=pw
		else:
			print('长度不够')
	def __abc(self):
		print(self.__password)

u=User('kuraby','123123')
#u.username='kuraby'
#u.Set('123trfdas')
u.__password='123'
print(u)
#__+文件名为私有属性，只能class内部调用，调用方式self.__+文件名()
