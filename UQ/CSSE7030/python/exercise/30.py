class User(object):
	name="ted"  #公共的类属性，修改方式只能是，User.name=***
	__password='123456'
	def __init__(self):
		self.sex='F'
		self.name='kelive'
		#self.password='qwerasdf'
		#print(self.__password)
class a(User):
	pass
u1=User()
print(u1.name)
User.name='lily'
print(a.name)
#User是类，u1是对象
#类属性的访问可以通过类名，也可以通过对象
#修改类属性只能通过类名修改。