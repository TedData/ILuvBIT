import pygame,sys
from pygame.locals import *
pygame.init()


screen=pygame.display.set_mode((600,500),0,32)
myfront = pygame.font.Font(None,100)
textImage = myfront.render('hello', True, (255,0,0))
while True:
	#screen.fill((255,255,255))
	#screen.blit(textImage, (50, 350))
	pygame.display.update()
	#screen.blit(textImage, (50, 350))	
	screen.fill((0,255,255))
	screen.blit(textImage, (50, 350))	
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
'''
screen = pygame.display.set_mode((600, 500))
myfront = pygame.font.Font(None,100)
textImage = myfront.render("Hello Pygame", True, (0,0,100))
while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    pygame.display.update()
    screen.fill((255,255,255))
    screen.blit(textImage, (50, 350))'''