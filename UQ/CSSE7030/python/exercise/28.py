'''
1=100
2=50*2=100/2**0  100/2**2
3=25*2=50=100/2**1 100/2**3
4=12.5*2=25=100/2**2
5    =   	100/2**3
6    =      100/2**4

#第m次后反弹高度
m=100/(2**m)
#第n次的距离
n=100/(2**(n-2))
'''

#数学逻辑
n=int(input('No.:'))
for i in range(1,n+1):
	if i==1:
		b=100
	else:
		b+=100/(2**(i-2))
print(b)
print(100/(2**n))
'''
#计算机逻辑
tour=[]
height=[]
hei=100
tim=10
for i in range(1,tim+1):
	if i==1:
		tour.append(hei)
	else:
		tour.append(2*hei)
	hei/=2
	height.append(hei)
print(sum(tour))
print(tour)
print(height[-1])
print(height)
'''