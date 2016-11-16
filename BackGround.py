from pico2d import *
 
import game_framework

from Main import *

class BackGround:
	Map1, Map2, Map3 = 0,1,2
	
	
	
	
	def __init__(self):
		self.stage1 = load_image('D:\\2-2\\2DGP\\BackGround\\03.png')
		self.stage2 = load_image('D:\\2-2\\2DGP\\BackGround\\07.png')
		self.stage3 = load_image('D:\\2-2\\2DGP\\BackGround\\12.png')
		self.Cloud1= load_image('D:\\2-2\\2DGP\\BackGround\\cloud_01.png')
		self.Cloud2= load_image('D:\\2-2\\2DGP\\BackGround\\cloud_02.png')
		self.Cloud3 = load_image('D:\\2-2\\2DGP\\BackGround\\cloud_03.png')
		self.Cloudy = load_image('D:\\2-2\\2DGP\\BackGround\\Cloudy1.png')
		
		
		
		#self.Cloud
		#self.Cloud2
		#self.Black_Cloud
		#self.Black_Cloud2
		self.y1 = 0
		self.y2 = 800
		self.CloudY1 = 1536
		self.CloudY2 = 1536
		
		self.BackGround_State = self.Map1
		self.Map2Timer=0
		self.Mapping2=False
		self.Mapping3=False
		
		BackGround.BGM = load_music('logo_background.mp3')
		BackGround.BGM.set_volume(64)
		BackGround.BGM.repeat_play()
		
	def update(self, Map):
		#self.BGM.play()
		
		#if Stage == 0:
		#if Stage ==1:
		#	self.CloudY1 -= 2
		self.y1 -= 10
		self.y2 -= 10
		if (self.y1 == -800):
			self.y1 = 800
		if self.y2 == -800:
			self.y2 = 800
			
		if (Map == self.Map2):
			self.CloudY1 -= 40
			if self.CloudY1 <0:
				self.Mapping2 = True
		if (Map == self.Map3):
			self.CloudY2-=40
			if self.CloudY2<0:
				self.Mapping3=True
	
	
	def draw(self):
		if self.BackGround_State== self.Map1:
			self.stage1.draw_to_origin(0, self.y2, 600, 800)
		elif self.BackGround_State == self.Map2:
			if self.Mapping2 == True:
				self.stage2.draw_to_origin(0, self.y2, 600, 800)
			else:
				self.stage1.draw_to_origin(0, self.y2, 600, 800)
		elif self.BackGround_State == self.Map3:
			if self.Mapping3 == True:
				self.stage3.draw_to_origin(0, self.y2, 600, 800)
			else:
				self.stage2.draw_to_origin(0, self.y2, 600, 800)
			
	def draw2(self):
		if self.BackGround_State == self.Map1:
			self.stage1.draw_to_origin(0, self.y1, 600, 800)
		elif self.BackGround_State == self.Map2:
			if self.Mapping2 == True:
				self.stage2.draw_to_origin(0, self.y1, 600, 800)
			else:
				self.stage1.draw_to_origin(0, self.y1, 600, 800)
		elif self.BackGround_State == self.Map3:
			if self.Mapping3 == True:
				self.stage3.draw_to_origin(0, self.y1, 600, 800)
			else:
				self.stage2.draw_to_origin(0, self.y1, 600, 800)
			
	def drawCloud(self, Map):
		if Map == self.Map2:
			self.Cloudy.draw_to_origin(0, self.CloudY1, 600, 1536)
		elif Map==self.Map3:
			self.Cloudy.draw_to_origin(0, self.CloudY2, 600, 1536)
			
		#elif Map == self.Map3:
		#	self.Cloudy.draw_to_origin(0, self.CloudY1, 600, 1536)
	def handle_event(self, event):
		if event.key == SDLK_1:
			self.BackGround_State= BackGround.Map1
		if event.key == SDLK_2:
			self.BackGround_State= BackGround.Map2
		if event.key == SDLK_3:
			self.BackGround_State= BackGround.Map3
			
	def MapLevel(self,Level):
		self.BackGround_State = Level