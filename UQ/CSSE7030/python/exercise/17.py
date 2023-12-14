#批量复制文件
import os
a=os.listdir('../123')
print(a)
b=[]
for i in range(0,len(a)):
	b.append('../123/[copy]'+a[i])
	a[i]='../123/'+a[i]
	R=open(a[i],'r')
	W=open(b[i],'w')
	r=R.read()
	W.write(r)
	R.close()
	W.close()
	os.remove(a[i])
a=os.listdir('../123')
print(a)	