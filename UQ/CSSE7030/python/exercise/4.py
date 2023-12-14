#增改姓名
name=['kelvin','ted','ather','lily','hunter']
while True:
	print('='*19)
	print('welcome to system')
	print('1:add a new name')
	print('2:del a name')
	print('3:change a name')
	print('4:find a name')
	print('5:all names')
	print('0:exit')
	print('='*19)
	a=input('what do you need?')
	if a=='1':
		b1=input('add a new name:')
		if b1 not in name:
			name.append(b1)
			print('done')
			print(name)
		else:
			print('we already have.')
	elif a=='2':
		b2=input('write a name:')
		if b2 in name:
			name.remove(b2)
			print(name)
		else:
			print('the name is not in our list.')
	elif a=='3':
		while True :
			b3=input('write before name:')
			if b3 in name:
				b31=name.index(b3)
				b32=input('new name:')
				name[b31]=b32
				#name.replace(b3,b32)
				print(name)
				break
			if b3 not in name:
				print('please chick the name')
				print('x:bask')
				if b3=='x':
					break 
	elif a=='4':
		b4=input('which name do you need find?')
		if b4 in name:
			print('yes')
		else:
			print('no')
	elif a=='5':
		for b5 in name:
			print(b5)
	elif a=='0':
		break
	else:
		print('gogogo')


