from pico2d import *
from Obj_Player import *
from Collision import*
import Main

class Attack:
	def __init__(self):
		self.b_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_sunny.png')
		self.bX =100
		self.bY = 50
		self.Drawing = False
		self.YSpeed = 22
	
	def update(self,xPos):
		if self.Drawing == False:
			self.bX = xPos
			self.bY = 50
		if self.Drawing == True:
			self.bY += self.YSpeed
			if self.bY > 800:
				self.Drawing = False
				self.bY = 50
				self.bX = 100
	
	def draw(self):
		if self.Drawing == True:
			self.b_image.clip_draw(0, 0, 64, 64, self.bX, self.bY)
	
	def collide(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb()
		left_b, bottom_b, right_b, top_b = self.get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	def draw_bb(self):
		if self.Drawing == True:
			draw_rectangle(*self.get_bb())

	def get_bb(self):
		return self.bX -10, self.bY-10,self.bX +10,self.bY+20
	
	