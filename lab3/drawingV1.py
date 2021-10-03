import pygame
from pygame.draw import rect
from pygame.draw import polygon
from pygame.draw import circle
from pygame.draw import ellipse
from pygame.draw import line

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 1000))

screen.fill((199, 255, 142))


circle(screen, (0, 232, 0), (625, 800), 100) #Луг


ellipse(screen, (255, 255, 255), [(100, 600), (200, 80)]) #Туловище
ellipse(screen, (255, 255, 255), [(250, 475), (50, 150)]) #Шея
ellipse(screen, (255, 255, 255), [(260, 440), (60, 45)]) #Голова


line(screen, (0, 0, 0), (0, 430), (120, 50), 1) #Начинаю рисовать горы

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()


