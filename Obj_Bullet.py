from pico2d import *
from Obj_Player import *

import Main

class Attack:
	def __init__(self):
		self.b_image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\bullet_sunny.png')
		self.bX =100
		self.bY = 50
		self.Drawing = False
		self.YSpeed = 22
	
	def update(self,xPos):
		if self.Drawing == False:
			self.bX = xPos
		if self.Drawing == True:
			
			self.bY += self.YSpeed
			if self.bY > 800:
				self.Drawing = False
				self.bY = 50
				self.bX = 100
	
	def draw(self):
		if self.Drawing == True:
			self.b_image.clip_draw(0, 0, 64, 64, self.bX, self.bY)
			
	def draw_bb(self):
		if self.Drawing == True:
			draw_rectangle(*self.get_bb())

	def get_bb(self):
		return self.bX -10, self.bY-10,self.bX +10,self.bY+20
	