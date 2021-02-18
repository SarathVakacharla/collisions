##Random Collisions

# Import and initialize the pygame library
import pygame
from datetime import date, datetime
import random
import math

from ball import Ball
from constants import *

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

balls = [Ball(i, BALL_RADIUS) for i in range(NUMBER_OF_BALLS)]
balls_pos = None

# Run until the user asks to quit
running = True

while running:	
	# Did the user click the window close button?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Fill the background with white
	screen.fill(BLACK)

	# fps
	screen.blit(font.render(f'FPS: {int(clock.get_fps())}', 1, CORAL), (10,0))

	# balls
	for i in range(len(balls)):
		b = balls[i]
		b.update_pos()
		screen.blit(b.surf, (screen.blit(b.surf, b.pos)))

	# Flip the display
	pygame.display.flip()
	clock.tick(FPS)

# Done! Time to quit.
pygame.quit()