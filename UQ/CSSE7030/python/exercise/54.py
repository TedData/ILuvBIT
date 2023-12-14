#按逗号分隔list
l=[1,2,3,4,5]
s=str(l)
b=s[1:-1]
a=b.strip().split(',')
print(a)
print(type(a))
print(len(a))
c=str(a)
c=c[1:-1]
print(c)
print(type(c))
print(len(c))

for i in range(0,len(l)):
	l[i]=str(l[i])
print(l)
print(type(l))
print(len(l))
m=str(l)
m=m[1:-1]
print(m)
print(type(m))
print(len(m))