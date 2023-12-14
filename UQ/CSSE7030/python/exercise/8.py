#倒正三角
j=int(input('number:'))
m=j
while j>0:
	print (" "*(m-j),end=(''))
	for i in range(j):
		print("* ",end=(''))
	print('')
	j-=1