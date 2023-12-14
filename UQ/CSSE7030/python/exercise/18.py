#目录文件下，是否有查找的内容
b=input('输入查找的内容：')
import os
a=os.listdir('../123')
m=0
for i in range(0,len(a)):
	a[i]='../123/'+a[i]
	R=open(a[i])
	while True:
		l=R.readline()
		if l=="":
			break
		else:
			if b in l:
				print(a[i])
				m=1
				break
	R.close()
if m!=1:
	print('False')
else:
	print('True')
	






#print(a)



