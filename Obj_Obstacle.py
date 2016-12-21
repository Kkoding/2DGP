from pico2d import *

import game_framework

import main_state


class Obstacle:
	def __init__(self):
		#meteo 떨어진다.
		self.warning  = load_image ('D:\\2-2\\2DGP\\object\\warn_line.png')
		self.warning_mark = load_image ('D:\\2-2\\2DGP\\object\\warn_makr.png')
		self.meteo = load_image ('D:\\2-2\\2DGP\\object\\meteo.png')
		
		
	def draw_meteo(self):
		self.warning.draw_to_origin(150,150,32,256)
	
	