#简单工厂模式
class aa(object):
	def __init__(self,name):
		self.name=name
	def work(self,way):
		print(self.name+'开始工作')
		'''
		bb=cc('没钱自己干')
		bb.cut_tree()'''
		bb=Factory.abc(way)
		bb.cut_tree()
class bb(object):
	def __init__(self,name):
		self.name=name
	def cut_tree(self):
		print('%s开始砍树'%self.name)
class cc(bb):
	def cut_tree(self):
		print('手动砍树')
class dd(bb):
	def cut_tree(self):
		print('自动砍树')
#简单工厂模式
class Factory(object):
	#@staticmethod#静态传递参
	def abc(type):
		if type=='没钱':
			return cc('')
		elif type=='有钱':
			return dd('')
		else:
			print('滚')
			return bb('')
#class Factory(object):
#	def abc(self):
a=aa('ted')
a.work('有钱')
