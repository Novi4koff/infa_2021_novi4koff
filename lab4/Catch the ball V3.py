#importing libraries
import pygame
from pygame.draw import *
from random import randint

#creating palette
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

#setting all important variables
score = 0
death = 0
velocity = []
game_over = False

print('Choose the difficulty (easy, medium, hard, insane, impossible): ')
difficulty = str(input())

if difficulty == 'easy':
	velocity = [-100, 100]
elif difficulty == 'medium':
	velocity = [-250, 250]
elif difficulty == 'hard':
	velocity = [-500, 500]
elif difficulty == 'insane':
	velocity = [-750, 750]
elif difficulty == 'impossible':
	velocity = [-1000, 1000]

pygame.init()

#setting FPS and display
FPS = 150
screen = pygame.display.set_mode((1200, 900))

class ball:
    '''This class contains moving balls with its own color, radius, position, and velocity'''
    def init(self):
        '''This function initializes the ball, gives it start velocity, radius, start point, and color'''
        self.x = randint(400, 700)
        self.y = randint(300, 600)
        self.v_x = randint(velocity[0], velocity[1])
        self.v_y = randint(velocity[0], velocity[1])
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

class ring:
	'''This class contains moving rings'''
	def init(self):
		'''This function initializes a ring'''
		self.x = randint(400, 700)
		self.y = randint(300, 600)
		self.v_x = randint(velocity[0], velocity[1])
		self.v_y = randint(velocity[0], velocity[1])
		self.R = randint(20, 50)
		self.r = 0.4 * self.R
		self.color = COLORS[randint(0, 5)]
	
	def draw(self, surface):
		'''This function draws a ring'''
		circle(surface, self.color, (self.x, self.y), self.R)
		circle(surface, BLACK, (self.x, self.y), self.r)
	
	def move(self):
		'''This function moves a ring and allows it to bounce off the walls'''
		if(self.x + self.R > 1200 or self.x - self.R < 0):
			self.v_x *= -1
		if(self.y + self.R > 900 or self.y - self.R < 0):
			self.v_y *= -1
		self.x += self.v_x * 0.01
		self.y += self.v_y * 0.01
	
	def check(self):
		'''This function checks if we caught a ball. If we did, we get new score. If not, we lose'''
		if self.r**2 <= (self.x - event.x)**2 + (self.y - event.y)**2 <= self.R**2:
			print('Congratulations! You caught the ring')
			global score
			score = score + 21 - int(self.R * 0.2)
			print('Your score is', score)
		else:
			global death
			death += 1

list_of_balls = []
list_of_rings = []

for i in range(randint(5, 10)):
	tmp_ball = ball()
	list_of_balls.append(tmp_ball)
	list_of_balls[i].init()

for i in range(randint(3, 8)):
	tmp_ring = ring()
	list_of_rings.append(tmp_ring)
	list_of_rings[i].init()

pygame.display.update()
clock = pygame.time.Clock()
finished = False


while (not finished) and (not game_over):
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished == True
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			finished == True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			event.x = event.pos[0]
			event.y = event.pos[1]
			for i in range(len(list_of_balls)):
				list_of_balls[i].check()
			for i in range(len(list_of_rings)):
				list_of_rings[i].check()
			if death == len(list_of_balls) + len(list_of_rings):
				game_over = True
			else:
				death = 0
				list_of_balls = []
				list_of_rings = []
				for i in range(randint(5, 10)):
					tmp_ball = ball()
					list_of_balls.append(tmp_ball)
					list_of_balls[i].init()
				for i in range(randint(3, 8)):
					tmp_ring = ring()
					list_of_rings.append(tmp_ring)
					list_of_rings[i].init()
	for i in range(len(list_of_balls)):
		list_of_balls[i].draw(screen)
		list_of_balls[i].move()
	for i in range(len(list_of_rings)):
		list_of_rings[i].draw(screen)
		list_of_rings[i].move()
	pygame.display.update()
	screen.fill(BLACK)
pygame.quit()
print('GAME OVER! Your score is', score)
