#四个数取三个
#frist
num=[1,2,3,4]
def A(aa,x):#bb为删除list(aa)里x元素，但不更改aa里的内容
	aa=tuple(aa)
	bb=list(aa)
	bb.remove(x)
	return bb
q=0
for n in num:
	a=A(num,n)
	for m in a:
		b=A(a,m) 
		for i in b:
			print(n,m,i)
			q+=1
print(q)

#second
'''
q=0
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if(i!=k) and (i!=j) and (j!=k):
				print(i,j,k)
				q+=1
print(q)
'''

