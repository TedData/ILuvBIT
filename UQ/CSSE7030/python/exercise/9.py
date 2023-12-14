#创建拥有存储功能的list
def Try(): #判断是否存在文件，没有建立文件
	try:
		try_open=open('file.data')
		try_open.close()
	except:
		found=open('file.data','w')
		found.write(str([]))
		found.close()
def Read():	#读取文件的内容，内有两个A 
	global A
	open_file=open('file.data')
	change_type=eval(open_file.read())
	A+=change_type
	open_file.close() 
def add_del(): #修改信息
	j=input('choice：\n1:add\n2:del\n')
	if j=='1':
		i=input('add:')
		A.append(i)
	elif j=='2':
		i=input('del:')
		if i in A:
			A.remove(i)
		else:
			print('wrong')
	else:
		pass 
def Write(): #写入文档，内有两个A
	write_content=open('file.data','w')
	write_content.write(str(A))
	write_content.close() 
	print(A)
A=[] #先定义全局变量
Try()
Read()
add_del()
Write()


