import game_framework
import select_state
import start_state
import ready_state
from pico2d import *

name = "TitleState"
image = None
BG_Sound = None

BGM = None


from BackGround import *
from Obj_Monster import *
from Obj_Player import *
from Obj_Bullet import *
from Obj_Boss import *
from Collision import *


Map1, Map2, Map3 = 0, 1, 2

Count = 0
BulltNum = 0
S_BulletNum = 0
S_BulletNum2 = 0

Bullet_Max = 22
Stage = None
Bullet = None
Mob = None

User = None
King = None
StoneKing = None
MapState = None
BossShot = None
BossNum = 0

MobLimit = 12

YellowMonster = None
SubBullet = None
SubBullet2 = None


Cloud = None
YellowMonster = None
RedMonster = None
BossAttack = None
BossNum = 0
gBGM = None


Change=False
def enter():
	global image, BG_Sound
	open_canvas(600, 800)
	image = load_image('BackGround\\Title.png')
	global BGM
	BGM = load_music('background.mp3')
	BGM.set_volume(64)
	BGM.repeat_play()

	global Stage, Bullet, Mob, User, King, BossShot, Cloud, YellowMonster, MapState, RedMonster, BossAttack
	global SubBullet, SubBullet2
	
	Bullet = [Attack() for i in range(Bullet_Max)]
	SubBullet = [Attack() for i in range(Bullet_Max)]
	SubBullet2 = [Attack() for i in range(Bullet_Max)]
	Stage = BackGround()
	##BossShot = [Boss() for i in range(30)]
	Mob = [Monster(i) for i in range(MobLimit)]
	User = Player()
	King = [Boss(i) for i in range(3)]
	Cloud = BackGround()
	YellowMonster = [Monster(i) for i in range(MobLimit)]
	RedMonster = [Monster(i) for i in range(MobLimit)]
	MapState = Map1
	BossAttack = [Boss(i) for i in range(10)]
	

def exit():
	global image, BG_Sound
	close_canvas()
	del (image)


def handle_events():
	global Change
	global User
	global BackGround
	global Stage
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			game_framework.quit()
		else:
			if Change==False:
				if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
					game_framework.quit()
				elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
					game_framework.change_state(select_state)
				elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
					Change=True
					game_framework.change_state(select_state)
					pass
			elif (event.key) == (SDLK_ESCAPE):
				game_framework.change_state(ready_state)
			else:
				User.handle_event(event)
				Stage.handle_event(event)
		



def draw():
	global BG_Sound
	global Count, i, BossNum, S_BulletNum, S_BulletNum2
	global Mob, BulltNum, YellowMonster, King, MapState, RedMonster, BossAttack
	global Cloud, SubBullet, SubBullet2,Change
	clear_canvas()
	if Change==False:
		image.clip_draw(0, 0, 384, 512, 300, 400, 600, 800)
	else:
		# image.draw(192,256)
		# 다 그리기(스테이지)
		Stage.draw()
		Stage.draw2()
		# 몬스터
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
			Shot.draw(Player.damage, Player.GM)
		# 충돌사각형
		# Attack.draw_bb(Shot)
		
		# Bullet-Sub
		for Obj_Bullet in SubBullet:
			Obj_Bullet.RSub_draw(Player.R_Hatch)
		
		for Obj_Bullet in SubBullet2:
			Obj_Bullet.LSub_draw(Player.L_Hatch)
		
		# Colli-Sub
		# for Obj_Bullet in SubBullet:
		#	Obj_Bullet.draw_bb()
		
		# 충돌사각형
		# Player.draw_bb(User)
		# if MapState == Map1:
		#	for Obj_Monster in Mob:
		#		if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
		#			Obj_Monster.draw_bb()
		# elif MapState == Map2:
		#	for Obj_Monster in YellowMonster:
		#		if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
		#			Obj_Monster.draw_bb()
		# elif MapState == Map3:
		#	for Obj_Monster in RedMonster:
		#		if Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
		#			Obj_Monster.draw_bb()
		
		# if MapState == Map1:
		#	Boss.draw_bb(King[0])
		# elif MapState == Map2:
		#	Boss.draw_bb2(King[1])
		# elif MapState == Map3:
		#	Boss.draw_bb3(King[2])
		
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
			
			if SubBullet2[S_BulletNum].Drawing == False:
				SubBullet2[S_BulletNum].Drawing = True
				S_BulletNum2 += 1
			
			if S_BulletNum > Bullet_Max - 5:
				S_BulletNum = 0
			if S_BulletNum2 > Bullet_Max - 5:
				S_BulletNum2 = 0
		
		# 구름 그리기
		Cloud.drawCloud(MapState)
		
		BossNum += 1
		# 보스총알
		if MapState == Map1:
			King[0].BossAttack(MapState, User.x)
		elif MapState == Map2:
			King[1].BossAttack(MapState, User.x)
		elif MapState == Map3:
			King[2].BossAttack(MapState, User.x)
	
	update_canvas()
	delay(0.05)
	pass


def update():
	global MapState, Stage, BulltNum, i, BossNum, King, BossAttack
	global Cloud, BG_Sound, gBGM, SubBullet, SubBullet2,Change
	if Change == True:
		# stage
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
		
		# Player
		User.update()
		
		# Kings
		if MapState == Map1:
			King[0].update(MapState)
		elif MapState == Map2:
			King[1].update(MapState)
			if King[1].Change2 == True:
				# print("ㅁㄴㅇㅁㄴㅇ")
				King[0].Change2 = True
		elif MapState == Map3:
			King[2].update(MapState)
		
		# 보스체크:
		if King[0].Change2 == False:
			MapState = King[0].BossLevel()
		elif King[0].Change2 == True:
			# print("asdasdsad")
			MapState = 2
		
		# 맵 선택체크
		Stage.MapLevel(MapState)
		
		# SubAttack
		for Shot in SubBullet:
			Shot.Sub_Update(User.x)
		
		for Shot in SubBullet2:
			Shot.Sub_Update2(User.x)
		
		# for Obj_Bullet in SubBullet:
		#	Obj_Bullet.updatebb()
		
		# 총알충돌체크
		for Shot in Bullet:
			Shot.update(User.x)
		
		# 총알과 몬스터`s
		for Obj_Bullet in Bullet:
			if MapState == Map1:
				for Obj_Monster in Mob:
					if Obj_Bullet.Drawing == True:
						if Obj_Bullet.collide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
							Obj_Bullet.Drawing = False
							# 들어가는 데미지
							if Obj_Monster.Damaged == True:
								Obj_Monster.Damege(Player.damage)
							if Obj_Monster.MonHp < 14:
								Obj_Monster.Damaged = True
								if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
									# Obj_Monster.y = -20
									Obj_Monster.Damaged = False
									Obj_Bullet.Drawing = False
									del Obj_Monster
						elif Obj_Bullet.collide(King[0]) == True:
							King[0].FlagBossHp = True
							King[0].getHp(User.damage, MapState)
							Obj_Bullet.Drawing = False
			elif MapState == Map2:
				for Obj_Monster in YellowMonster:
					if Obj_Bullet.Drawing == True:
						if Obj_Bullet.collide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
						elif Obj_Bullet.collide2(King[1]) == True:
							King[1].FlagBossHp = True
							King[1].getHp(User.damage, MapState)
							Obj_Bullet.Drawing = False
			elif MapState == Map3:
				for Obj_Monster in RedMonster:
					if Obj_Bullet.Drawing == True:
						if Obj_Bullet.collide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
		
		# Sub Attack
		if Player.R_Hatch == True:
			for Obj_Bullet in SubBullet:
				if MapState == Map1:
					for Obj_Monster in Mob:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
							elif Obj_Bullet.Rcollide(King[0]) == True:
								King[0].FlagBossHp = True
								King[0].getHp(User.damage, MapState)
								Obj_Bullet.Drawing = False
				elif MapState == Map2:
					for Obj_Monster in YellowMonster:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
				elif MapState == Map3:
					for Obj_Monster in RedMonster:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Rcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
		
		if Player.L_Hatch == True:
			for Obj_Bullet in SubBullet2:
				if MapState == Map1:
					for Obj_Monster in Mob:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Lcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
							elif Obj_Bullet.Lcollide(King[0]) == True:
								King[0].FlagBossHp = True
								King[0].getHp(User.damage, MapState)
								Obj_Bullet.Drawing = False
				if MapState == Map2:
					for Obj_Monster in YellowMonster:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Lcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
							elif Obj_Bullet.Lcollide(King[1]) == True:
								King[1].FlagBossHp = True
								King[1].getHp(User.damage, MapState)
								Obj_Bullet.Drawing = False
				elif MapState == Map3:
					for Obj_Monster in RedMonster:
						if Obj_Bullet.Drawing == True:
							if Obj_Bullet.Lcollide(Obj_Monster) == True and Obj_Monster.MonHp < 14 and Obj_Monster.y > 0:
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
							elif Obj_Bullet.Lcollide(King[2]) == True:
								King[2].FlagBossHp = True
								King[2].getHp(User.damage, MapState)
								Obj_Bullet.Drawing = False
		
		# if King[2].getHp(User.damage, MapState) == 0:
		#	game_framework.change_state(start_state)
		
		# for Obj_Monster in Mob:
		#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
		#		Obj_Monster.Damaged = False
		#		Obj_Bullet.Drawing = False
		#		del Obj_Monster
		# for Obj_Monster in YellowMonster:
		#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
		#		Obj_Monster.Damaged = False
		#		Obj_Bullet.Drawing = False
		#		del Obj_Monster
		# for Obj_Monster in RedMonster:
		#	if Obj_Monster.MonHp >= 14 or Obj_Monster.y < 0:
		#		Obj_Monster.Damaged = False
		#		Obj_Bullet.Drawing = False
		#		del Obj_Monster
		
		
		# 구름그리기
		Cloud.update(MapState)
		
		if (King[2].SlimeHp == 0):
			Change=False
			return
	pass


def pause():
	pass


def resume():
	pass






