import sys
print(sys.argv)
a=[]
for i in range(10,0,-1):
	a.append(i)
print(a)
b=[ 1 for j in range(1,11)]
print(b)
c=[j**2 for j in range(1,11) ]
print(c)
d=[{x:y} for x in range(0,3) for y in range (4,6)]
print(d)
e=[m for m in range(1,101,2) if not(m//2==0)]
print(e)
f=[[n-2,n-1,n] for n in range(1,101) if n%3==0]
print(f)
