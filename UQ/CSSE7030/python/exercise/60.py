import random
if __name__=='__main__':
	for i in range(10):
		r=random.randint(0,5)
		m=['+','-','*','//','**','%']
		a=random.randint(10,99)
		b=random.randint(10,99)
		if r==4:
			a=random.randint(0,3)
			b=random.randint(0,3)
			s=a**b
		elif r==0:
			s=a+b
		elif r==1:
			s=a-b
		elif r==2:
			s=a*b
		elif r==3:
			s=a//b
		else:
			s=a%b
		result='result:'+str(a)+m[r]+str(b)+'='
		gruess=int(input(result))
		if s==gruess:
			print('correct')
		else:
			print('sorry',s,'=',a,m[r],b,sep='')