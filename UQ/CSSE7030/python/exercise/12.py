#递归函数，斐波那契数列
#first
def a(x):
	if x==1 or x==2:
		return 1
	else:
		return a(x-1)+a(x-2)
m=[]
i=int(input('number:'))
for b in range(1,i+1):
	m.append(a(b))
print(m)
'''
#second
def f(n):
	a,b=1,1
	for j in range(n-1):
		a,b=b,a+b
		return a
print(f(10))
'''