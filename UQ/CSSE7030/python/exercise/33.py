#求前20位和2/1+3/2+5/3+8/5...
'''
i=2
j=1
m=0
for n in range(1,21):
	m=i/j+m
	i,j=(i+j),i
print(m)
'''
a=2
b=1
l=[]
l.append(a/b)
for n in range(1,20):
	b,a=a,a+b
	l.append(a/b)
print(sum(l))