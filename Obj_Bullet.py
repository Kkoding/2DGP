from pico2d import *

from Obj_Player import *
from Collision import*
import main_state

class Attack:
	
	Lev1, Lev2, Lev3 = 0, 1, 2
	Rev1, Rev2, Rev3 = 0, 1, 2
	Gun_Sound=None
	def __init__(self):
		self.b1_image = load_image('Player\\bullet_sunny.png')
		self.b2_image = load_image('Player\\bullet_sunny_two.png')
		self.b3_image = load_image('Player\\bullet_sunny_three.png')
		
		self.r1_image = load_image('Player\\bullet_raby.png')
		self.r2_image = load_image('Player\\bullet_raby_two.png')
		self.r3_image = load_image('Player\\bullet_raby_three.png')
		
		self.LD = load_image('bullet_02_01.png')
		self.RD = load_image('hatzling_03_01.png')
		
		if Attack.Gun_Sound == None:
			Attack.Gun_Sound = load_wav('missile_show.wav')
			Attack.Gun_Sound.set_volume(32)
		
		self.bX =100
		self.bY = 50
		self.Y2=50
		self.Y3=50
		self.Drawing = False
		self.SDrawing = False
		self.YSpeed = 22
		
	#	self.Shot_sound = load_wav('D:\\2-2\\2DGP\\Sound\\missile_show.wav')
	#	self.Shot_sound.set_volume(64)
	#	self.Shot_sound.repeat_play()
	
	def __del__(self):
		del self.b1_image
		del self.b2_image
		del self.b3_image
		del self.r1_image
		del self.r2_image
		del self.r3_image
		del self.LD
		del self.RD
		
		
		
	def update(self,xPos):
	#	self.Shot_sound.play()
		self.Gun_Sound.play()
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
			elif damage == 2:
				if self.Drawing == True:
					self.b2_image.clip_draw(0, 0, 129, 129, self.bX, self.bY)
			elif damage == 3:
				if self.Drawing == True:
					self.b3_image.clip_draw(0, 0, 128, 128, self.bX, self.bY)
		else:
			if damage == 1:
				if self.Drawing == True:
					self.r1_image.clip_draw(0, 0, 64, 64, self.bX, self.bY)
			elif damage == 2:
				if self.Drawing == True:
					self.r2_image.clip_draw(0, 0, 101, 93, self.bX, self.bY)
			elif damage == 3:
				if self.Drawing == True:
					self.r3_image.clip_draw(0, 0, 129, 125, self.bX, self.bY)
	
	def Sub_Update(self,xPos):
			if self.Drawing == False:
				self.bX = xPos
				self.Y2 = 50
			elif self.Drawing == True:
				self.Y2 += self.YSpeed
				if self.Y2 > 800:
					self.Drawing = False
					self.Y2 = 50
					self.bX = 100
	
	def Sub_Update2(self,xPos):
		if self.Drawing == False:
			self.bX = xPos
			self.Y3 = 50
		elif self.Drawing == True:
			self.Y3 += self.YSpeed
			if self.Y3 > 800:
				self.Drawing = False
				self.Y3 = 50
				self.bX = 100
				
		
	def RSub_draw(self,RB):
		if RB == True:
			if self.Drawing == True:
				self.RD.clip_draw(0, 0, 64, 64, self.bX + 64, self.Y2 + 32)
				#self.RSub_draw_bb()
		
	def LSub_draw(self,LB):
		if LB == True:
			if self.Drawing == True:
				self.LD.clip_draw(0, 0, 64, 64, self.bX - 64, self.Y3 + 32)
				#self.LSub_draw_bb()
	
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
		return self.bX -15, self.bY-10,self.bX +15,self.bY+20
	
	def Rcollide(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb()
		left_b, bottom_b, right_b, top_b = self.RSub_get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	def Lcollide(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb()
		left_b, bottom_b, right_b, top_b = self.LSub_get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	def LSub_draw_bb(self):
		if self.Drawing == True:
			draw_rectangle(*self.LSub_get_bb())
			
	def RSub_draw_bb(self):
		if self.Drawing == True:
			draw_rectangle(*self.RSub_get_bb())
			
	def RSub_get_bb(self):
		return self.bX +55, self.Y2+20,self.bX +75,self.Y2+40
	
	def LSub_get_bb(self):
		return self.bX -75, self.Y3+20,self.bX -55,self.Y3+40

	
	