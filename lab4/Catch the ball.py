#importing libraries
import pygame
from pygame.draw import *
from random import randint
pygame.init()

#setting FPS and display
FPS = 1.5
screen = pygame.display.set_mode((1200, 900))

#creating palette
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

score = 0


def new_ball():
    '''This function draws new ball centered at a random point (x, y) and with random radius r
    and also adds the point (x, y, r) to the list of the coordinates of all balls'''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    point = [x, y, r]
    coordinates.append(point)
    
def check():
    '''This function checks if we clicked on one of the balls, and if we did, we get new score'''
    j = 0
    while j < len(coordinates):
        coordinate1 = coordinates[j][0]
        coordinate2 = coordinates[j][1]
        radius = coordinates[j][2]
        if (coordinate1 - event.x)**2 + (coordinate2 - event.y)**2 <= radius**2:
            print('Congratulation!!!')
            global score
            score = score + 1
            print('Your score is ', score)
        j += 1

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            event.x = event.pos[0]
            event.y = event.pos[1]
            check()
    coordinates = []        
    i = 0
    while i <= randint(1, 10):
        new_ball()
        i += 1
    
    pygame.display.update()
    screen.fill(BLACK)
pygame.quit()
