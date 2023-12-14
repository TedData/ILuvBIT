#1!+2!...20!求和
a=[]
for i in range(2,22):
	m=1
	for j in range(1,i):
		m=m*j
	a.append(m)
print(sum(a))


c=0
d=1
for b in range(1,21):
	d*=b
	c+=d
print(c)