#importing libraries
import pygame
from pygame.draw import *
from random import randint
pygame.init()

#setting FPS and display
FPS = 150
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
death = 0
game_over = False

class ball:
    '''This class contains moving balls with its own color, radius, position, and velocity'''
    def init(self):
        '''This function initializes the ball, gives it start velocity, radius, start point, and color'''
        self.x = randint(400, 700)
        self.y = randint(300, 600)
        self.v_x = randint(-350, 350)
        self.v_y = randint(-350, 350)
        self.r = randint(5, 50)
        self.color = COLORS[randint(0, 5)]

    def draw(self, surface):
        '''This function draws the ball as circle in current position'''
        circle(surface, self.color, (self.x, self.y), self.r)

    def move(self):
        '''This funcion moves the ball and allows it to bounce off the walls'''
        if(self.x + self.r > 1200 or self.x - self.r < 0):
            self.v_x *= -1
        if(self.y + self.r > 900 or self.y - self.r < 0):
            self.v_y *= -1
        self.x += self.v_x * 0.01
        self.y += self.v_y * 0.01

    def check(self):
        '''This function checks if we caught the ball. If we did, the score grows higher. If not, we lose'''
        if (self.x - event.x)**2 + (self.y - event.y)**2 <= self.r**2:
            print('Congratulations!!! You caught the ball')
            global score
            score = score + 11 - int(self.r * 0.2)
            print('Your score is', score)
        else:
            global death
            death += 1

list_of_balls = []
for i in range(randint(5, 10)):
	'''This cycle fills the list with our obhjects and initializes them'''
	tmp_ball = ball()
	list_of_balls.append(tmp_ball)
	list_of_balls[i].init()

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while (not finished) and (not game_over):
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished == True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			event.x = event.pos[0]
			event.y = event.pos[1]
			for i in range(len(list_of_balls)):
				list_of_balls[i].check()
			if death == len(list_of_balls):
				game_over = True
			else:
				death = 0
				list_of_balls = []
				for i in range(randint(5, 10)):
					'''This cycle replaces old balls with new ones'''
					tmp_ball = ball()
					list_of_balls.append(tmp_ball)
					list_of_balls[i].init()
	for i in range(len(list_of_balls)):
		list_of_balls[i].draw(screen)
		list_of_balls[i].move()
	pygame.display.update()
	screen.fill(BLACK)
pygame.quit()
print('GAME OVER! Your score is', score)
