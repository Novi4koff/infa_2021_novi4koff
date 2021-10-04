#подключение библиотек
import pygame
from pygame.draw import rect
from pygame.draw import polygon
from pygame.draw import circle
from pygame.draw import ellipse
from pygame.draw import lines

#инициализация модуля pygame
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
Pink = (255, 0, 250)

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
    ellipse(screen, White, [(x - 4*size, y + 2*size), (8*size, 4*size)]) #Нижний лепесток
    ellipse(screen, White, [(x - 4*size, y - 6*size), (8*size, 4*size)]) #Верхний лепесток
    ellipse(screen, White, [(x - 9*size, y - 4*size), (8*size, 4*size)]) #Верхний правый диагональный лепесток
    ellipse(screen, White, [(x - 9*size, y), (8*size, 4*size)]) #Нижний правый диагональный лепесток
    ellipse(screen, White, [(x + size, y - 4*size), (8*size, 4*size)]) #Верхний левый диагональный лепесток
    ellipse(screen, White, [(x + size, y), (8*size, 4*size)]) #Нижний левый диагональный лепесток
    ellipse(screen, Yellow, [(x - 4*size, y - 2*size), (8*size, 4*size)]) #Сердцевина

def lama(x, y, size):
	#Эта функция рисует ламу, центр туловища у которой в точке (x, y), а размеры в size раз превышают "единичный" размер
    ellipse(screen, White, [(x - 2.5*size, y - size), (5*size, 2*size)]) #Туловище
    ellipse(screen, White, [(x + 1.5*size, y - 4*size), (size, 4*size)]) #Шея 
    ellipse(screen, White, [(x + 1.75*size, y - 4.75*size), (4/3 * size, size)]) #Голова
    polygon(screen, White, [(x + 1.75*size, y - 4.25*size), (x + 1.25*size, y - 4.75*size), (x + (1.75 + 2/3)*size, y - 4.25*size)], 0) #Первое ушко
    polygon(screen, White, [(x + (1.75 + 2/3)*size, y - 4.25*size), (x + (1.75 + 4/9)*size, y - 5.25*size), (x + (1.75 + 4/9)*size, y - 4.25*size)], 0) #Второе ушко
    ellipse(screen, Pink, [(x + 2*size, y - 4.625*size), (0.8*size, 0.4*size)]) #Склера
    ellipse(screen, Black, [(x + 2.375*size, y - 4.525*size), (0.4*size, 0.2*size)]) #Зрачок
    ellipse(screen, White, [(x - 2*size, y), (0.75*size, 1.5*size)]) #Бедро 1-й ноги
    ellipse(screen, White, [(x - 2*size, y + 1.25*size), (0.75*size, 1.5*size)]) #Голень 1-й ноги
    ellipse(screen, White, [(x - 2*size,y + 2.5*size), (size, 0.5*size)]) #Стопа 1-й ноги
    ellipse(screen, White, [(x - size, y + 0.5*size), (0.75*size, 1.5*size)]) #Бедро 2-й ноги
    ellipse(screen, White, [(x - size, y + 1.75*size), (0.75*size, 1.5*size)]) #Голень 2-й ноги
    ellipse(screen, White, [(x - size,y + 3*size), (size, 0.5*size)]) #Стопа 2-й ноги
    ellipse(screen, White, [(x + size, y - 0.25*size), (0.75*size, 1.5*size)]) #Бедро 3-й ноги
    ellipse(screen, White, [(x + size, y + size), (0.75*size, 1.5*size)]) #Голень 3-й ноги
    ellipse(screen, White, [(x + size, y + 2.25*size), (size, 0.5*size)]) #Стопа 3-й ноги
    ellipse(screen, White, [(x + 1.75*size, y + 0.5*size), (0.75*size, 1.5*size)]) #Бедро 4-й ноги
    ellipse(screen, White, [(x + 1.75*size, y + 1.75*size), (0.75*size, 1.5*size)]) #Голень 4-й ноги
    ellipse(screen, White, [(x + 1.75*size, y + 3*size), (size, 0.5*size)]) #Стопа 4-й ноги

    
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

#Выведем стадо лам
lama(230, 475 , 25)
lama(25, 650, 40)
lama(450, 450, 15)
lama(475, 600, 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
