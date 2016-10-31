
import random

from game_framework import *
from pico2d import *
from Obj_Bullet import *

class Player:
	Move_Stop,Move_Left, Move_Right = 0,1,2
	
	def __init__(self):
		self.p_image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\character1.png')
		self.Sunny = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\sunny.png')
		self.frame = 0
		self.x=100
		self.y = 50
		self.state=self.Move_Stop
		self.speed = 10
		self.damage=1
		
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
		
		self.p_image.clip_draw(self.SunnyFrame * 170, 0, 170, 130, self.x, 50)
		#self.Sunny.clip_draw(self.frame * 128, 0, 128, 130, x, 50)
	
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
	
	def Bullet(self):
		Attack
		

			
