#异常的处理 try:... except:...finally:
def Try():
	try:
		main()
	#except Exception:#所有的异常
		#print('hello, world')
		#print(ex)
	except NameError as ex:
		print('名字没有被定义')
		print(ex)
	except ZeroDivisionError as ex:
		print('除数不能为0')
		print(ex)
	except AttributeError as ex:
		print('语言程序写错了')
		print(ex)
	except SyntaxError as ex:
		print('语法错误')
		print(ex)
	except TypeError as ex:
		print('格式错误')
		print(ex)
	finally:
		print('hello, world')
def main():
	class PassWord(Exception):#(Exception):
		def __init__(self,pw,min):
			self.pw=pw
			self.min=min
		def __str__(self):
			return "%s的密码错误，密码最小长度为%s"%(self.pw,self.min)
	def abc(username,password):
		if len(password)<6:
			#print(PassWord(password,6))
			raise PassWord(password,6)
		else:
			print('用户名为%s,密码为%s'%(username,password))
	#abc('ted','142342323')
	
	try:
		abc('ted','123')
	except Exception:
		print('捕获异常')




Try()