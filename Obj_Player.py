
import random

from game_framework import *
from pico2d import *
from Obj_Bullet import *

Raby, Sunny = 0, 1

class Player:
	PIXEL_PER_METER = (10.0/0.3) #10 pixel 30cm
	RUN_SPEED_KMPH = 20.0
	RUN_SPEED=
	Move_Stop,Move_Left, Move_Right = 0,1,2
	Lev1, Lev2, Lev3 = 0, 1, 2
	Rev1, Rev2, Rev3 = 0, 1, 2
	damage = 1
	GM = None
	L_Hatch=False
	R_Hatch=False
	def __init__(self):
		self.p_image = load_image('D:\\2-2\\2DGP\\Player\\character1.png')
		self.Sunny = load_image('D:\\2-2\\2DGP\\Player\\sunny.png')
		self.LD = load_image('D:\\2-2\\2DGP\\Player\\LD.png')
		self.RD = load_image('D:\\2-2\\2DGP\\Player\\RD.png')
		self.frame = 0
		self.x=100
		self.y = 50
		self.state=self.Move_Stop
		self.speed = 10
		
		
	def update(self):
		self.frame = (self.frame + 1) % 4
		self.SunnyFrame = (self.frame + 1) % 3
		if self.state == self.Move_Stop:
			self.x+=0
		if self.state == self.Move_Right:
			self.x = min(600, self.x+self.speed)
		if self.state == self.Move_Left:
			self.x = max(0, self.x -self.speed)
	
	def draw(self):
		if Player.GM == Raby:
			self.p_image.clip_draw(self.SunnyFrame * 170, 0, 170, 130, self.x, 50)
		elif Player.GM == Sunny:
			self.Sunny.clip_draw(self.frame * 128, 0, 128, 130, self.x, 50)
			
		#if Player.L_Hatch == True:
		if Player.L_Hatch == True:
			self.LD.clip_draw(self.frame * 64, 0, 64, 64, self.x - 64, 50)
			
		if Player.R_Hatch == True:
			self.RD.clip_draw(self.frame * 64, 0, 64, 64, self.x + 64, 50)
	
	def handle_event(self,event):
		if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
			if self.state in (self.Move_Stop, self.Move_Right,):
				self.state = self.Move_Left
		if (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
			if self.state in (self.Move_Stop, self.Move_Left,):
				self.state = self.Move_Right
		
		if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
			if  self.state in (self.Move_Right,):
				self.state = self.Move_Right
			elif self.state in (self.Move_Left, ):
				self.state = self.Move_Stop
		if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
			if  self.state in (self.Move_Left,):
				self.state = self.Move_Left
			elif self.state in (self.Move_Right,):
				self.state = self.Move_Stop
				
	
	def draw_bb(self):
		draw_rectangle(*self.get_bb())

	def get_bb(self):
		return self.x-10, self.y-10,self.x+10,self.y+30
	
	def Bullet(none):
		if Player.damage<3:
			Player.damage +=1
		

			
