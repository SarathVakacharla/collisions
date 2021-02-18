import random
from constants import *

def get_random_pos_dir():
	return [[random.randint(BALL_RADIUS,SCREEN_WIDTH-BALL_RADIUS), random.randint(BALL_RADIUS,SCREEN_HEIGHT-BALL_RADIUS)], random.randint(0, 360)]