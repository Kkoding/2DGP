from pico2d import *

import game_framework

import Main

class Monster:
	def __init__(self):
		self.Mon1=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\Mon1.png')
		self.SizeOfMobX = 300
		self.SizeOfMobY = 800
		self.y = self.SizeOfMobY
		self.x = self.SizeOfMobX
		self.MonFrame=0
		self.MonHp=14
		self.Hp0=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\0.png')
		self.Hp1=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\1.png')
		self.Hp2=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\2.png')
		self.Hp3=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\3.png')
		self.Hp4=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\4.png')
		self.Hp5=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\5.png')
		self.Hp6=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\6.png')
		self.Hp7=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\7.png')
		self.Hp8=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\8.png')
		self.Hp9=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\9.png')
		self.Hp10=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\10.png')
		self.Hp11=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\11.png')
		self.Hp12=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\12.png')
		self.Hp13=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\13.png')
		self.Hp14=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\14.png')
	def update(self ):
		self.MonFrame =(self.MonFrame +1) % 4
		self.y -=10
	
	def draw(self):
		self.Mon1.clip_draw(180*self.MonFrame,0,180,120,self.x,self.y)
		
	def draw_bb(self):
		draw_rectangle(*self.get_bb())
	
	def draw_bb(self):
		draw_rectangle(*self.get_bb())
			
	def get_bb(self):
		return self.x -60, self.y-60,self.x +60,self.y+20