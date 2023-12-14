#矩形主对角线元素之和

if __name__=='__main__':
	def commond(x,y):
		l=[]
		for i in range(y):
			l.append([])
			for j in range(x):
				input_num=int(input('enter a number: '))
				l[i].append(input_num)

		for var in l:
			print(var,'\n')
		return l

	x=commond(4,4)

	sum=0
	for i in range(len(x)):
		sum+=x[i][i]
	print(sum)









