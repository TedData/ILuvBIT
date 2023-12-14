import pygame,sys,random,time
from pygame.locals import *
pygame.init()
class air_main(object):
	width=1800
	heigth=1200
	my_air=None
	enemy_air_list=pygame.sprite.Group()
	air_missile_list=pygame.sprite.Group()
	enemy_missile_list=pygame.sprite.Group()
	upgrade_list=pygame.sprite.Group()
	upgrade_p_list=pygame.sprite.Group()
	upgrade_e_list=pygame.sprite.Group()
	def __init__(self):
		self.score=0
		self.missile_speed=0
		self.air_speed=0
	def start_game(self):
		screen=pygame.display.set_mode((air_main.width,air_main.heigth),0,32)
		pygame.display.set_caption('飞机大战')	
		air_main.my_air=my_air(screen)
		
		for i in range(0,6):
			air_main.enemy_air_list.add(enemy_air(screen))
		frequency=0
		greater_score=game.score
		



		while True:
			time.sleep(0.06)
			pygame.display.update()
			screen.fill((255,255,255))
			self.get_event(air_main.my_air,screen)
			
			if air_main.my_air:
				for i,text1 in enumerate(self.air_level(),0):
					screen.blit(text1,(0,5+(90*i)))
				for j,text2 in enumerate(self.air_score(),0):
					screen.blit(text2,(1300,50+(90*j)))
				air_main.my_air.air_to_enemy_air()
				air_main.my_air.air_to_enemy_missile()
				air_main.my_air.air_to_pgrade()
			else:
				for o,text3 in enumerate(self.air_game_over(),0):
					screen.blit(text3,(300,250+(390*o)))
			if air_main.my_air and air_main.my_air.live:
				
				air_main.my_air.display()
				air_main.my_air.air_random_fire()
				air_main.my_air.move()
			else:
				air_main.my_air=None
			

			
			for ene in air_main.enemy_air_list:
				if ene.live:
					ene.display()
					ene.enemy_move()
					ene.random_fire()
				else:
					air_main.enemy_air_list.remove(ene)
			if frequency==40:
				frequency=1
				enemy_air_number=random.randint(1,6)
				while enemy_air_number-frequency :
					air_main.enemy_air_list.add(enemy_air(screen))
					enemy_air_number-=1
			frequency+=1
			
			if game.score!=greater_score:
				r=random.randint(1,3)
				if r==1:
					air_main.upgrade_list.add(upgrade(screen))
				elif r==2:
					air_main.upgrade_e_list.add(upgrade_e(screen))
				elif r==3:
					air_main.upgrade_p_list.add(upgrade_p(screen))
				greater_score=game.score

			for up in air_main.upgrade_list:
				if up.live:
					up.display()
					up.upgrade_move()
				else:
					air_main.upgrade_list.remove(up)
			for up1 in air_main.upgrade_e_list:
				if up1.live:
					up1.display()
					up1.upgrade_move()
				else:
					air_main.upgrade_e_list.remove(up1)
			for up2 in air_main.upgrade_p_list:
				if up2.live:
					up2.display()
					up2.upgrade_move()
				else:
					air_main.upgrade_p_list.remove(up2)


			for m in air_main.air_missile_list:
				if m.live:
					m.display()
					m.missile_to_enemy_air()
					m.move()
				else:
					air_main.air_missile_list.remove(m)
			

			for n in air_main.enemy_missile_list:
				if n.live:
					n.display()
					n.move()

				else:
					air_main.enemy_missile_list.remove(n)
	def air_level(self):
		front=pygame.font.Font(None,80)
		text_sf1=front.render('POWER:%d'%game.missile_speed,True,(255,0,0))
		text_sf2=front.render('SPEED:%d'%game.air_speed,True,(255,0,0))
		return text_sf1, text_sf2
	def air_score(self):
		front=pygame.font.Font(None,100)
		text_sf3=front.render('SCORE:%d'%game.score,True,(255,0,0))
		text_sf4=front.render('ENEMY:%d'%len(air_main.enemy_air_list),True,(255,0,0))
		return text_sf4, text_sf3
	def air_game_over(self):
		front=pygame.font.Font(None,300)
		text_sf5=front.render('SCORE:%d'%game.score,True,(255,0,0))
		text_sf6=front.render('GAME OVER',True,(255,0,0))
		return text_sf6, text_sf5

	def get_event(self,my_air,screen):
		for event in pygame.event.get():
			if event.type in (QUIT,MOUSEBUTTONUP):
				self.stop_game()
			elif event.type==KEYDOWN and (not my_air) and event.key==K_n:
				air_main.my_air=my_air(screen)

			elif event.type==KEYDOWN:
				if event.key==K_LEFT:
					my_air.direct='L'
					my_air.run=True
				elif event.key==K_RIGHT:
					my_air.direct='R'
					my_air.run=True
				elif event.key==K_UP:
					my_air.direct='U'
					my_air.run=True
				elif event.key==K_DOWN:
					my_air.direct='D'
					my_air.run=True
				elif event.key==K_SPACE:
					m=my_air.fire()
					m.good=True#我方炮弹
					air_main.air_missile_list.add(m)#添加炮弹
	

				elif event.key==K_ESCAPE:
					self.stop_game()
			if event.type==KEYUP and my_air:
				if event.key in (K_DOWN,K_LEFT,K_RIGHT,K_UP):
					my_air.run=False
	def stop_game(self):
		sys.exit()




class BaseItem(pygame.sprite.Sprite):
	def __init__(self,screen):
		pygame.sprite.Sprite.__init__(self)
		self.screen=screen
	def display(self):
		if self.live:
			self.image=self.images[self.direction]
			self.screen.blit(self.image,self.rect)
class all_air(BaseItem):
	width=100
	heigth=100
	def __init__(self,screen):
		super().__init__(screen)
		self.direction='U'
		self.direct='U'
		self.images={}
		self.images['U']=pygame.image.load('Images/my_air.jpg')
		self.images['D']=pygame.image.load('Images/enemy_air.jpg')
		self.images['R']=pygame.image.load('Images/enemy_air.jpg')
		self.images['L']=pygame.image.load('Images/enemy_air.jpg')
		self.image=self.images[self.direction]
		self.rect=self.image.get_rect()
		self.live=True
		self.speed=35
		self.run=False
	def move(self):
		if self.run:
			if self.direct=='L':
				if self.rect.left>0:
					self.rect.left-=self.speed
				else:
					self.rect.left=0
			elif self.direct=='R':
				if self.rect.right<air_main.width:
					self.rect.right+=self.speed
				else:
					self.rect.right=air_main.width
			elif self.direct=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.rect.top=0
			elif self.direct=='D':
				if self.rect.bottom<air_main.heigth:
					self.rect.bottom+=self.speed
				else:
					self.rect.bottom=air_main.heigth
	def fire(self):
		m=all_missile(self.screen,self)
		return m
class my_air(all_air):
	def __init__(self,screen):
		super().__init__(screen)
		self.rect.left=600
		self.rect.top=800
		self.live=True

	def air_random_fire(self):
		r=random.randint(0,(5000+game.air_speed*100))
		if r>4500:
			m=self.fire()
			m.good=True
			air_main.air_missile_list.add(m)
		else:
			return




	def air_to_enemy_missile(self):
		hit_list1=pygame.sprite.spritecollide(self,air_main.enemy_missile_list,False)
		for m in hit_list1:
			m.live=False
			air_main.enemy_missile_list.remove(m)
			self.live=False
	def air_to_enemy_air(self):	
		hit_list2=pygame.sprite.spritecollide(self,air_main.enemy_air_list,False)
		for n in hit_list2:
			n.live=False
			air_main.enemy_air_list.remove(n)
			self.live=False
	def air_to_pgrade(self):
		hit_list3=pygame.sprite.spritecollide(self,air_main.upgrade_list,False)
		for p in hit_list3:
			p.live=False
			game.air_speed+=20
			self.live=True
		hit_list4=pygame.sprite.spritecollide(self,air_main.upgrade_p_list,False)
		for s in hit_list4:
			s.live=False
			game.missile_speed+=10
			self.live=True
		hit_list5=pygame.sprite.spritecollide(self,air_main.upgrade_e_list,False)
		for e in hit_list5:
			e.live=False
			for a in air_main.enemy_air_list:
				a.live=False
				air_main.enemy_air_list.remove(a)
				game.score+=1
			for b in air_main.enemy_missile_list:
				b.live=False
				air_main.enemy_missile_list.remove(b)
			self.live=True

class enemy_air(all_air):
	def __init__(self,screen):
		super().__init__(screen)
		self.live=True
		self.direction='D'#初始方向
		self.direct='D'
		self.speed=10+(game.score//4)
		self.rect.left=random.randint(1,9)*120
		self.rect.top=50
		self.get_random_direction()
	def get_random_direction(self):
		r=random.randint(0,5)
		if r==1:
			self.direction="L"
		elif r==2:
			self.direction="R"
		elif r==0:
			self.direction="D"
		self.run=True

	def enemy_move(self):
		if self.live:
			self.run=True
			self.direct='D'
			self.move()
			if not(self.rect.bottom<air_main.heigth):
				self.live=False
	def random_fire(self):
		r=random.randint(0,(5000+game.score*5))
		if r>5000:
			m=self.fire()
			air_main.enemy_missile_list.add(m)
		else:
			return

class all_missile(BaseItem):
	width=22
	heigth=22
	def __init__(self,screen,all_air):
		super().__init__(screen)
		self.live=True
		self.all_air=all_air
		self.direction=all_air.direction
		self.speed=30+game.missile_speed
		self.enemy_speed=20+game.score
		self.images={}
		self.images['L']=pygame.image.load('Images/missile_LL.jpg')
		self.images['U']=pygame.image.load('Images/missile_U.jpg')
		self.images['R']=pygame.image.load('Images/missile_RR.jpg')
		self.images['D']=pygame.image.load('Images/missile_D.jpg')
		self.image=self.images[self.direction]
		self.rect=self.image.get_rect()
		self.rect.left=all_air.rect.left+(all_air.width-self.width)/2
		self.rect.top=all_air.rect.top+(all_air.heigth-self.heigth)/2
		self.good=False
	def move(self):
		if self.live:#如果炮弹存在
			if self.direction=='L':
				if self.rect.bottom<air_main.heigth:
					self.rect.left-=(self.enemy_speed/2)
					self.rect.bottom+=self.enemy_speed
				else:
					self.live=False	
			elif self.direction=='R':
				if self.rect.bottom<air_main.heigth:
					self.rect.bottom+=self.enemy_speed
					self.rect.right+=(self.enemy_speed/2)
				else:
					self.live=False	
			elif self.direction=='U':
				if self.rect.top>0:
					self.rect.top-=self.speed
				else:
					self.live=False	
			elif self.direction=='D':
				if self.rect.bottom<air_main.heigth:
					self.rect.bottom+=self.enemy_speed
				else:
					self.live=False	
	def missile_to_enemy_air(self):
		if self.good:
			hit_list=pygame.sprite.spritecollide(self,air_main.enemy_air_list,False)
			for e in hit_list:
				e.live=False
				air_main.enemy_air_list.remove(e)
				self.live=False
				game.score+=1
		


class upgrade(all_air):
	def __init__(self,screen):
		super().__init__(screen)
		self.live=True
		#self.get_random_upgrade()
		self.speed=10
		self.images={}
		self.direction='S'
		self.images['P']=pygame.image.load('Images/upgrade_P.jpg')
		self.images['S']=pygame.image.load('Images/upgrade_S.jpg')
		self.images['E']=pygame.image.load('Images/upgrade_E.jpg')
		self.image=self.images[self.direction]
		self.rect=self.image.get_rect()
		self.rect.left=random.randint(2,17)*100
		self.rect.top=random.randint(2,17)*100
		'''
		g=random.randint(1,3)
		if g==1:
			self.direction='P'
		elif g==2:
			self.direction='S'
		elif g==3:
			self.direction='E'''
		self.run=True

	'''
	def get_random_upgrade(self):
		g=random.randint(1,3)
		if g==1:
			self.direction='P'
		elif g==2:
			self.direction='S'
		elif g==3:
			self.direction='E'
		self.run=True'''

	def upgrade_move(self):
		if self.live:
			self.run=True
			self.direct='D'
			self.move()
			if not(self.rect.bottom<air_main.heigth):
				self.live=False


class upgrade_p(upgrade):
	def __init__(self,screen):
		super().__init__(screen)
		self.direction='P'

class upgrade_e(upgrade):
	def __init__(self,screen):
		super().__init__(screen)
		self.direction='E'
		





if __name__ == '__main__':
	
	game=air_main()
	#upgrades=upgrade(air_main)
	game.start_game()
