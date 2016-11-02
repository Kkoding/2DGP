import random
import os

from pico2d import *

import game_framework
import title_state

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
Bullet_Max=30
Stage = None
Bullet = None
Mob = None

User = None
King = None
MapState = Map1
BossShot=None
BossNum=0

MobLimit=12



RedMonster=None
#추가할 것들.
#   Red몹
#   각 탄마다 보스 깨고나서 스크롤링
#   보스구현
#   보스 탄환알고리즘 구현하기(시간지남에 따라서 패턴반복)
#
#

def enter():
	global Stage, Bullet, Mob, User,King, BossShot
	open_canvas(600,800,sync=True)
	Bullet = [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	BossShot = [Boss() for i in range(30)]
	Mob = [Monster(i) for i in range(MobLimit)]
	User = Player()
	King = Boss()
	
	RedMonster=[Monster(i) for i in range(MobLimit)]
	
	
def update():
	global MapState, Stage, BulltNum, i
	Stage.update(MapState)
	for i in range(MobLimit):
		Mob[i].update(i)
	User.update()
	King.update()
	
	#보스체크
	MapState = King.BossLevel()
	
	#맵 선택체크
	Stage.MapLevel( MapState)
	
	#총알충돌체크
	for Shot in Bullet:
		Shot.update(User.x)
		
	for i in range(Bullet_Max):
		for j in range(MobLimit):
			if Bullet[i].Drawing == True:
				if Bullet[i].collide(Mob[j]) == True:
					print("Mob Col")
					if Mob[j].Damaged==True:
						Mob[j].Damege(2)
					if Mob[j].MonHp<14:
						Mob[j].Damaged = True
					elif Mob[j].MonHp>14:
						Mob[j].Damaged=False
					Bullet[i].Drawing = False
				elif Bullet[i].collide(King) == True:
					King.FlagBossHp=True
					print("King Col")
					King.getHp(User.damage)
					Bullet[i].Drawing = False
				

def draw():
	global Count,i, BossNum
	global Mob,BulltNum
	clear_canvas()
	
	#다 그리기
	Stage.draw()
	Stage.draw2()
	for i in range(MobLimit):
		Mob[i].draw(i)
	User.draw()
	King.draw(MapState)
	
	for Shot in Bullet:
		Shot.draw()
		# 충돌사각형
		Attack.draw_bb(Shot)
		
	
	# 충돌사각형
	Player.draw_bb(User)
	for i in range(MobLimit):
		Mob[i].draw_bb()
	Boss.draw_bb(King)
	
	
	for i in range(0,BossNum):
		BossShot[i].drawShot(BossNum)
	
	# T/F ?? Count of Bullet
	Count += 3
	if Count % 6 == 0:
		if Bullet[BulltNum].Drawing == False:
			Bullet[BulltNum].Drawing = True
			BulltNum += 1
		if BulltNum > Bullet_Max - 1:
			BulltNum = 0
	
	update_canvas()
	delay(0.05)

def exit():
	pass

def handle_events():
	global User
	global BackGround
	global Stage
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		else :
			User.handle_event(event)
			Stage.handle_event(event)
			
			
	
	



