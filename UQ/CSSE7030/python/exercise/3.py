#九九乘法表
a=0
while a<9:
	a+=1
	j=0
	while j<a:
		j+=1
		c=a*j
		print('%s*%s=%-2s'%(j,a,c),end=('	'))
	print('')

