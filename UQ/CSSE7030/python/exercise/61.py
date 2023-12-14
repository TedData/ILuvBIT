#插入两个个数，按原有顺序排列
if __name__=='__main__':
	m=[2,9,4,7,6,5,8,3]
	#插入list
	b,c=input('enter two numbers: ').split(',')
	b=int(b)
	c=int(c)
	m.append(b)
	m.append(c)
	for i in range(len(m)-1):
		if i%2==0:
			for j in range(i,len(m)):
				if j%2==0 and m[i]>m[j]:
					m[i],m[j]=m[j],m[i]
		else :
			for j in range(i,len(m)):
				if j%2==1 and m[i]<m[j]:
					m[i],m[j]=m[j],m[i]
print(m)

