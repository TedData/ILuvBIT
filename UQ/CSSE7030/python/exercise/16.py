#输入五个整数，从小到大排列输出
x,y,z,m,n=input('three numbers:').split()#以空格为分节符，分别定义三个字符
x=int(x)
y=int(y)
z=int(z)
m=int(m)
n=int(n)
a=[x,y,z,m,n]
#frist
a.sort()
#second
'''
for j in range(0,len(a)-1):
	for i in range(j,len(a)):
		if a[j]>a[i]:
			a[j],a[i]=a[i],a[j] 
'''
print(a)



