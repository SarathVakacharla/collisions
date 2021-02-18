import pygame
import random

# Constants
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = pygame.Color("red")
CORAL = pygame.Color("coral")

# simulation parameters
FPS = 30
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_RADIUS = 10
NUMBER_OF_BALLS = random.randint(30, 50)
VELOCITY = 5