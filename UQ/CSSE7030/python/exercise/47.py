import pygame, sys,time,random
from pygame.locals import *
pygame.init()#pygame模块初始化，加载系统的资源

class Main(object):#坦克大战的主窗口
	width=1800#设置屏幕的宽度
	height=1200#设置屏幕的高度
	my_tank=None#建立我方坦克	
	my_tank_missile_list=pygame.sprite.Group()#我方炮弹组群
	ene_list=pygame.sprite.Group()#敌方坦克的组群
	ene_missile_list=pygame.sprite.Group()#敌方炮弹碰撞检测
	explode_list=[]#碰撞列表
	wall=None#初始化墙
	def start_game(self):
		#创建一个屏幕
		#屏幕的宽高为600*500
		#窗口可变为(0(不可调节),pygame.locals.RESIZABLE(可调节),pygame.FULLSCREEM全屏)
		#颜色为32位
		screen=pygame.display.set_mode((Main.width,Main.height),0,32)
		#给窗口设置标题
		pygame.display.set_caption('坦克大战')
		Main.wall=Wall(screen)#创建一堵墙
		Main.my_tank=My_tank(screen)#创建我方坦克
		#创建敌方坦克
		for i in range(0,6):#初始化敌方坦克数量为6
			Main.ene_list.add(Ene_tank(screen))#把敌方坦克放到组里面
		x=0
		while True:
			time.sleep(0.06)#刷新时间
			pygame.display.update()#显示重置，要放在第一位
			#设置屏幕的背景色
			#color(RGB)(red,green,blue)(0,100,255)
			#填充颜色大小None
			screen.fill((255,255,255))#白色，(0,0,0)为黑色
			for i,text in enumerate(self.write_text(),0):
				#显示图案（文字内容，位置）
				screen.blit(text,(0,5+(90*i)))
			#根据获取的事件来处理，操作坦克
			self.get_event(Main.my_tank,screen)
			if Main.my_tank:#必须强调我方坦克类存在
				Main.my_tank.hit_enemy_missile()#我方坦克与敌方炮弹进行碰撞检测
			if Main.my_tank and Main.my_tank.live:
				Main.my_tank.display()#在屏幕上显示坦克图像
				Main.my_tank.move()#在屏幕上移动我方坦克
			else:
				Main.my_tank=None#我方被消灭
			#显示我方炮弹
			for m in Main.my_tank_missile_list:
				if m.live:
					m.display()#显示我方炮弹
					m.hit_tank()#炮弹打中敌方坦克
					m.move()#移动炮弹
				else:
					Main.my_tank_missile_list.remove(m)#移除炮弹
			#显示和随机移动所有的敌方坦克
			for ene in Main.ene_list:
				ene.display()#在屏幕上显示敌方坦克
				ene.random_move()#随机移动
				ene.random_fire()#随机开火
			if x==50:#一段时间后添加敌方坦克
				Main.ene_list.add(Ene_tank(screen))
				x=1
			x+=1
			#显示所有的敌方炮弹
			for m in Main.ene_missile_list:
				if m.live:
					m.display()#显示敌方炮弹
					m.move()#移动炮弹
				else:
					Main.ene_missile_list.remove(m)#移除炮弹
			for explode in Main.explode_list:
				explode.display()#碰撞后显示爆炸图片
			#显示游戏中的墙，并且对墙和其他对象进行碰撞检测
			Main.wall.display()
			Main.wall.hit_other()
	#在屏幕上显示文字
	def write_text(self):
		#设置字体格式跟大小
		front=pygame.font.Font(None,100)
		#设置显示内容，锯齿，颜色
		text_sf1=front.render('Tank:%d'%len(Main.ene_list),True,(255,0,0))
		text_sf2=front.render('Missile:%d'%len(Main.my_tank_missile_list),True,(255,0,0))
		return text_sf1, text_sf2
	def get_event(self,my_tank,screen):#获取鼠标键盘信息
		for event in pygame.event.get():
			#点击❌或点击鼠标退出
			if event.type in (QUIT,MOUSEBUTTONUP):
				self.stop_game()
			elif event.type==KEYDOWN and (not my_tank) and event.key==K_n:
				Main.my_tank=My_tank(screen)#重启坦克
			#获取键盘信息
			elif event.type == KEYDOWN and my_tank:#我方坦克必须存活
				if event.key==K_LEFT:
					my_tank.direction='L'
					my_tank.run=True
				elif event.key==K_RIGHT:
					my_tank.direction='R'
					my_tank.run=True
				elif event.key==K_UP:
					my_tank.direction='U'
					my_tank.run=True
				elif event.key==K_DOWN:
					my_tank.direction='D'
					my_tank.run=True
				elif event.key==K_SPACE:
					m=my_tank.fire()
					m.good=True#我方炮弹
					Main.my_tank_missile_list.add(m)#添加炮弹
				elif event.key==K_ESCAPE:
					self.stop_game()
			#按键不动持续移动
			if event.type==KEYUP and my_tank:
				if event.key in (K_DOWN,K_LEFT,K_RIGHT,K_UP):
				 	my_tank.run=False
	def stop_game(self):#关闭游戏
		sys.exit()
#坦克大战游戏中所有的父类
class BaseItem(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		#所有对象公共的属性
		self.screen=screen#坦克显示在当前屏幕窗口
	#把坦克对应的图片显示在游戏窗口上
	def display(self):
		if self.live:#如果坦克存活
			self.image=self.images[self.direction]#根据方向选择图片
			#显示屏幕的内容，位置
			self.screen.blit(self.image,self.rect)
class Tank(BaseItem):
	#定义类属性，所有坦克宽高都一样
	width=100
	height=100
	def __init__(self,screen):
		super().__init__(screen)
		self.direction='U'#坦克方向，默认方向为上
		self.images={}#坦克的所有图片，key:方向，value:图片
		#加载图片
		self.images['L']=pygame.image.load('Images/air_left.gif')
		self.images['U']=pygame.image.load('Images/air_up.gif')
		self.images['R']=pygame.image.load('Images/air_right.gif')
		self.images['D']=pygame.image.load('Images/air_down.gif')
		#坦克的图片由方向决定
		self.image=self.images[self.direction]
		#坦克图标的边界
		self.rect=self.image.get_rect()#获取边界
		self.live=True#判断坦克是否存活
		self.speed=25#坦克移动的速度
		self.run=False#坦克是否移动
		self.oldtop=self.rect.top
		self.oldleft=self.rect.left
	def stay(self):#发生碰撞后退回原位置
		self.rect.top=self.oldtop
		self.rect.left=self.oldleft
	def move(self):
		if self.run:#如果坦克不是停止状态
			self.oldleft=self.rect.left
			self.oldtop=self.rect.top
			if self.direction=='L':
				if self.rect.left>0:
					self.rect.left-=self.speed
				else:
					self.rect.left=0	
			elif self.direction=='R':
				if self.rect.right<Main.width:
					self.rect.right+=self.speed
				else:
					self.rect.right=Main.width
			elif self.direction=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.rect.top=0
			elif self.direction=='D':
				if self.rect.bottom<Main.height:
					self.rect.bottom+=self.speed
				else:
					self.rect.bottom=Main.height
	def fire(self):
		m=Missile(self.screen,self)
		return m
class My_tank(Tank):
	def __init__(self,screen):
		super().__init__(screen)
		#我方坦克初始位置
		self.rect.left=600
		self.rect.top=800
		self.live=True
	def hit_enemy_missile(self):#我方坦克与敌方炮弹进行碰撞
		#我方坦克与敌方炮弹进行碰撞后，炮弹以列表的形式写入
		hit_list=pygame.sprite.spritecollide(self,Main.ene_missile_list,False)#用我方坦克与敌方炮弹进行碰撞
		for m in hit_list:#我方坦克中弹了
			m.live=False#移除坦克
			Main.ene_missile_list.remove(m)#移除敌方炮弹
			self.live=False
			explode=Explode(self.screen,self.rect)#定义爆炸类
			Main.explode_list.append(explode)#发生爆炸图片

class Ene_tank(Tank):#敌方坦克
	def __init__(self,screen):
		super().__init__(screen)
		#坦克按照某个方向连续移动8次
		self.Times=8
		self.step=self.Times
		self.get_random_direction()#初始方向
		self.speed=10#重新设定速度
		self.images={}#坦克的所有图片，key:方向，value:图片
		#加载图片
		self.images['L']=pygame.image.load('Images/tank1_left.png')
		self.images['U']=pygame.image.load('Images/tank1_up.png')
		self.images['R']=pygame.image.load('Images/tank1_right.png')
		self.images['D']=pygame.image.load('Images/tank1_down.png')
		#坦克的图片由方向决定
		self.image=self.images[self.direction]
		#坦克图标的边界
		self.rect=self.image.get_rect()#获取边界
		#敌方坦克初始位置
		self.rect.left=random.randint(5,12)*100
		self.rect.top=500
	def get_random_direction(self):#随机方向
		r=random.randint(0,4)
		if r==1:
			self.direction='L'
		elif r==2:
			self.direction='R'
		elif r==3:
			self.direction='U'
		elif r==4:
			self.direction='D'
		self.run=True
		if r==0:
			self.run=False
	#敌方坦克，按照一个随机方向，连续移动，然后才能改变
	def random_move(self):
		if self.live:
			if self.step==0:
				self.get_random_direction()
				self.step=self.Times
			else:
				self.move()
				self.step-=1
	def random_fire(self):#随机开火
		r=random.randint(0,5000)
		if r>4900:
			m=self.fire()
			Main.ene_missile_list.add(m)#把子弹添加到敌方子弹列表里
		else:#貌似没什么用
			return
class Missile(BaseItem):
	width=44
	height=44
	def __init__(self,screen,tank):
		super().__init__(screen)
		self.live=True#判断炮弹是否存在
		self.tank=tank
		self.direction=tank.direction#炮弹的方向等于坦克方向
		self.speed=30#设定子弹速度
		self.images={}#子弹图片，key:方向，value:图片
		#加载图片
		self.images['L']=pygame.image.load('Images/missile_L.jpg')
		self.images['U']=pygame.image.load('Images/missile_U.jpg')
		self.images['R']=pygame.image.load('Images/missile_R.jpg')
		self.images['D']=pygame.image.load('Images/missile_D.jpg')
		#子弹的图片方向
		self.image=self.images[self.direction]
		#坦克图标的边界
		self.rect=self.image.get_rect()#获取边界
		#炮弹初始位置
		self.rect.left=tank.rect.left+(tank.width-self.width)/2
		self.rect.top=tank.rect.top+(tank.height-self.height) /2
		self.good=False
	def move(self):
		if self.live:#如果炮弹存在
			if self.direction=='L':
				if self.rect.left>0:
					self.rect.left-=self.speed
				else:
					self.live=False	
			elif self.direction=='R':
				if self.rect.right<Main.width:
					self.rect.right+=self.speed
				else:
					self.live=False	
			elif self.direction=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.live=False	
			elif self.direction=='D':
				if self.rect.bottom<Main.height:
					self.rect.bottom+=self.speed
				else:
					self.live=False	
	#我方炮弹击中敌方坦克
	def hit_tank(self):
		if self.good:#如果炮弹是我方炮弹
			hit_list=pygame.sprite.spritecollide(self,Main.ene_list,False)#列表
			for e in hit_list:
				e.live=False
				Main.ene_list.remove(e)
				self.live=False
				explode=Explode(self.screen,e.rect)#产生一个爆炸对象
				Main.explode_list.append(explode)
#爆炸类
class Explode(BaseItem):
	def __init__(self,screen,rect):
		super().__init__(screen)
		self.live=True
		self.images=[pygame.image.load('images/1.jpg'),pygame.image.load('images/2.jpg'),pygame.image.load('images/3.jpg'),pygame.image.load('images/4.jpg'),pygame.image.load('images/5.jpg'),pygame.image.load('images/6.jpg'),pygame.image.load('images/7.jpg'),pygame.image.load('images/8.jpg'),pygame.image.load('images/9.jpg'),pygame.image.load('images/10.jpg')]
		self.step=0
		self.rect=rect#爆炸的位置和发生爆炸前，炮弹碰到的坦克位置一样，在构建爆炸的时候吧坦克的rect传递进来
	#display方法在整个游戏运行过程中，循环调用，每隔0.05秒调用一次
	def display(self):#显示爆炸动画
		if self.live:
			if self.step==len(self.images):#最后一张图片已经显示了
				self.live=False
			else:
				self.image=self.images[self.step]
				self.screen.blit(self.image,self.rect)
				self.step+=1 
#游戏中的障碍物
class Wall(BaseItem):
	def __init__(self,screen):
		super().__init__(screen)
		#画出障碍物的(left,top,width,height)
		self.rect=Rect(165,800,300,120)
		self.color=(130,100,120)
	def display(self):
		self.screen.fill(self.color,self.rect)
	#针对墙和其他坦克或者炮弹的碰撞检测
	def hit_other(self):
		if Main.my_tank:#我方坦克与墙面发生碰撞
			#如果墙与我方坦克(type:class)放生碰撞返回值为True
			is_hit=pygame.sprite.collide_rect(self,Main.my_tank)
			if is_hit:
				Main.my_tank.run=False#停止运动
				Main.my_tank.stay()#返回原来位置，否则会一点一点移动
		if len(Main.ene_list)!=0:#敌方坦克存在
			#墙面与敌方坦克(list)碰撞返回敌方坦克为list
			hit_list=pygame.sprite.spritecollide(self,Main.ene_list,False)
			for e in hit_list:
				e.run=False#停止运动
				e.stay()#返回原来位置，否则会一点一点移动
		if len(Main.my_tank_missile_list)!=0:#我方炮弹存在
			#墙面与我方炮弹(list)碰撞返回我方炮弹为list
			is_missile_hit=pygame.sprite.spritecollide(self,Main.my_tank_missile_list,False)
			for s in is_missile_hit:
				Main.my_tank_missile_list.remove(s)#移除炮弹
		if len(Main.ene_missile_list)!=0:#敌方炮弹存在
			#墙面与敌方炮弹(list)碰撞返回敌方炮弹为list
			is_ene_missile_hit=pygame.sprite.spritecollide(self,Main.ene_missile_list,False)
			for u in is_ene_missile_hit:
				Main.ene_missile_list.remove(u)#移除炮弹
if __name__ == '__main__':
	game=Main()
	game.start_game()

