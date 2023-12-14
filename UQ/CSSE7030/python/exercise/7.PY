#学生管理系统
def read():
	global name
	m=open('exercise.data')
	str1=m.read()
	name=eval(str1)
	m.close()
def printMenu():
	print('='*16)
	print('学生信息管理系统')
	print('1:添加学生信息')
	print('2:删除学生信息')
	print('3:修改学生信息')
	print('4:查询学生信息')
	print('5:显示所有学生信息')
	print('0:退出系统')
	print('='*16)
def a1():
	j=input('姓名：')
	m=input('性别(m/f)：')
	n=input('输入手机号：')
	a={}
	a['name']=j
	a['sex']=m
	a['num']=n
	name.append(a)
	write()
def a2():
	i2=int(input('输入删除序号：'))
	del name[i2-1]
	write()
def a3():
	i3=int(input('输入修改序号：'))
	j=input('姓名：')
	m=input('性别(m/f)：')
	n=input('输入手机号：')
	name[i3-1]['name']=j
	name[i3-1]['sex']=m
	name[i3-1]['num']=n
	write()
def a4():
	i4=int(input('请输入想要查询的序号：'))
	for c,d in name[i4-1].items():
		print(str(c)+':',end=(''))
		print(d)

	#print(name[i4-1])
def a5():
	print('='*16)
	print('学生信息')
	print('='*16)

	print('序号	姓名		性别		号码')
	i5=1
	for temp in name:
		print('%s	%s		%s	%s'%(i5,temp['name'],temp['sex'],temp['num']))
		i5+=1
def main():
	while True:
		printMenu()
		i=input('请输入数字：')
		if i=='1':
			a1()
		elif i=='2':
			a2()
		elif i=='3':
			a3()
		elif i=='4':
			a4()		
		elif i=='5':
			a5()
		elif i=='0':
			break
def write():
	f=open('exercise.data','w')
	f.write(str(name))
	f.close()
def No1():
	import os
	List=os.listdir('./')
	if 'exercise.data' not in List:
		f=open('exercise.data','w')
		name=[]
		f.write(str(name))
		f.close()
	else: 
		pass
No1()
read()
main()









'''	
while True:
	print('='*16)
	print('学生信息管理系统')
	print('1:添加学生信息')
	print('2:删除学生信息')
	print('3:修改学生信息')
	print('4:查询学生信息')
	print('5:显示所有学生信息')
	print('0:退出系统')
	print('='*16)
	key=input('请输入数字：')
	if key=='1':
		name1=input('姓名：')
		while True:
			sex10=input('性别(m/f)：')
			sex1=sex10.lower()
			if sex1 == 'm' or sex1 == 'f' :
				break
			else:
				print('请重新输入')
		num1=input('输入手机号：')
		i1=len(name)-1
		name.append({})
		name[i1]['name']=name1
		name[i1]['sex']=sex1
		name[i1]['num']=num1
		for a,b in name[i1].items():
			print(str(a)+':',end=(''))
			print(b)
	elif key=='2':
		while True:
			print('1:name')
			print('2:sex')
			print('3:num')
			key2=input('请选择学生信息:')
			i2=len(name)
			i21=-1
			if key2=='1':
				key21=input('请输入名字：')
			elif key2=='2':
				key21=input('性别：')
			elif key2=='3':
				key21=input('号码：')
			else:
				print('重新输入')
				continue
			while i21<=i2:
				i21+=1
				if key21 in name[i21].values():
					print(name[i21].items())
					j21=input('是否删除(y/n):').lower()
					if j21=='y':
						del name[i21]
						for b in name:
							print(b)
							i2=len(name)
					elif j21=='n':
						continue
					else:
						break
				else:
					print('没有查到，请重新选择')
					break
	elif key=='3':
		while True:
			print('1:name')
			print('2:sex')
			print('3:num')
			key3=input('请选择需要修改的学生信息:')
			i3=len(name)
			i31=-1
			if key3=='1':
				key31=input('请输入名字：')
			elif key3=='2':
				key31=input('性别：')
			elif key3=='3':
				key31=input('号码：')
			else:
				print('重新输入')
				continue
			while i31<=i3:
				i31+=1
				if key31 in name[i31].values():
					print(name[i31].items())
					j31=input('是否修改(y/n):').lower()
					if j31=='y':
						key30=input('修改后为：')
						name[i31][key31]=key30
						for a,b in name[i31].items():
							print(str(a)+':',end=(''))
							print(b)
							i3=len(name)
					elif j31=='n':
						continue
					else:
						break
				else:
					print('没有查到，请重新选择')
					break
	

	elif key=='5':
		#print(name)
		print('='*16)
		print('学生信息')
		print('='*16)

		print('序号	姓名		性别		号码')
		i5=1
		for temp in name:
			print('%s	%s		%s	%s'%(i5,temp['name'],temp['sex'],temp['num']))
			i5+=1

'''
