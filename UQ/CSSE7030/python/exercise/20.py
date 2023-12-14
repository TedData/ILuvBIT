#汉诺塔
aa=[]
bb=[]
cc=[]
mm=[]
nuM=int(input('how hard?'))
for temP in range(1,nuM+1):
	mm.append(temP)
mm=mm[::-1]
aa=mm
mm=tuple(mm)
def Print():
	print('a:',aa)
	print('b:',bb)
	print('c:',cc)
def Move():
	jj.append(ii[-1])
	del ii[-1]
def s(x):
	if x=='a':
		return aa
	elif x=='b':
		return bb
	elif x=='c':
		return cc
	else:
		print('wrong')
		Print()
		return ['wrong']
while True:
	Print()
	if cc==list(mm):
		print('good')
		break
	else:
		while True:
			i,j=input('a,b,c:').split()
			ii=s(i)
			jj=s(j)
			if jj!=['wrong'] and ii!=['wrong']:
				break
		if len(ii)==0:
			print('wrong')
		elif len(ii)>0:
			if len(jj)==0:
				Move()
			elif ii[-1]<jj[-1]:
				Move()
			else:
				print('wrong')
		else:
			print('wrong')