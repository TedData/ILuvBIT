#猜拳游戏
import random
while True:
	print('游戏规则：\n1:拳头\n2:剪刀\n3:布')
	b=str(random.randint(1,3))
	print('computer--->'+str(b))
	a=input('请a号选择你的野球拳：')
	if (a=='1' and b=='2') or (a=='2' and b=='3') or (a=='3' and b=='1'):
		print('player win')
		break
	elif (b=='1' and a=='2') or (b=='2' and a=='3') or (b=='3' and a=='1'):
		print('computer win')
	elif a==b:
		print('play game again')
	else:
		print('请好好玩游戏')