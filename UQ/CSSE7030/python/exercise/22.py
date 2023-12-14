#水仙花数
#first	
'''
for a in range(1,10):
	for b in range(10):
		for c in range(10):
			if (a*100+b*10+c)==(a*a*a+b*b*b+c*c*c):
				print(a,b,c)
'''
#second
for n in range(100,1000):
	i=n//100
	j=n//10%10
	k=n%10
	if n==(i**3+j**3+k**3):
		print(n)
