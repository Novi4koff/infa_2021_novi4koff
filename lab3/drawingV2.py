import pygame
from pygame.draw import rect
from pygame.draw import polygon
from pygame.draw import circle
from pygame.draw import ellipse
from pygame.draw import lines

pygame.init()

FPS = 30
screen = pygame.display.set_mode((650, 700)) #Устанавливаю масштаб рисунка

LightGreen = (199, 255, 142) #Палитра
Green = (0, 232, 0)
White = (255, 255, 255)
Black = (0, 0, 0)
Blue = (164, 220, 255)
Grey = (154, 154, 154)
Yellow = (250, 255, 0)

screen.fill(LightGreen) #Заливаю экран цветом

#Рисую границы неба и гор
polygon(screen, Blue, [(0, 0), (0, 200), (100, 120), (150, 180), (300, 50), (400, 300), (500, 200), (550, 400), (650, 150), (650, 0)], 0)

#Рисую границы гор и лужайки
polygon(screen, Grey, [(0, 200), (100, 120), (150, 180), (300, 50), (400, 300), (500, 200), (550, 400), (650, 150), (650, 450), (340, 450), (325, 445), (325, 425), (323, 422), (323, 415), (300, 425), (160,425), (120, 440), (80,440), (0, 460)], 0)

#Обвожу границы неба, гор и лужайки чёрным
lines(screen, Black, True, [(0, 200), (100, 120), (150, 180), (300, 50), (400, 300), (500, 200), (550, 400), (650, 150), (650, 450), (340, 450), (325, 445), (325, 425), (323, 422), (323, 415), (300, 425), (160,425), (120, 440), (80,440), (0, 460)], 3)


def grass(x, y, size):
	#Эта функция рисует траву в виде зелёного круга с центром в точке (x, y) и радиусом size
	circle(screen, Green, (x, y), size)

def flower(x, y, size):
	#Эта функция рисует цветок с жёлтой сердцевиной и белыми лепестками с центром в точке (x,y) и размером, в size раз больще единичного размера
    ellipse(screen, White, [(x - 4*size, y + 2*size), (8*size, 4*size)])
    ellipse(screen, White, [(x - 4*size, y - 6*size), (8*size, 4*size)])
    ellipse(screen, White, [(x - 9*size, y - 4*size), (8*size, 4*size)])
    ellipse(screen, White, [(x - 9*size, y), (8*size, 4*size)])
    ellipse(screen, White, [(x + size, y - 4*size), (8*size, 4*size)])
    ellipse(screen, White, [(x + size, y), (8*size, 4*size)])
    ellipse(screen, Yellow, [(x - 4*size, y - 2*size), (8*size, 4*size)])

#Засеиваем лужайку травой
grass(600, 650,  40)
grass(30, 500, 35)
grass(200, 600, 50)
grass(400, 550, 70)
grass(550, 500, 30)

#Засеиваем траву цветочками
flower(420, 560, 2)
flower(400, 520, 2)
flower(410, 600, 2)
flower(370, 580, 2)
flower(30, 500, 1)
flower(20, 515, 1)
flower(40, 515, 1)
flower(10, 500, 1)
flower(20, 485, 1)
flower(560, 500, 1)
flower(540, 490, 1)
flower(542, 510, 1)
flower(190, 600, 1.5)
flower(210, 625, 1.5)
flower(215, 590, 1.5)
flower(595, 645, 1.5)
flower(615, 660, 1.5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
