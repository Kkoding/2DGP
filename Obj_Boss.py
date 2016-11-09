from pico2d import *

import game_framework

import Main


class Boss:
	Map1, Map2, Map3 = 0, 1,2
	Boss1, Boss2, Boss3 = 10,11,22
	def __init__(self,select):
		if select==0:
			self.Boss=self.Boss1
			self.Boss_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime.png')
			self.Slime_Die_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\slime die.png')
		
		elif select==1:
			self.Boss = self.Boss2
			self.Stone_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\Stone.png')
			self.Stone_Die_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\StoneDie.png')
		elif (select == 2):
			self.Boss=self.Boss3
			self.Reds_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\Reds.png')
			self.Red_Die_image = load_image('D:\\2-2\\2DGP\\Monster\\Boss\\Reds die.png')
			
		
		
		self.BossHpImage =load_image('D:\\2-2\\2DGP\\Monster\\Boss\\boss_hp.png')
		self.Boss_YPos = 3000
		self.Boss_XPos = 300
		self.BYPos = self.Boss_YPos
		self.BXPos = self.Boss_XPos
		self.SYPos = self.Boss_YPos
		self.RYPos = self.Boss_YPos
		self.Bframe = 0
		self.FlagBossHp=False
		
		self.Boss_Bullet = load_image('D:\\2-2\\2DGP\\Monster\\bullet_boss.png')
		self.BulletX=30
		self.BulletY=700
		
		self.SlimeHp = 12
		self.StoneHp = 12
		
		self.imagetimer=0
		self.ChangeScene=0
		self.ChangeScene2 = 0
		self.Change2=False
	def update(self,Map):
		self.imagetimer+=1
		if self.imagetimer % 2 == 0:
			self.Bframe = (self.Bframe + 1) % 4
		#보스 내랴오는것
		if Map == 0:
			if self.BYPos > 680:
				self.BYPos -= 10
		elif Map == 1:
			if self.SYPos>680:
				self.SYPos-=10
		elif Map == 2:
			if self.RYPos>680:
				self.RYPos-=10
		
		#구름띄울떄필요함
		if self.SlimeHp <= 0 and self.ChangeScene <45:
			self.ChangeScene+=1
			
		if Map==1 and self.SlimeHp<0:
			if self.ChangeScene2 <45:
				self.ChangeScene2+=1
		
	def draw(self,BossNum):
		if  self.Boss == self.Boss1:
			if self.SlimeHp>=0:
				self.Boss_image.clip_draw(300 * self.Bframe, 0, 300, 256, self.BXPos, self.BYPos)
			else:
				self.Slime_Die_image.clip_draw(0, 0, 300, 256, self.BXPos, self.BYPos)
		elif self.Boss == self.Boss2:
			if (self.SlimeHp>=0):
				self.Stone_image.clip_draw(256*self.Bframe,0,256,205, self.BXPos, self.SYPos)
				#print("%d",self.SlimeHp)
			else:
				if self.ChangeScene2 < 45:
					self.Stone_Die_image.clip_draw(0, 0, 256, 205, self.BXPos, self.SYPos)
				else:
					self.Change2 = True
		elif self.Boss==self.Boss3:
			if self.SlimeHp>=0:
				self.Reds_image.clip_draw(512*self.Bframe%4,0,512,512,self.BXPos,self.RYPos)
			else:
				self.Red_Die_image.clip_draw(0, 0, 500, 485, self.BXPos, self.RYPos )
				
		if self.FlagBossHp == True:
			self.BossHpImage.clip_draw(0, 0, self.SlimeHp * 100, 25, 0, 790)
	
	def BossLevel(self):
		if self.SlimeHp>0:
			return 0
		elif self.StoneHp>0:
			if self.SlimeHp <= 0:
				if self.ChangeScene <45:
					return 0
				else:
					return 1
		elif self.SlimeHp <= 0:
			if self.ChangeScene2 < 45:
				return 1
			else:
				return 2
			
	def drawShot(self,Num):
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BulletX + Num*10, self.BulletY)
		
	def draw_bb(self):
		draw_rectangle(*self.get_bb())
	
	def get_bb(self):
		return self.BXPos - 120 , self.BYPos - 120, self.BXPos + 120, self.BYPos + 20
	
	def draw_bb2(self):
		draw_rectangle(*self.get_bb2())
	
	def get_bb2(self):
		return self.BXPos - 120, self.SYPos - 90, self.BXPos + 120, self.SYPos + 30
	
	def draw_bb3(self):
		draw_rectangle(*self.get_bb2())
	
	def get_bb3(self):
		return self.BXPos - 120, self.RYPos - 90, self.BXPos + 120, self.RYPos + 30
	
	def getHp(self,damage,Map):
		if self.SlimeHp>=0:
			self.SlimeHp-= damage
		
		
	#def Patter1(self):
		
		
		