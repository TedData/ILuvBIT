#导入模块，当前目录下可直接使用
'''
import 41 
i=''
print(41.bbb(i))


from random import randint
print(randint(0,2))
'''
#创建模块，文件名不能为数字
def bbb(str):
	if not str:
		return True
	elif str.strip()=='':
		return True
	else:
		return False

#测试模块，主动调用执行，模块调用不执行
if __name__=='__main__':
	print(bbb(''))
