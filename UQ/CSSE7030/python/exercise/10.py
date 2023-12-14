#杨辉三角型
i=int(input('number:'))
for m in range(1,i+1):
	if m==1:
		a=[1]
		print(a)
	elif m==2:
		a=[1,1]
		print(a)
	elif m==3:
		a=[1,2,1]
		print(a)
	elif m>3:
		h=[1]
		b=[1]
		for j in range(0,len(a)-1):
			c=a[j]+a[j+1]
			b.append(c)
		a=b+h
		print(a)
	else:
		pass

