#取质数
n=0
for i in range(100,201):
	m=0
	for j in range(2,i):
		if i%j==0:
			m+=1
			break
	if m==0:
		print(i)
		n+=1
print(n)