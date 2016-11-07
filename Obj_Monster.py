from pico2d import *

import game_framework

import Main

class Monster:
	
	Mon1, BlueMonster, PinkMonster,RedMonster = 0,1,2,3
	Limit=4
	def __init__(self,i):
		self.Mon1=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\Mon1.png')
		self.Yellow = load_image('D:\\2-2\\2DGP\\Monster\\Mon\\Yellow.png')
		
		self.SizeOfMobX = 70 + (155 * (i % 4))
		if i<self.Limit:
			self.SizeOfMobY = 1350
		elif i>=self.Limit and i<self.Limit*2:
			self.SizeOfMobY = 1350 + 400
		elif i>=self.Limit*2:
			self.SizeOfMobY = 1350 + 450*2
			
		self.y = self.SizeOfMobY
		self.x = self.SizeOfMobX
		self.MonFrame=0
		self.MonYFrame=0
		self.MonHp=0
		self.Hp0=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\0.png')
		self.Hp1=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\1.png')
		self.Hp2=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\2.png')
		self.Hp3=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\3.png')
		self.Hp4=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\4.png')
		self.Hp5=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\5.png')
		self.Hp6=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\6.png')
		self.Hp7=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\7.png')
		self.Hp8=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\8.png')
		self.Hp9=load_image ('D:\\2-2\\2DGP\\Monster\\Mon\\9.png')
		self.Hp10=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\10.png')
		self.Hp11=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\11.png')
		self.Hp12=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\12.png')
		self.Hp13=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\13.png')
		self.Hp14=load_image('D:\\2-2\\2DGP\\Monster\\Mon\\14.png')
		
		
		
		self.Damaged=False
		
	def update(self,Map):
		self.MonFrame =(self.MonFrame +1) % 4
		self.y -= 10
	
	def Damege(self,num):
		self.MonHp += num
	
	def draw(self,Map):
		if self.MonHp<14:
			if Map == 0:
				self.Mon1.clip_draw(180*self.MonFrame,0,180,120,self.SizeOfMobX,self.y)
			elif Map == 1:
				self.Yellow.clip_draw(180 * self.MonFrame, 0, 180, 120, self.SizeOfMobX, self.y)
		if self.Damaged == True:
			self.drawHp(self.MonHp)
		#self.Mon1.clip_draw(180 * self.MonFrame, 0, 180, 120, self.SizeOfMobX+155*i, self.y)
		#self.Mon1.clip_draw(180 * self.MonFrame, 0, 180, 120, self.SizeOfMobX+155*2, self.y)
		#self.Mon1.clip_draw(180 * self.MonFrame, 0, 180, 120, self.SizeOfMobX+155*3, self.y)
			
	def drawHp(self,hp):
		if hp == 0:
			self.Hp0.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==1:
			self.Hp1.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==2:
			self.Hp2.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==3:
			self.Hp3.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==4:
			self.Hp4.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==5:
			self.Hp5.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==6:
			self.Hp6.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==7:
			self.Hp7.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==8:
			self.Hp8.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==9:
			self.Hp9.clip_draw(0, 0, 132, 27, self.x, self.y - 60)
		elif hp==10:
			self.Hp10.clip_draw(0, 0, 132, 27, self.x, self.y -60)
		elif hp==11:
			self.Hp11.clip_draw(0, 0, 132, 27, self.x, self.y -60)
		elif hp==12:
			self.Hp12.clip_draw(0, 0, 132, 27, self.x, self.y -60)
		elif hp==13:
			self.Hp13.clip_draw(0, 0, 132, 27, self.x, self.y -60)
		elif hp==14:
			self.y= -350
			self.Hp14.clip_draw(0, 0, 132, 27, self.x, self.y -60)
	
	def collide(self, a):
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
		return self.x -60, self.y-60,self.x +60,self.y+20