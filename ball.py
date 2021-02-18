import pygame
import math
import random
from pygame.event import post
from constants import *
from util import *

# Define a Ball object by extending pygame.sprite.Sprite
class Ball(pygame.sprite.Sprite):
	def __init__(self, id, radius, pos=None, angle=None):
		super(Ball, self).__init__()
		self.id = id
		self.radius = radius
		self.pos = pos
		self.angle = angle # degrees
		self.surf = pygame.Surface((self.radius*2, self.radius*2))
		self.surf.set_colorkey(BLACK)
		self.surf.fill(BLACK)
		self.rect = self.surf.get_rect()
		
		#random color - random.choice(list(pygame.color.THECOLORS.values()))
		pygame.draw.circle(self.surf, pygame.Color(f'grey{random.choice(range(80,99))}'), (self.radius, self.radius), self.radius)

	def update_pos(self):
		
		if not self.pos or not self.angle:
			random_pos_dir = get_random_pos_dir()
			self.pos = random_pos_dir[0]
			self.angle = random_pos_dir[1]
		else:
			# current pos and direction (angle)
			current_x = self.pos[0]
			current_y = self.pos[1]
			current_angle = self.angle

			# Detect collisions with walls
			if current_x >= (SCREEN_WIDTH-(2*BALL_RADIUS)) or current_x <= 0 or current_y >= (SCREEN_HEIGHT-(2*BALL_RADIUS)) or current_y <= 0:
				#print(f'Angle:before:{current_angle}')
				# TODO: Fix reflection angle
				self.angle = ((current_angle+90) % 360)
				#print(f'Angle:after:{self.angle}')

			#TODO: detect collisions with other balls

			# Move the ball
			self.pos[0] += math.cos(math.radians(self.angle)) * VELOCITY
			self.pos[1] += math.sin(math.radians(self.angle)) * VELOCITY
