#正三角形
num=int(input('Please write a number:'))
i=0
m=1
while i<num:
	i+=1
	j=0
	b=0
	print(' '*2*(num-i),end=(''))
	while j<i:
		j+=1
		print(j,end=(' '))
	while b<i-1:
		b+=1
		print((m-b),end=(' '))
	print('')
	m+=1
