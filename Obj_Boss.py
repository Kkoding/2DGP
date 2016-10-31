from pico2d import *

import game_framework

import Main


class Boss:
	def __init__(self):
		self.Boss_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime.png')
		self.Slime_Die_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime die.png')
		self.BossHpImage =load_image('D:\\2-2\\2DGP\\Monster\\Boss\\boss_hp.png')
		self.Boss_YPos = 1000
		self.Boss_XPos = 300
		self.BYPos = self.Boss_YPos
		self.BXPos = self.Boss_XPos
		self.Bframe = 0
		self.FlagBossHp=False
		self.BossHp=12
		self.Boss_Bullet = load_image('D:\\2-2\\2DGP\\Monster\\bullet_boss.png')
		self.Count1=0
		self.BulletX=300
		self.BulletY=700
		
	
	def update(self):
		self.Bframe = (self.Bframe + 1) % 4
		if self.BYPos > 680:
			self.BYPos -= 10
		if self.Count1 <100:
			self.Count1+=1
		if self.Count1==100:
			self.BulletX-=10
			self.BulletY-=10
	
	def draw(self):
		if self.BossHp>=0:
			self.Boss_image.clip_draw(300 * self.Bframe, 0, 300, 256, self.BXPos, self.BYPos)
		elif self.BossHp<0:
			self.Slime_Die_image.clip_draw(0, 0, 300, 256, self.BXPos, self.BYPos)
		if self.FlagBossHp==True:
			self.BossHpImage.clip_draw(0,0,self.BossHp*100,25,0,790)
		
			
	def drawShot(self,Num):
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BulletX + Num*10, self.BulletY)
		
	def draw_bb(self):
		draw_rectangle(*self.get_bb())
	
	def get_bb(self):
		return self.BXPos - 120 , self.BYPos - 120, self.BXPos + 120, self.BYPos + 20
	
	def getHp(self,damage):
		self.BossHp-= damage
		
	#def Patter1(self):
		
		
		