import pygame, sys
from pygame.locals import *
pygame.init()
white = 255,255,255
black = 255,0,0
#设置窗口大小
screen = pygame.display.set_mode((600, 500))
#窗口显示内容（字体格式，大小）
myfront = pygame.font.Font(None,100)
#设置窗口显示（内容，锯齿，内容颜色）
textImage = myfront.render("Hello Pygame", True, black)
#设置窗口题目
pygame.display.set_caption('坦克大战')
while True:
    for event in pygame.event.get():
        #如果键盘按任意键，或单击❌，退出
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    #时刻更新
    pygame.display.update()
    #显示背景颜色
    screen.fill(white)
    #显示窗口（内容，位置宽高）
    screen.blit(textImage, (50, 350))