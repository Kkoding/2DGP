
import random


from game_framework import *
from pico2d import *
from Obj_Bullet import *
from Obj_Monster import *

Raby, Sunny = 0, 1

class Player:
	PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
	RUN_SPEED_KMPH = 80.0  # Km / Hour
	RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
	RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
	RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
	
	TIME_PER_ACTION = 0.5
	ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
	FRAMES_PER_ACTION = 8
	
	Move_Stop,Move_Left, Move_Right = 0,1,2
	Lev1, Lev2, Lev3 = 0, 1, 2
	Rev1, Rev2, Rev3 = 0, 1, 2
	
	damage = 1
	GM = None
	L_Hatch=False
	R_Hatch=False
	Protect=False
	Money = 10
	def __init__(self):
		self.p_image = load_image('Player\\character1.png')
		self.Sunny = load_image('Player\\sunny.png')
		self.LD = load_image('Player\\LD.png')
		self.RD = load_image('Player\\RD.png')
		self.frame = 0
		self.x=100
		self.y = 50
		self.state=self.Move_Stop
		self.speed = 10
		#self.Money=0
		self.value=0
		#self.bgm = load_music('logo_background.mp3')
		#self.bgm.set_volume(64)
		#self.bgm.play(1)
		self.Coins = load_image('etc\\item_coin.png')
		self.num = load_image('etc\\numbers.png')
		self.Protect_image = load_image('Player\\protect_missile.png')
		
		
		
	def __del__(self):
		del self.p_image
		del self.Sunny
		del self.LD
		del self.RD
		del self.Coins
		del self.num
		del self.Protect_image
		
		
		#del self.bgm
	
	def update(self):
		self.frame = (self.frame + 1) % 4
		self.SunnyFrame = (self.frame + 1) % 3
		if self.state == self.Move_Stop:
			self.x+=0
		elif self.state == self.Move_Right:
			self.x = min(600, self.x+self.speed)
		elif self.state == self.Move_Left:
			self.x = max(0, self.x -self.speed)
	
	def draw(self):
		if Player.Protect==True:
			self.Protect_image.clip_draw(0, 0, 200, 200, self.x, 50)
			
		#self.value=self.Money
		self.Coins.clip_draw(0, 0, 64, 64, 450-64, 750, 64, 64)
		# self.num.clip_draw(0,0,64,64,450+64+32*(self.Money/10),750,64,64)
		if Player.Money > 99:
			Player.Money=99
		if Player.Money == 99:
			self.num.clip_draw(64 * 9, 0, 64, 64, 450 + 32 + 16, 750, 64, 64)
			self.num.clip_draw(64*9, 0, 64, 64, 450 + 64 + 32, 750, 64, 64)
			self.num.clip_draw(64 * 9, 0, 64, 64, 450  , 750, 64, 64)
		elif Player.Money < 10:
			self.num.clip_draw(64 * (Player.Money % 10), 0, 64, 64, 450 + 32+16 , 750, 64, 64)
			self.num.clip_draw(0, 0, 64, 64, 450 + 64 + 32, 750, 64, 64)
		elif Player.Money >=10 and Player.Money < 99:
			if Player.Money >=10 and Player. Money <20:
				self.num.clip_draw(64, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=20 and Player.Money <30:
				self.num.clip_draw(64*2, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=30 and Player.Money <40:
				self.num.clip_draw(64*3, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=40 and Player.Money <50:
				self.num.clip_draw(64*4, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=50 and Player.Money <60:
				self.num.clip_draw(64*5, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=60 and Player.Money <70:
				self.num.clip_draw(64*6, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=70 and Player.Money <80:
				self.num.clip_draw(64*7, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=80 and Player.Money <90:
				self.num.clip_draw(64*8, 0, 64, 64, 450 , 750, 64, 64)
			elif Player.Money >=90:
				self.num.clip_draw(64*9, 0, 64, 64, 450 , 750, 64, 64)
				
			self.num.clip_draw(64 * (self.Money % 10), 0, 64, 64, 450 + 32 + 16, 750, 64, 64)
			self.num.clip_draw(0, 0, 64, 64, 450 + 64 + 32, 750, 64, 64)
			pass
		
		if Player.GM == Raby:
			self.p_image.clip_draw(self.SunnyFrame * 170, 0, 170, 130, self.x, 50)
		elif Player.GM == Sunny:
			self.Sunny.clip_draw(self.frame * 128, 0, 128, 130, self.x, 50)
		if Player.L_Hatch == True:
			self.LD.clip_draw(self.frame * 64, 0, 64, 64, self.x - 64, 50)
		if Player.R_Hatch == True:
			self.RD.clip_draw(self.frame * 64, 0, 64, 64, self.x + 64, 50)
		
		
		
		
	def handle_event(self,event):
		if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
			if self.state in (self.Move_Stop, self.Move_Right,):
				self.state = self.Move_Left
		elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
			if self.state in (self.Move_Stop, self.Move_Left,):
				self.state = self.Move_Right
		
		if (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
			if  self.state in (self.Move_Right,):
				self.state = self.Move_Right
			elif self.state in (self.Move_Left, ):
				self.state = self.Move_Stop
		elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
			if  self.state in (self.Move_Left,):
				self.state = self.Move_Left
			elif self.state in (self.Move_Right,):
				self.state = self.Move_Stop
	
	def collide(self, a):
		left_a, bottom_a, right_a, top_a = a.C_get_bb()
		left_b, bottom_b, right_b, top_b = self.get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	def collide2(self, a):
		left_a, bottom_a, right_a, top_a = a.get_bb()
		left_b, bottom_b, right_b, top_b = self.get_bb()
		
		if left_a > right_b: return False
		if right_a < left_b: return False
		if top_a < bottom_b: return False
		if bottom_a > top_b: return False
		
		return True
	
	
	def draw_bb(self):
		draw_rectangle(*self.get_bb())

	def get_bb(self):
		return self.x-10, self.y-10,self.x+10,self.y+30
	
	def Bullet(none):
		if Player.damage<3:
			Player.damage +=1
		

			
