#一个数恰好等于它的因子之和
for n in range(1,1001):
	b=0
	a=0
	while a<n-1:
		a+=1	
		if n%a==0:
			b=b+a
	if b==n:
		print(n)
		for i in range(1,n):
			if n%i==0:
				print(i,end=(" "))
		print("")
			


