#练习递归函数
def aa(i):
	s=0
	if i==1:
		s=1
	else :
		s=aa(i-1)*i
	return s
print(aa(5))

def bb(a,b):
	x=''
	if b==0:
		pass
	else:
		x=a[b-1]+bb(a,b-1)
	return x
m='abcdefghigk'
n=len(m)
print(bb(m,n))

def cc(m):
	if m==1:
		i=10
	else:
		i=2+cc(m-1)
	return i
print(cc(5))