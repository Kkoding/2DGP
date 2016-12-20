from pico2d import *
from Obj_Player import *
from Collision import*
import Main

class Attack:
	
	Lev1, Lev2, Lev3 = 0, 1, 2
	Rev1, Rev2, Rev3 = 0, 1, 2
	
	def __init__(self):
		self.b1_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_sunny.png')
		self.b2_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_sunny_two.png')
		self.b3_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_sunny_three.png')
		
		self.r1_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_raby.png')
		self.r2_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_raby_two.png')
		self.r3_image = load_image('D:\\2-2\\2DGP\\Player\\bullet_raby_three.png')
		
		self.LD = load_image('D:\\2-2\\2DGP\\bullet_02_01.png')
		self.RD = load_image('D:\\2-2\\2DGP\\hatzling_03_01.png')
		
		self.bX =100
		self.bY = 50
		self.Y2=50
		
		self.Drawing = False
		self.SDrawing = False
		self.YSpeed = 22
		
	#	self.Shot_sound = load_wav('D:\\2-2\\2DGP\\Sound\\missile_show.wav')
	#	self.Shot_sound.set_volume(64)
	#	self.Shot_sound.repeat_play()
		
	def update(self,xPos):
	#	self.Shot_sound.play()
		if self.Drawing == False:
			self.bX = xPos
			self.bY = 50
		if self.Drawing == True:
			self.bY += self.YSpeed
			if self.bY > 800:
				self.Drawing = False
				self.bY = 50
				self.bX = 100
	
	def draw(self,damage,character):
		if(character == 0):
			if damage == 1:
				if self.Drawing == True:
					self.b1_image.clip_draw(0, 0, 64, 64, self.bX, self.bY)
			if damage == 2:
				if self.Drawing == True:
					self.b2_image.clip_draw(0, 0, 129, 129, self.bX, self.bY)
			if damage == 3:
				if self.Drawing == True:
					self.b3_image.clip_draw(0, 0, 128, 128, self.bX, self.bY)
		else:
			if damage == 1:
				if self.Drawing == True:
					self.r1_image.clip_draw(0, 0, 64, 64, self.bX, self.bY)
			if damage == 2:
				if self.Drawing == True:
					self.r2_image.clip_draw(0, 0, 101, 93, self.bX, self.bY)
			if damage == 3:
				if self.Drawing == True:
					self.r3_image.clip_draw(0, 0, 129, 125, self.bX, self.bY)
	
	def Sub_Update(self,xPos):
		if self.Drawing == False:
			self.bX = xPos
			self.Y2 = 50
		if self.Drawing == True:
			self.Y2 += self.YSpeed
			if self.Y2 > 800:
				self.Drawing = False
				self.Y2 = 50
				self.bX = 100
				
		
	def Sub_draw(self,LB,RB):
		if LB == True:
			if self.Drawing == True:
				self.LD.clip_draw(0, 0, 64, 64, self.bX - 64, self.Y2 + 32)
		if RB == True:
			if self.Drawing == True:
				self.RD.clip_draw(0, 0, 64, 64, self.bX + 64, self.Y2 + 32)
	
	def collide(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb()
		left_b, bottom_b, right_b, top_b = self.get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	def collide2(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb2()
		left_b, bottom_b, right_b, top_b = self.get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	def collide3(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb3()
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
	
	