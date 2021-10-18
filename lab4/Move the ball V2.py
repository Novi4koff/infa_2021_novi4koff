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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class ball:
    def init(self):
        self.x = randint(400, 700)
        self.y = randint(300, 600)
        self.v_x = randint(-300, 300)
        self.v_y = randint(-300, 300)
        self.r = randint(5, 30)
        self.color = COLORS[randint(0, 5)]

    def draw(self, surface):
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        if (self.x + self.r > 1200) or (self.x - self.r < 0):
            self.v_x *= -1
        if (self.y + self.r > 900) or (self.y - self.r < 0):
            self.v_y *= -1
        self.x += self.v_x * 0.01
        self.y += self.v_y * 0.01

list_of_balls = list()

for i in range(randint(5, 10)):
    tmp_ball = ball()
    list_of_balls.append(tmp_ball)
    list_of_balls[i].init()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    for j in range(len(list_of_balls)):
        list_of_balls[j].draw(screen)
        list_of_balls[j].move()
    pygame.display.update()
    screen.fill(BLACK)
    
pygame.quit()
