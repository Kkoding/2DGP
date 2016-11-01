from pico2d import *

import game_framework

import Main


class Boss:
	def __init__(self):
		self.Boss_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime.png')
		self.Slime_Die_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime die.png')
		self.BossHpImage =load_image('D:\\2-2\\2DGP\\Monster\\Boss\\boss_hp.png')
		self.Stone_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\Stone.png')
		self.Boss_YPos = 1000
		self.Boss_XPos = 300
		self.BYPos = self.Boss_YPos
		self.BXPos = self.Boss_XPos
		self.Bframe = 0
		self.FlagBossHp=False
		
		self.Boss_Bullet = load_image('D:\\2-2\\2DGP\\Monster\\bullet_boss.png')
		self.Count1=0
		self.BulletX=300
		self.BulletY=700
		
		self.SlimeHp = 12
		self.StoneHp = 12
		
		self.imagetimer=0
	
	def update(self):
		self.imagetimer+=1
		if self.imagetimer % 2 == 0:
			self.Bframe = (self.Bframe + 1) % 4
		if self.BYPos > 680:
			self.BYPos -= 10
		if self.Count1 <100:
			self.Count1+=1
		if self.Count1==100:
			self.BulletX-=10
			self.BulletY-=10
	
	def draw(self,BossNum):
		if BossNum == 0:
			if self.SlimeHp>=0:
				self.Boss_image.clip_draw(300 * self.Bframe, 0, 300, 256, self.BXPos, self.BYPos)
			elif self.SlimeHp<0:
				self.Slime_Die_image.clip_draw(0, 0, 300, 256, self.BXPos, self.BYPos)
		elif BossNum==1:
			if self.StoneHp>0:
				self.Stone_image.clip_draw(256*self.Bframe,0,256,205, self.BXPos, self.BYPos)
		if self.FlagBossHp == True:
			self.BossHpImage.clip_draw(0, 0, self.SlimeHp * 100, 25, 0, 790)
	
	def BossLevel(self):
		if self.SlimeHp>0:
			return 0
		elif self.StoneHp>0:
			self.FlagBossHp=False
			return 1
		
			
	def drawShot(self,Num):
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BulletX + Num*10, self.BulletY)
		
	def draw_bb(self):
		draw_rectangle(*self.get_bb())
	
	def get_bb(self):
		return self.BXPos - 120 , self.BYPos - 120, self.BXPos + 120, self.BYPos + 20
	
	def getHp(self,damage):
		if self.SlimeHp>0:
			self.SlimeHp-= damage
		
	#def Patter1(self):
		
		
		