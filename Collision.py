from pico2d import *

import game_framework

import main_state

from BackGround import *
from Obj_Monster import *
from Obj_Player import *
from Obj_Bullet import *
from Obj_Boss import *



def create_world():
	global Stage, Bullet, Mob, User, King
	
	Bullet_Max =30
	Bullet = [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	Mob = Monster()
	User = Player()
	King = Boss()


def collide(a, b):
	left_a, bottom_a, right_a, top_a = a.get_bb()
	left_b, bottom_b, right_b, top_b = b.get_bb()
	
	if left_a > right_b: return False
	if right_a < left_b: return False
	if top_a < bottom_b: return False
	if bottom_a > top_b: return False
	
	return True


def update():
	for Attack in Bullet:
		if collide (User, Bullet):
			print("collision")
		
		
	
	
	
	