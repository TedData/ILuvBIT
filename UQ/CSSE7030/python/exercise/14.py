#提成
i=int(input('当月利润：'))
'''
if i<=100000:
	m=i*0.1
elif 100000<i<=200000:
	m=100000*0.1+(i-100000)*0.075
elif 200000<i<=400000:
	m=100000*0.1+200000*0.075+(i-200000)*0.05
elif 400000<i<=600000:
	m=100000*0.1+200000*0.075+400000*0.05+(i-400000)*0.03
elif 600000<i<=1000000:
	m=100000*0.1+200000*0.075+400000*0.05+600000*0.03+(i-600000)*0.015
else:
	m=100000*0.1+200000*0.075+400000*0.05+600000*0.03+1000000*0.015+(i-1000000)*0.01
print(m)
'''
a=[1000000,600000,400000,200000,100000,0]
b=[0.01,0.015,0.03,0.05,0.075,0.1]
r=0
for j in range(0,len(a)):
	if i>a[j]:
		r=(i-a[j])*b[j]+r
		i=a[j]

print(r)







