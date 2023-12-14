#无聊的程序
a=int(input('count:'))
n=int(input('number:'))
j=0
o=0
for i in range(n):
	j=10**i*a+j
	o=o+j
	print(j)
print(o)