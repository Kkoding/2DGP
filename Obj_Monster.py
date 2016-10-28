from pico2d import *

import game_framework

import Main


class Monster:
	def __init__(self):
		self.image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Boss\\slime.png')
		self.Mon1=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\Mon1.png')
		self.Boss_Pos=1000
		self.SizeOfMobX = 300
		self.SizeOfMobY = 800
		self.y = self.SizeOfMobY
		self.x = self.SizeOfMobX
		self.Bframe = 0
		self.MonFrame=0
	def update(self):
		self.Bframe = (self.Bframe + 1) % 4
		self.MonFrame =(self.MonFrame +1) % 4
		if self.Boss_Pos>680:
			self.Boss_Pos-=10
		self.y -=10
	
	def draw(self):
		self.Mon1.clip_draw(180*self.MonFrame,0,180,120,self.x,self.y)
		self.image.clip_draw(300*self.Bframe,0, 300,256, 300,self.Boss_Pos)
		
	def draw_bb(self):
		draw_rectangle(*self.get_bb())

	def get_bb(self):
		return self.x -60, self.y-60,self.x +60,self.y+20