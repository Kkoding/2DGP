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

Count=0
i=0
Bullet_Max=30
Stage = None
Bullet = None
Mob = None
User = None

	
def enter():
	global Stage, Bullet, Mob, User
	open_canvas(600,800)
	Bullet = [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	Mob = Monster()
	User = Player()
	
def update():
	global User
	Stage.update()
	Mob.update()
	User.update()
	for Shot in Bullet:
		Shot.update(User.x)
		

def draw():
	global Count,i
	clear_canvas()
	
	Stage.draw()
	Stage.draw2()
	
	Mob.draw()
	User.draw()
	for Shot in Bullet:
		Shot.draw()
	
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


def handle_events():
	global User
	global Player
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		else :
			User.handle_event(event)
			
	
	



