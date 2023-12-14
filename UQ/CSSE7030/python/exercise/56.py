#两个数之间的素数
lower=int(input('min:'))
upper=int(input('max:'))
for i in range(lower,upper+1):
	if i>1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
			print(i)

