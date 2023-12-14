#一组数可拆分成str
a=int(input('write a number'))
a=str(a)
b=len(a)
for j in a:
	print(j)
s=a[::-1]
print(s)
print('*'*10)


m=0
for i in range(10000,100000):
	i=str(i)
	if i[0]==i[-1] and i[1]==i[-2]:
		print(i)
		m+=1
print(m)

