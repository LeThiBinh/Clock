import pygame, sys
import datetime
from math import*


pygame.init() 
WIDTH, HEIGHT = 900, 600
center =(WIDTH/2 , HEIGHT/2)
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("Vu-Tru1.jpeg")
WHITE =(255,255,255 )
BLACK =(0,0,0)
RED =(255,0,0)

def numbers(number, position):
	font = pygame.font.SysFont("Castellar", 25, True, False )
	text = font.render(number, True, WHITE)
	screen.blit(text, position)

def convert(R,theta):
	y = R*cos(pi*theta/180)
	x = R*sin(pi*theta/180)
	return x + 450 -10 , -(y - 300) -10


running = True
while running:

	screen.fill((BLACK))
	screen.blit(background,(0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	current_time = datetime.datetime.now()
	second = current_time.second
	minute = current_time.minute
	hour = current_time.hour

	#pygame.draw.circle(screen, (227, 229, 228), center, 160, 4)
	pygame.draw.circle(screen, WHITE, center, 8)


	for number in range(1, 13):
		#numbers(str(number), 20, convert(130, number*30))
		numbers(str(number), convert(140, number*30))

	#Hour
	R = 110
	theta = (hour + minute /60 + second /3600) *(360 /12)
	pygame.draw.line(screen, WHITE, center, convert(R,theta),8)
	#Minute
	R = 135
	theta = (minute + second /60) *(360 /60)
	pygame.draw.line(screen, WHITE, center, convert(R,theta),5)
	# Second	
	R = 140
	theta =second * (360/60)
	pygame.draw.line(screen,(RED), center, convert(R, theta),3)
	
	clock.tick(FPS)
	pygame.display.flip()
	pygame.display.update()

pygame.quit()
sys.exit()