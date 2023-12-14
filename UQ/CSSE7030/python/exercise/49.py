
import pygame,sys,time
from random import randint
from pygame.locals import *
'''坦克大战的主窗口'''
class TankMain(object):
	width=600
	height=500
	my_tank_missile_list=[]
	my_tank=None
	#enemy_list=[]
	wall=None
	enemy_list=pygame.sprite.Group()#敌方坦克的组群
	explode_list=[]
	enemy_missile_list=pygame.sprite.Group()#碰撞检测
	#开始游戏的方法
	def startGame(self):
		pygame.init()#pygame模块初始，加载系统的资源
		#创建一个屏幕，屏幕的大小(宽，高)，窗口的特性，
		screen=pygame.display.set_mode((TankMain.width,TankMain.height),0,32)
		#给窗口设置一个标题
		pygame.display.set_caption('坦克大战')
		
		#创建一堵墙
		TankMain.wall=Wall(screen,65,160,30,120)

		TankMain.my_tank=My_Tank(screen)#创建一个我方坦克，坦克显示在屏幕的中下部位置
		if len(TankMain.enemy_list)==0:
			for i in range(1,6):#游戏开始时候初始化5个敌方坦克
				TankMain.enemy_list.add(Enemy_Tank(screen))#把敌方坦克放到组里面		
		while True:
			if len(TankMain.enemy_list)<5:
				TankMain.enemy_list.add(Enemy_Tank(screen))
			#color RGB(0,0,0)，(255,255,255)
			#设置屏幕的背景色为黑色
			screen.fill((0,0,0))
			#瞎写的
			pygame.draw.rect(screen,(0,255,0),Rect(400,30,100,30),2)

			#显示左上角的文字
			for i,text in enumerate(self.write_text(),0):
				screen.blit(text,(0,5+(15*i)))
			#显示游戏中的墙，并且对墙和其他对象进行碰撞检测
			TankMain.wall.display()
			TankMain.wall.hit_other()

			self.get_event(TankMain.my_tank,screen)#获取事件，根据获取的事件处理
			if TankMain.my_tank:
				TankMain.my_tank.hit_enemy_missile()#我方坦克与敌方炮弹进行碰撞检测
			if TankMain.my_tank and TankMain.my_tank.live:
				TankMain.my_tank.display()#在屏幕上显示我方坦克
				TankMain.my_tank.move()#在屏幕上移动我方坦克
			else:
				TankMain.my_tank=None
				#sys.exit()
			#显示和随机移动所有的敌方坦克
			for enemy in TankMain.enemy_list:
				enemy.display()
				enemy.random_move()
				enemy.random_fire()

			#显示所有的我方炮弹
			for m in TankMain.my_tank_missile_list:
				if m.live:
					m.display()
					m.hit_tank()#炮弹打中敌方坦克
					m.move()
				else:
					TankMain.my_tank_missile_list.remove(m)
			#显示所有的敌方炮弹
			for m in TankMain.enemy_missile_list:
				if m.live:
					m.display()
					m.move()
				else:
					TankMain.enemy_missile_list.remove(m)
		
			for explode in TankMain.explode_list:#碰撞之后显示图片
				explode.display()

			#屏幕重置	
			time.sleep(0.05)#每次休眠0.05秒跳到下一桢
			pygame.display.update()

	#获取所有的时间(敲击键盘，鼠标点击等)
	def get_event(self,my_tank,screen):
		for event in pygame.event.get():
			if event.type in (QUIT,MOUSEBUTTONUP):
				self.stopGame()#程序退出
			if event.type==KEYDOWN and (not my_tank) and event.key==K_n:
				TankMain.my_tank=My_Tank(screen)
			if event.type==KEYDOWN and my_tank:
				if event.key==K_LEFT:
					my_tank.direction="L"
					my_tank.stop=False
					#my_tank.move()
				if event.key==K_RIGHT:
					my_tank.direction="R"
					my_tank.stop=False
					#my_tank.move()
				if event.key==K_UP:
					my_tank.direction="U"
					my_tank.stop=False
					#my_tank.move()
				if event.key==K_DOWN:
					my_tank.direction="D"
					my_tank.stop=False
					#my_tank.move()
				if event.key==K_ESCAPE:#敲击键盘ESC
					self.stopGame()
				if event.key==K_SPACE:
					m=my_tank.fire()
					m.good=True#我方炮弹
					TankMain.my_tank_missile_list.append(m)
			if event.type==KEYUP and my_tank:
				if event.key==K_LEFT or event.key==K_RIGHT or event.key==K_UP or event.key==K_DOWN:
					my_tank.stop=True

	#关闭游戏
	def stopGame(self):
		sys.exit()
	#在屏幕的左上方显示文字内容
	def write_text(self):
		font=pygame.font.SysFont('stxiheittf',12)#定义一个字体
		text_sf1=font.render('敌方坦克数量为:%d'%len(TankMain.enemy_list),True,(255,0,0))#根据字体创建一个文件图像
		text_sf2=font.render('我方炮弹的数量为:%d'%len(TankMain.my_tank_missile_list),True,(255,0,0))#根据字体创建一个文件图像
		return text_sf1, text_sf2

#坦克大战游戏中所有对象的父类
class BaseItem(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		#所有对象共享的属性
		self.screen=screen#坦克在移动或者显示过程中需要用到当前游戏的屏幕

	#在游戏屏幕中显示但前游戏对象
	def display(self):
		if self.live:
			self.image=self.images[self.direction]
			self.screen.blit(self.image,self.rect)

#坦克的公共父类
class Tank(BaseItem):
	#定义类属性，所有坦克对象高和宽都是一样
	width=50
	height=50
	def __init__(self,screen,left,top):
		super().__init__(screen)	
		self.direction='D'#坦克的方向，默认方向往下，上下左右
		self.speed=5#坦克移动的速度
		self.stop=False
		self.images={}#坦克的所有图片，key：方向，value：图片
		self.images['L']=pygame.image.load('images/tankL.png')
		self.images['R']=pygame.image.load('images/tankR.png')
		self.images['U']=pygame.image.load('images/tankU.png')
		self.images['D']=pygame.image.load('images/tankD.png')
		self.image=self.images[self.direction]#坦克的图片由方向决定
		self.rect=self.image.get_rect()
		self.rect.left=left
		self.rect.top=top
		self.live=True#决定坦克是否消灭了
		self.oldtop=self.rect.top
		self.oldleft=self.rect.left

	def stay(self):
		self.rect.top=self.oldtop
		self.rect.left=self.oldleft

	def move(self):
		if not self.stop :#如果坦克不是停止状态
			self.oldleft=self.rect.left
			self.oldtop=self.rect.top
			if self.direction=='L':
				if self.rect.left>0:#判断坦克是否在屏幕左边的边界上
					self.rect.left-=self.speed
				else:
					self.rect.left=0
			elif self.direction=='R':#如果坦克方向向右，坦克的right增加就ok了
				if self.rect.right<TankMain.width:#坦克已经在屏幕的最右边的话就不能往右移动了
					self.rect.right+=self.speed
				else:
					self.rect.right=TankMain.width
			elif self.direction=='D':
				if self.rect.bottom<TankMain.height:
					self.rect.bottom+=self.speed
				else:
					self.rect.bottom=TankMain.height
			elif self.direction=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.rect.top=0
	def fire(self):
		m=Missile(self.screen,self)
		return m
#我方坦克的类
class My_Tank(Tank):
	def __init__(self,screen):
		super().__init__(screen,275,400)
		self.stop=True
		self.live=True

	def hit_enemy_missile(self):
		hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_missile_list,False)#用我方坦克与敌方炮弹进行碰撞
		for m in hit_list:#我方坦克中弹了
			m.live=False
			TankMain.enemy_missile_list.remove(m)
			self.live=False
			explode=Explode(self.screen,self.rect)
			TankMain.explode_list.append(explode)

class Enemy_Tank(Tank):

	def __init__(self,screen):
		super().__init__(screen,randint(1,5)*100,200)
		self.speed=4
		self.step=8#坦克按照某个方向移动的步数
		self.get_random_direction()

	def get_random_direction(self):
		r=randint(0,4)#得到一个坦克移动方向和停止的随机数
		if r==4:
			self.stop=True
		elif r==1:
			self.direction="L"
			self.stop=False
		elif r==2:
			self.direction="R"
			self.stop=False
		elif r==0:
			self.direction="D"
			self.stop=False
		elif r==3:
			self.direction="U"
			self.stop=False

	#敌方坦克，按照一个确定随机方向，连续移动6步，然后才能再次改变方向。
	def random_move(self):
		if self.live:
			#print(self.step)
			if self.step==0:
				self.get_random_direction()
				self.step=6
			else:
				self.move()
				self.step-=1
	def random_fire(self):
		r=randint(0,50)
		if r>45:
			m=self.fire()
			TankMain.enemy_missile_list.add(m)
		else:
			return
class Missile(BaseItem):
	width=12
	height=12
	def __init__(self,screen,tank):
		super().__init__(screen)
		self.tank=tank
		self.direction=tank.direction#炮弹的方向由所发射的坦克方向决定
		self.speed=12#炮弹移动的速度
		self.images={}#炮弹的所有图片，key：方向，value：图片
		self.images['L']=pygame.image.load('images/missileL.jpg')
		self.images['R']=pygame.image.load('images/missileR.jpg')
		self.images['U']=pygame.image.load('images/missileU.jpg')
		self.images['D']=pygame.image.load('images/missileD.jpg')
		self.image=self.images[self.direction]#坦克的图片由方向决定
		self.rect=self.image.get_rect()
		self.rect.left=tank.rect.left+(tank.width-self.width) /2
		self.rect.top=tank.rect.top+(tank.height-self.height) /2
		self.live=True#炮弹是否消灭了
		self.good=False

	def move(self):
		if self.live:#如果炮弹还存在
			if self.direction=='L':
				if self.rect.left>0:#判断坦克是否在屏幕左边的边界上
					self.rect.left-=self.speed
				else:
					self.live=False
			elif self.direction=='R':#如果坦克方向向右，坦克的right增加就ok了
				if self.rect.right<TankMain.width:#坦克已经在屏幕的最右边的话就不能往右移动了
					self.rect.right+=self.speed
				else:
					self.live=False
			elif self.direction=='D':
				if self.rect.bottom<TankMain.height:
					self.rect.bottom+=self.speed
				else:
					self.live=False
			elif self.direction=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.live=False
	#炮弹击中坦克,第一种我方的炮弹击中敌方坦克，敌方炮弹击中我方坦克
	def hit_tank(self):
		if self.good:#如果炮弹是我方炮弹
			hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_list,False)#列表
			for e in hit_list:
				e.live=False
				TankMain.enemy_list.remove(e)
				self.live=False
				explode=Explode(self.screen,e.rect)#产生一个爆炸对象
				TankMain.explode_list.append(explode)

#爆炸类
class Explode(BaseItem):
	def __init__(self,screen,rect):
		super().__init__(screen)
		self.live=True
		self.images=[pygame.image.load('images/1.jpg'),\
					 pygame.image.load('images/2.jpg'),\
					 pygame.image.load('images/3.jpg'),\
					 pygame.image.load('images/4.jpg'),\
					 pygame.image.load('images/5.jpg'),\
					 pygame.image.load('images/6.jpg'),\
					 pygame.image.load('images/7.jpg'),\
					 pygame.image.load('images/8.jpg'),\
					 pygame.image.load('images/9.jpg'),\
					 pygame.image.load('images/10.jpg')]

		self.step=0
		self.rect=rect#爆炸的位置和发生爆炸前，炮弹碰到的坦克位置一样，在构建爆炸的时候吧坦克的rect传递进来

	#display方法在整个游戏运行过程中，循环调用，每隔0.05秒调用一次
	def display(self):
		if self.live:
			if self.step==len(self.images):#最后一张图片已经显示了
				self.live=False
			else:
				self.image=self.images[self.step]
				self.screen.blit(self.image,self.rect)
				self.step+=1
		else:
			pass#删除该对象			

#游戏中的障碍物
class Wall(BaseItem):
	def __init__(self,screen,left,top,width,height):
		super().__init__(screen)
		self.rect=Rect(left,top,width,height)
		self.color=(255,0,0)
	def display(self):
		self.screen.fill(self.color,self.rect)

	#针对墙和其他坦克或者炮弹的碰撞检测
	def hit_other(self):
		if TankMain.my_tank:
			is_hit=pygame.sprite.collide_rect(self,TankMain.my_tank)
			if is_hit:
				TankMain.my_tank.stop=True
				TankMain.my_tank.stay()
		if len(TankMain.enemy_list)!=0:
			hit_list=pygame.sprite.spritecollide(self,TankMain.enemy_list,False)
			for e in hit_list:
				e.stop=True
				e.stay()

game=TankMain()
game.startGame()







'''
 'diwanthuluthttf',
 'sfcompactdisplayttf',
 'toppanbunkyuminchopr6nregularotf',
 'stixsiztwosymbolotf',
 'kohinoorbanglattc',
 'silomttf',
 'sfnstextcondensedlightotf',
 'sfnstextcondensedboldotf',
 'muktamaheettc',
 'stixsizonesymbolotf',
 'chalkboardsettc',
 'arialnarrowitalicttf',
 'gillsansttc',
 'keyboardttf',
 'galvjittc',
 'comicsansmsttf',
 'weibeiscboldotf',
 'applegothicttf',
 'sfnsdisplaycondensedheavyotf',
 'stixsiztwosymregotf',
 'timesnewromanbolditalicttf',
 'symbolttf',
 'tahomaboldttf',
 'nanummyeongjottc',
 'arabicuitextttc',
 'notosansmyanmarttc',
 'sfnsroundedttf',
 'comicsansmsboldttf',
 'applelisunglightttf',
 'kohinoorgujaratittc',
 'impactttf',
 'timesnewromanttf',
 'ヒラキノ角コシックw1ttc',
 'songtittc',
 'yugothicmediumotf',
 'stixintupdbolotf',
 'kleettc',
 'arabicuidisplayttc',
 'myanmarmnttc',
 'ヒラキノ角コシックw8ttc',
 'verdanaboldttf',
 'sfnsdisplaycondensedultralightotf',
 'papyrusttc',
 'avenirnextttc',
 'notonastaliqttc',
 'luminarittf',
 'munattc',
 'trattatellottf',
 'wawascregularotf',
 'sfnstextcondensedheavyotf',
 'stixvarotf',
 'biaukaittf',
 'sfnstextcondensedsemiboldotf',
 'shree714ttc',
 'decotypenaskhttc',
 'kohinoorttc',
 'newpeninimmtttc',
 'markerfeltttc',
 'liheiprottf',
 'sfnsdisplaycondensedblackotf',
 'stfangsottf',
 'ptserifttc',
 'stixsizonesymregotf',
 'snellroundhandttc',
 'gurmukhisangammnttc',
 'sfnsdisplaycondensedlightotf',
 'andalemonottf',
 'trebuchetmsboldttf',
 'copperplatettc',
 'charterttc',
 'banglasangammnttc',
 'sathuttf',
 'nisc18030ttf',
 'kokonorttf',
 'applesdgothicneottc',
 'bodoni72osttc',
 'helveticaneuedeskinterfacettc',
 'sfcompacttextttf',
 'hannotatettc',
 'khmersangammnttf',
 'toppanbunkyugothicpr6nttc',
 'yuantittc',
 'stixintupsmregotf',
 'laomnttc',
 'ヒラキノ角コシックw6ttc',
 'bodoni72smallcapsbookttf',
 'pcmyoungjottf',
 'kaitittc',
 'kohinoorteluguttc',
 'stixgeneralbolitaotf',
 'verdanaitalicttf',
 'lingwaiscmediumotf',
 'applebraillettf',
 'mshtakanttc',
 'heittf',
 'sinhalasangammnttc',
 'tamilsangammnttc',
 'beirutttc',
 'sfnsdisplaycondensedsemiboldotf',
 'stixsizfoursymregotf',
 'libianttc',
 'stixgeneralbolotf',
 'mishafigoldttf',
 'verdanabolditalicttf',
 'timesttc',
 'kannadamnttc',
 'chalkboardttc',
 'stixnonunibolotf',
 'notoserifmyanmarttc',
 'laosangammnttf',
 'applebrailleoutline6dotttf',
 'couriernewboldttf',
 'cochinttc',
 'sfnsdisplaycondensedmediumotf',
 'microsoftsansserifttf',
 'thonburittc',
 'georgiattf',
 'altarikhttc',
 'yugothicboldotf',
 'sfnstextcondensedmediumotf',
 'nanumscriptttc',
 'couriernewitalicttf',
 'ヒラキノ角コシックw4ttc',
 'helveticattc',
 'corsivattc',
 'arialnarrowboldttf',
 'arialblackttf',
 'raananattc',
 'malayalammnttc',
 'malayalamsangammnttc',
 'oriyasangammnttc',
 'weibeitcboldotf',
 'signpainterttc',
 'toppanbunkyumidashiminchostdnextraboldotf',
 'phosphatettc',
 'itfdevanagarittc',
 'savoyeletttc',
 'ヒラキノ丸コpronw4ttc',
 'zapfinottf',
 'devanagarimtttc',
 'albayanttc',
 'sfnsmonottf',
 'lucidagrandettc',
 'khmermnttc',
 'kufistandardgkttc',
 'stheitittf',
 'waseemttc',
 'rockwellttc',
 'georgiaitalicttf',
 'stixintsmregotf',
 'herculanumttf',
 'kaittf',
 'toppanbunkyumidashigothicstdnextraboldotf',
 'notosansjavaneseregularotf',
 'avenirnextcondensedttc',
 'stheitilightttc',
 'ptsansttc',
 'ヒラキノ角コシックw2ttc',
 'notosanskannadattc',
 'sfnstextcondensedregularotf',
 'hoeflertextornamentsttf',
 'plantagenetcherokeettf',
 'dincondensedboldttf',
 'ヒラキノ角コシックw9ttc',
 'sfnsmonoitalicttf',
 'stixintdbolotf',
 'futurattc',
 'banglamnttc',
 'applesymbolsttf',
 'couriernewttf',
 'telugumnttc',
 'hiraginosansgbttc',
 'chalkdusterttf',
 'farahttc',
 'arialttf',
 'arialboldttf',
 'stixsizfoursymbolotf',
 'applechanceryttf',
 'arialitalicttf',
 'stheitimediumttc',
 'geezaprottc',
 'mishafittf',
 'pilgichettf',
 'stixintupregotf',
 'bodoniornamentsttf',
 'baskervillettc',
 'sfnsttf',
 'myanmarsangammnttc',
 'trebuchetmsbolditalicttf',
 'bodoni72ttc',
 'sinhalamnttc',
 'telugusangammnttc',
 'baghdadttc',
 'skiattf',
 'arialbolditalicttf',
 'nanumgothicttc',
 'sfcompactroundedttf',
 'wingdingsttf',
 'palatinottc',
 'diwankufittc',
 'stixnonuniotf',
 'applebraillepinpoint6dotttf',
 'ヒラキノ角コシックw0ttc',
 'bigcaslonttf',
 'wawatcregularotf',
 'xingkaittc',
 'helveticaneuettc',
 'arialhbttc',
 'krungthepttf',
 'sfnsdisplaycondensedboldotf',
 'gujaratisangammnttc',
 'hanzipenttc',
 'hoeflertextttc',
 'headlineattf',
 'ヒラキノ角コシックw7ttc',
 'applebrailleoutline8dotttf',
 'tahomattf',
 'stixintupbolotf',
 'sfnsitalicttf',
 'sanattc',
 'kailasattc',
 'baolittc',
 'stixintsmbolotf',
 'kefattc',
 'menlottc',
 'ayuthayattf',
 'applecoloremojittc',
 'hiraginosanscnsttc',
 'damascusttc',
 'yuppytcregularotf',
 'wingdings2ttf',
 'didotttc',
 'yuminchottc',
 'verdanattf',
 'timesnewromanitalicttf',
 'tsukushiamarugothicttc',
 'couriernewbolditalicttf',
 'osakattf',
 'euphemiacasttc',
 'inaimathimnttc',
 'sukhumvitsetttc',
 'farisittf',
 'notosansoriyattc',
 'gurmukhimnttc',
 'osakamonottf',
 'lantingheittc',
 'kannadasangammnttc',
 'zapfdingbatsttf',
 'trebuchetmsitalicttf',
 'yuppyscregularotf',
 'ヒラキノ角コシックw5ttc',
 'devanagarisangammnttc',
 'arialnarrowbolditalicttf',
 'trebuchetmsttf',
 'nadeemttc',
 'stixgeneralitalicotf',
 'arialunicodettf',
 'americantypewriterttc',
 'arialnarrowttf',
 'sfcompacttextitalicttf']
 stxiheittf	
lingwaitcmediumotf
'''

