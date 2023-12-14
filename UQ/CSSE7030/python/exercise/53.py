#赌博小程序
import random
a=[]
my_score=0
i=1

while True:
	print('='*10)
	if len(a)>6:
		a.remove(a[0])
	print(a)
	r=random.randint(0,37)
	a.append(r)
	print('剩余金额：%s'%my_score)
	if i==1:
		print('1:0'+'\n2:偶数'+'\n3:奇数'+'\n4:放弃'+'\n0:退出')
		s=int(input('选择：'))
		if s in (1,2,3):
			pass 
		elif s==0:
			break
		else:
			continue
		d=int(input('下注：'))
	else:
		print('重复次数%s'%i+'\n下注金额:%s'%(d*(2**(i-1))))
		print('一共开销:%s'%(d*(2**i)-d))
	z=x=10
	if r==0 or r==37:
		z=1
	elif r%2==0:
		x=2
	elif r%2==1:
		x=3
	if s==z:
		my_score+=(d)*(2**(i-1))
		print('you win')
		i=1
	elif s==x:
		my_score+=d*(2**(i-1))
		print('you win')
		i=1
	else:
		my_score-=d*(2**(i-1))
		print('you lost')
		i+=1