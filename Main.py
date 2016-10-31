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
i=0
Bullet_Max=30
Stage = None
Bullet = None
Mob = None
User = None
King = None
name = Map1
BossShot=None
BossNum=0
	
def enter():
	global Stage, Bullet, Mob, User,King, BossShot
	open_canvas(600,800)
	Bullet = [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	BossShot = [Boss() for i in range(30)]
	Mob = Monster()
	User = Player()
	King = Boss()
	
def update():
	Stage.update()
	Mob.update()
	User.update()
	King.update()
	for Shot in Bullet:
		Shot.update(User.x)
		
	for i in range(Bullet_Max):
		if Bullet[i].Drawing == True:
			if Bullet[i].collide(Mob) == True:
				print("Mob Col")
				Bullet[i].Drawing=False
			elif Bullet[i].collide(King) == True:
				King.FlagBossHp=True
				print("King Col")
				King.getHp(User.damage)
				Bullet[i].Drawing = False
				

def draw():
	global Count,i, BossNum
	global Mob
	clear_canvas()
	
	#다 그리기
	Stage.draw()
	Stage.draw2()
	Mob.draw()
	User.draw()
	King.draw()
	
	for Shot in Bullet:
		Shot.draw()
		# 충돌사각형
		Attack.draw_bb(Shot)
		
	
	# 충돌사각형
	Player.draw_bb(User)
	Monster.draw_bb(Mob)
	Boss.draw_bb(King)
	
	
	for i in range(0,BossNum):
		BossShot[i].drawShot(BossNum)
	
	
	# T/F ?? Count of Bullet
	Count += 2
	if Count % 6 == 0:
		if Bullet[i].Drawing == False:
			Bullet[i].Drawing = True
			i += 1
		if i > Bullet_Max - 1:
			i = 0
	
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
			
			
	
	



