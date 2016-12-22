from pico2d import *

import random
import game_framework
import start_state
import title_state

import main_state

import math

from Obj_Player import*


class Boss:
	Map1, Map2, Map3 = 0, 1,2
	Boss1, Boss2, Boss3 = 10,11,22
	def __init__(self,select):
		if select==0:
			self.Boss=self.Boss1
			self.Boss_image = load_image('Monster\\Boss\\slime.png')
			self.Slime_Die_image = load_image('Monster\\Boss\\slime die.png')
		
		elif select==1:
			self.Boss = self.Boss2
			self.Stone_image = load_image('Monster\\Boss\\Stone.png')
			self.Stone_Die_image = load_image('Monster\\Boss\\StoneDie.png')
		elif (select == 2):
			self.Boss=self.Boss3
			self.Reds_image = load_image('Monster\\Boss\\Reds.png')
			self.Red_Die_image = load_image('Monster\\Boss\\Reds die.png')
			
		
		
		self.BossHpImage =load_image('Monster\\Boss\\boss_hp.png')
		self.Boss_YPos = 3000
		self.Boss_XPos = 300
		self.BYPos = self.Boss_YPos
		self.BXPos = self.Boss_XPos
		self.Bframe = 0
		self.FlagBossHp=False
		
		self.Boss_Bullet = load_image('Monster\\bullet_boss.png')
		self.BulletX=30
		self.BulletY=700
		
		self.SlimeHp = 24*((select+1)*3)
		self.StoneHp = 24
		
		self.imagetimer=0
		self.ChangeScene=0
		self.ChangeScene2 = 0
		self.Change2=False
		
		self.Patter1Y=1
		self.Pattern2=-1
		self.Pattern2Y=0
		
		self.Pattern3X=self.BXPos
		self.Pat3X = [300,300,300,300]
		self.Pat3Y = [680,680,680,680]
		self.Rope=1
		self.Timer=0
		self.num=0
		self.ENDING=False
		
	def __del__(self):
		del self.Boss_image
		del self.Slime_Die_image
		del self.Stone_Die_image
		del self.Stone_image
		del self.BossHpImage
		del self.Boss_Bullet
		del self.Reds_image
		del self.Red_Die_image
		
	def update(self,Map):
		self.imagetimer+=0.5
		if self.imagetimer % 2 == 0:
			self.Bframe = (self.Bframe + 1) % 4
		#보스 내랴오는것
		if Map == 0:
			if self.BYPos > 680:
				self.BYPos -= 10
				#self.Pattern2Y=self.BYPos
			self.Patter1Y -= 25
			if (self.Patter1Y < -1200):
				self.Patter1Y = 0
		elif Map == 1:
			if self.BYPos>680:
				self.BYPos-=10
			self.Patter1Y -= 25
			if (self.Patter1Y < -1200):
				self.Patter1Y = 0
				if (self.Rope < 8):
					self.Rope += 1
				
		elif Map == 2:
			if self.BYPos>680:
				self.BYPos-=10
			self.Patter1Y -= 25
			if (self.Patter1Y < -1200):
				self.Patter1Y = 0
				if (self.Rope < 8):
					self.Rope += 1
			
		
				
		if (self.Pattern2 < 1000):
			self.Pattern2 += 0.2
			# 구의 속도
			# if self.Pattern2Y<300:
			#self.Pattern2Y -= 5
		
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
				self.Stone_image.clip_draw(256*self.Bframe,0,256,205, self.BXPos, self.BYPos)
				#print("%d",self.SlimeHp)
			else:
				if self.ChangeScene2 < 45:
					self.Stone_Die_image.clip_draw(0, 0, 256, 205, self.BXPos, self.BYPos)
				else:
					self.Change2 = True
		elif self.Boss==self.Boss3:
			if self.SlimeHp>=0:
				self.Reds_image.clip_draw(512*self.Bframe%4,0,512,512,self.BXPos,self.BYPos)
			else:
				self.ENDING=True
				self.Red_Die_image.clip_draw(0, 0, 500, 485, self.BXPos, self.BYPos )
					
				
				
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
		return self.BXPos - 120, self.BYPos - 90, self.BXPos + 120, self.BYPos + 30
	
	def draw_bb3(self):
		draw_rectangle(*self.get_bb2())
	
	def get_bb3(self):
		return self.BXPos - 120, self.BYPos - 90, self.BXPos + 120, self.BYPos + 30
	
	def getHp(self,damage,Map):
		if self.SlimeHp>=0:
			self.SlimeHp-= damage
			return self.SlimeHp
		
		
	#할튼 날라가버리기~
	def Pattern1_Draw(self):
		#6시방향
		self.Boss_Bullet.clip_draw(0,0,52,52,self.BXPos,self.BYPos+self.Patter1Y*math.sin(math.pi/2))
		#self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos- self.Patter1Y/2 * math.sin(math.pi / 2), self.BYPos+ self.Patter1Y/2 * math.sin(math.pi / 2) )
		#7시
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos + self.Patter1Y/2 * math.sin(math.pi / 2), self.BYPos+self.Patter1Y*math.sin(math.pi/2))
		#7.5시
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos + self.Patter1Y/4 * math.sin(math.pi / 2), self.BYPos + self.Patter1Y * math.sin(math.pi / 2))
		#5시
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos - self.Patter1Y/2 * math.sin(math.pi / 2), self.BYPos + self.Patter1Y * math.sin(math.pi / 2))
		#5.3시
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos - self.Patter1Y/4 * math.sin(math.pi / 2),self.BYPos + self.Patter1Y * math.sin(math.pi / 2))
		#5.35
		self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos - self.Patter1Y / 4 * math.sin(math.pi / 2), self.BYPos + self.Patter1Y * math.sin(math.pi / 2))
	
			
	
	#채찍
	def Patter2_Draw(self):
		for i in range(1,self.Rope):
			self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos+80*i * math.cos(self.Pattern2), 600 +80*i * math.sin(self.Pattern2))
		
		# self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos+ 10*i* math.sin(math.pi / 2), self.BYPos-  10*i * math.sin(math.pi / 2)*i)
		# self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos + 1 * math.cos(self.Pattern2), self.Pattern2Y + 1 * math.sin(self.Pattern2))
		# self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.BXPos + self.Pattern2X * math.cos(self.Pattern2),self.Pattern2Y + 50 * math.sin(self.Pattern2))
	
	#유도
	def Pattern3_Update(self,Pos):
		for i in range(self.num+1):
			if i < 4:
				self.Pat3Y[i] -= 5
				if self.Pat3X[i] >Pos:
					self.Pat3X[i]-=2.5
				elif self.Pat3X[i ]<Pos:
					self.Pat3X[i] += 2.5
				if self.Pat3Y[i]==350:
					if self.num !=4:
						self.num+=1
		#if self.Pattern2Y<300:
		#	self.num+=1
		
	def Pattern3_Draw(self):
		for i in range(0,self.num+1):
			if i < 4:
				self.Boss_Bullet.clip_draw(0, 0, 52, 52, self.Pat3X[i] , self.Pat3Y[i])
		
	
		
	def BossAttack(self, num,xPos):
		if (num == self.Map1):
			if self.BYPos < 689 and self.SlimeHp>0:
				self.Pattern1_Draw ()
			#	self.Patter2_Draw()
			#	self.Pattern3_Update(xPos)
			#	self.Pattern3_Draw()
		if(num == self.Map2):
			if self.BYPos < 689 and self.SlimeHp > 0:
				self.Pattern1_Draw()
				self.Patter2_Draw()
		if (num == self.Map3):
			if self.BYPos < 689 and self.SlimeHp > 0:
				self.Pattern1_Draw()
				self.Patter2_Draw()
				self.Pattern3_Update(xPos)
				self.Pattern3_Draw()
		
	

			
		
		
		
		
		