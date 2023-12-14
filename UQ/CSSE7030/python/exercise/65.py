#函数内argument与外部不通用	
#class可调用外部函数，也可用内部函数
class func (object):
	num=1
	def func_num(self):
		self.num+=10
		print('func.func_num num is',self.num)
		print('outside_num is',num)
num = 2
def autofunc():
	num = 1
	print('autofunc num is ',num)
	num+=1
x=func()
for i in range(3):
	print('num is',num)
	num+=1
	autofunc()
	func.num=100
	x.func_num()