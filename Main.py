import random
import os
import math

from pico2d import *

import game_framework
import title_state
import ready_state

name = "Main"

from BackGround import *
from Obj_Monster import *
from Obj_Player import *
from Obj_Bullet import *
from Obj_Boss import *
from Collision import *
Map1, Map2, Map3 = 0,1,2

Count=0
BulltNum=0
S_BulletNum=0
Bullet_Max=30
Stage = None
Bullet = None
Mob = None

User = None
King = None
StoneKing=None
MapState = None
BossShot=None
BossNum = 0

MobLimit=12

YellowMonster=None
SubBullet = None
SubBullet2  = None
#추가할 것들.
#   Red몹
#   각 탄마다 보스 깨고나서 스크롤링
#   보스구현
#   보스 탄환알고리즘 구현하기(시간지남에 따라서 패턴반복)

Cloud = None
YellowMonster=None
RedMonster=None
BossAttack=None
BossNum=0
gBGM=None

def enter():
	global Stage, Bullet, Mob, User,King, BossShot, Cloud, YellowMonster,MapState,RedMonster,BossAttack
	global SubBullet
	open_canvas(600,800,sync=True)
	
	Bullet = [Attack() for i in range(Bullet_Max)]
	SubBullet = [Attack() for i in range(Bullet_Max)]
	SubBullet2= [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	##BossShot = [Boss() for i in range(30)]
	Mob = [Monster(i) for i in range(MobLimit)]
	User = Player()
	King = [Boss(i)for i in range(3)]
	Cloud = BackGround()
	YellowMonster=[Monster(i) for i in range(MobLimit)]
	RedMonster = [Monster(i) for i in range(MobLimit)]
	MapState=Map1
	BossAttack=[Boss(i) for i in range(10)]

	global gBGM
	gBGM = load_music('logo_background.mp3')
	gBGM.set_volume(64)
	
	
def update():
	global MapState, Stage, BulltNum, i,BossNum, King,BossAttack
	global Cloud, BG_Sound,gBGM,SubBullet,SubBullet2
	
	gBGM.repeat_play()
	
	#stage
	Stage.update(MapState)
	if MapState == Map1:
		for Obj_Monster in Mob:
			Obj_Monster.update(MapState)
	elif MapState == Map2:
		for i in range(MobLimit):
			YellowMonster[i].update(MapState)
	elif MapState == Map3:
		for i in range(MobLimit):
			RedMonster[i].update(MapState)

	#Player
	User.update()
		
	#Kings
	if MapState == Map1:
		King[0].update(MapState)
	elif MapState == Map2:
		King[1].update(MapState)
		if King[1].Change2==True:
			#print("ㅁㄴㅇㅁㄴㅇ")
			King[0].Change2 = True
	elif MapState == Map3:
		King[2].update(MapState)
	

	
	#보스체크:
	if King[0].Change2==False:
		MapState = King[0].BossLevel()
	elif King[0].Change2==True:
		#print("asdasdsad")
		MapState =2
	
	
	
	#맵 선택체크
	Stage.MapLevel(MapState)
	
	#SubAttack
	for Shot in SubBullet:
		Shot.Sub_Update(User.x)
		
	#for Shot in SubBullet2:
	#
	# 	Shot.Sub_Update(User.x,Player.L_Hatch)
		
	#for Obj_Bullet in SubBullet:
	#	Obj_Bullet.updatebb()
		
	#총알충돌체크
	for Shot in Bullet:
		Shot.update(User.x)
		
	
		
	#총알과 몬스터`s
	for Obj_Bullet in Bullet:
		if MapState == Map1:
			for Obj_Monster in Mob:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.collide(Obj_Monster) == True and Obj_Monster.MonHp<14:
						Obj_Bullet.Drawing = False
						#들어가는 데미지
						if Obj_Monster.Damaged==True:
							Obj_Monster.Damege(Player.damage)
						if Obj_Monster.MonHp<14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp>=14 or Obj_Monster.y < 0:
								#Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.collide(King[0]) == True:
						King[0].FlagBossHp=True
						King[0].getHp(User.damage,MapState)
						Obj_Bullet.Drawing = False
		if MapState == Map2:
			for Obj_Monster in YellowMonster:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.collide(Obj_Monster) == True:
						Obj_Bullet.Drawing = False
						if Obj_Monster.Damaged==True:
							Obj_Monster.Damege(Player.damage)
						if Obj_Monster.MonHp<14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp>=14 or Obj_Monster.y < 0:
								#Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.collide2(King[1]) == True:
						King[1].FlagBossHp = True
						King[1].getHp(User.damage, MapState)
						Obj_Bullet.Drawing = False
		if MapState == Map3:
			for Obj_Monster in RedMonster:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.collide(Obj_Monster) == True:
						Obj_Bullet.Drawing = False
						if Obj_Monster.Damaged == True:
							Obj_Monster.Damege(Player.damage)
						if Obj_Monster.MonHp < 14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
								# Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.collide2(King[2]) == True:
						King[2].FlagBossHp = True
						King[2].getHp(User.damage, MapState)
						Obj_Bullet.Drawing = False
	
	#Sub Attack
	for Obj_Bullet in SubBullet:
		if MapState == Map1:
			for Obj_Monster in Mob:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp<14:
						Obj_Bullet.Drawing = False
						#들어가는 데미지
						if Obj_Monster.Damaged==True:
							Obj_Monster.Damege(1)
						if Obj_Monster.MonHp<14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp>=14 or Obj_Monster.y < 0:
								#Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.Rcollide(King[0]) == True:
						King[0].FlagBossHp=True
						King[0].getHp(User.damage,MapState)
						Obj_Bullet.Drawing = False
					
		if MapState == Map2:
			for Obj_Monster in YellowMonster:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp<14:
						Obj_Bullet.Drawing = False
						# 들어가는 데미지
						if Obj_Monster.Damaged == True:
							Obj_Monster.Damege(1)
						if Obj_Monster.MonHp < 14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
								# Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.Rcollide(King[1]) == True:
						King[1].FlagBossHp = True
						King[1].getHp(User.damage, MapState)
						Obj_Bullet.Drawing = False
					
		if MapState == Map3:
			for Obj_Monster in RedMonster:
				if Obj_Bullet.Drawing == True:
					if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp<14:
						Obj_Bullet.Drawing = False
						# 들어가는 데미지
						if Obj_Monster.Damaged == True:
							Obj_Monster.Damege(1)
						if Obj_Monster.MonHp < 14:
							Obj_Monster.Damaged = True
							if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
								# Obj_Monster.y = -20
								Obj_Monster.Damaged = False
								Obj_Bullet.Drawing = False
								del Obj_Monster
					elif Obj_Bullet.Rcollide(King[2]) == True:
						King[2].FlagBossHp = True
						King[2].getHp(User.damage, MapState)
						Obj_Bullet.Drawing = False
					
	#for Obj_Monster in Mob:
	#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
	#		Obj_Monster.Damaged = False
	#		Obj_Bullet.Drawing = False
	#		del Obj_Monster
	#for Obj_Monster in YellowMonster:
	#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
	#		Obj_Monster.Damaged = False
	#		Obj_Bullet.Drawing = False
	#		del Obj_Monster
	#for Obj_Monster in RedMonster:
	#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
	#		Obj_Monster.Damaged = False
	#		Obj_Bullet.Drawing = False
	#		del Obj_Monster
			
				
	#구름그리기
	Cloud.update(MapState)
	
def draw():
	global Count,i, BossNum,S_BulletNum
	global Mob,BulltNum,YellowMonster,King,MapState,RedMonster,BossAttack
	global Cloud,SubBullet,SubBullet2
	clear_canvas()
	
	#다 그리기(스테이지)
	Stage.draw()
	Stage.draw2()
	#몬스터
	if MapState == Map1:
		for i in range(MobLimit):
			Mob[i].draw(MapState)
	elif MapState == Map2:
		for i in range(MobLimit):
			YellowMonster[i].draw(MapState)
	elif MapState == Map3:
		for i in range(MobLimit):
			RedMonster[i].draw(MapState)
		 
	User.draw()
	if MapState == Map1:
		King[0].draw(MapState)
	elif MapState == Map2:
		King[1].draw(MapState)
	elif MapState == Map3:
		King[2].draw(MapState)
		
	for Shot in Bullet:
		Shot.draw(Player.damage,Player.GM)
		# 충돌사각형
		Attack.draw_bb(Shot)
		
	#Bullet-Sub
	for Obj_Bullet in SubBullet:
		Obj_Bullet.RSub_draw(Player.R_Hatch)
		
#	for Obj_Bullet in SubBullet2:
#		Obj_Bullet.LSub_draw(Player.L_Hatch)
	
	#Colli-Sub
	#for Obj_Bullet in SubBullet:
	#	Obj_Bullet.draw_bb()
		
	# 충돌사각형
	Player.draw_bb(User)
	if MapState == Map1:
		for Obj_Monster in Mob:
			if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
				Obj_Monster.draw_bb()
	elif MapState == Map2:
		for Obj_Monster in YellowMonster:
			if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
				Obj_Monster.draw_bb()
	elif MapState == Map3:
		for Obj_Monster in RedMonster:
			if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
				Obj_Monster.draw_bb()
	
	if MapState == Map1:
		Boss.draw_bb(King[0])
	if MapState == Map2:
		Boss.draw_bb2(King[1])
	if MapState == Map3:
		Boss.draw_bb3(King[2])
		
	# T/F ?? Count of Bullet
	Count += 3
	if Count % 6 == 0:
		if Bullet[BulltNum].Drawing == False:
			Bullet[BulltNum].Drawing = True
			BulltNum += 1
		if BulltNum > Bullet_Max - 1:
			BulltNum = 0
		#########Sub
		if SubBullet[S_BulletNum].Drawing == False:
			SubBullet[S_BulletNum].Drawing = True
			S_BulletNum += 1
		if S_BulletNum > Bullet_Max - 5:
			S_BulletNum = 0
			
			
			
	
	#구름 그리기
	Cloud.drawCloud(MapState)
	BossNum+=1
	#보스총알
	if MapState == Map1:
		King[0].BossAttack(MapState,User.x)
	elif MapState == Map2:
		King[1].BossAttack(MapState,User.x)
	elif MapState == Map3:
		King[2].BossAttack(MapState,User.x)
	
	
	
	update_canvas()
	delay(0.05)

def exit():
	global Mob, BulltNum, YellowMonster, King, MapState, RedMonster, BossAttack,MobLimit,User
	global Cloud
	
	del User
	for Obj_Monster in Mob:
		del Obj_Monster
	for Obj_Monster in RedMonster:
		del Obj_Monster
	for Obj_Monster in YellowMonster:
		del Obj_Monster
		
	for Obj_Bullet in Bullet:
		del Obj_Bullet
		
	for Obj_Bullet in SubBullet:
		del Obj_Bullet
	
	close_canvas()
	
	

def handle_events():
	global User
	global BackGround
	global Stage
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		elif (event.key) == (SDLK_SPACE):
			game_framework.change_state(ready_state)
		else :
			User.handle_event(event)
			Stage.handle_event(event)
			
			
	
	



