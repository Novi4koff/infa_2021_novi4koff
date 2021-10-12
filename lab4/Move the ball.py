#importing libraries
import pygame
from pygame.draw import *
from random import randint
pygame.init()

#setting FPS and display
FPS = 100
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

def new_ball():
    '''This function draws new ball centered at a random point (x, y) and with random radius r
    and also adds the point (x, y, r) to the list of the coordinates of all balls'''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    global color
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    

new_ball()    
coordinates = [x, y]

case = 1

clock = pygame.time.Clock()
finished = False

while not finished:
    
    clock.tick(FPS)
    if case == 1:
        
        if 0 <= coordinates[0] <= 1200 and 0 <= coordinates[1] <= 900:
            coordinates[0] += 1
            coordinates[1] += 1
            circle(screen, color, coordinates, r)
            pygame.display.update()
            screen.fill(BLACK)
        elif coordinates[0] == 1200 and coordinates[1] < 900:
            case = 2
        elif coordinates[0] < 1200 and coordinates[1] == 900:
            case = 3
    elif case == 2:
        if 0 <= coordinates[0] <= 1200 and 0 <= coordinates[1] <= 900:
            coordinates[0] -= 1
            coordinates[1] += 1
            circle(screen, color, coordinates, r)
            pygame.display.update()
            screen.fill(BLACK)
    elif case == 3:
        if 0 <= coordinates[0] <= 1200 and 0 <= coordinates[1] <= 900:
            coordinates[0] += 1
            coordinates[1] -= 1
            circle(screen, color, coordinates, r)
            pygame.display.update()
            screen.fill(BLACK)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
         
pygame.quit()



