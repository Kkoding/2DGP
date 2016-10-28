from pico2d import *

import game_framework

from Main import *

class BackGround:
	Map1, Map2, Map3 = 0,1,2
	
	def __init__(self):
		self.stage1 = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\03.png')
		self.stage2 = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\99.png')
		self.stage3 = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\12.png')
		#self.Cloud
		#self.Cloud2
		#self.Black_Cloud
		#self.Black_Cloud2
		self.y1 = 0
		self.y2 = 800
		self.BackGround_State = self.Map3
	def update(self):
		self.y1 -= 10
		self.y2 -= 10
		if (self.y2 == 0):
			self.y1 = 0
			self.y2 = 800
	
	def draw(self):
		if self.BackGround_State== self.Map1:
			self.stage1.draw_to_origin(0, self.y2, 600, 800)
		elif self.BackGround_State == self.Map2:
			self.stage2.draw_to_origin(0, self.y2, 600, 800)
		elif self.BackGround_State == self.Map3:
			self.stage3.draw_to_origin(0, self.y2, 600, 800)
			
	def draw2(self):
		if self.BackGround_State == self.Map1:
			self.stage1.draw_to_origin(0, self.y1, 600, 800)
		elif self.BackGround_State == self.Map2:
			self.stage2.draw_to_origin(0, self.y1, 600, 800)
		elif self.BackGround_State == self.Map3:
			self.stage3.draw_to_origin(0, self.y1, 600, 800)
	
	def handle_event(self, event):
		if event.key == SDLK_1:
			self.BackGround_State= BackGround.Map1
		if event.key == SDLK_2:
			self.BackGround_State= BackGround.Map2
		if event.key == SDLK_3:
			self.BackGround_State= BackGround.Map3