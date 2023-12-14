#list逆序排列
if __name__=='__main__':
	a=[1,4,2,'viola','ted']
	b=[]
	for i in range(len(a)):
		b.append(a[-1-i])
	print(b)

