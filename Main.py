from pico2d import *



def handle_events():
	global running
	global x
	global isRight, isLeft
	global Shot
	global Move
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_RIGHT:
				isRight = True
			if event.key == SDLK_LEFT:
				isLeft = True
			elif event.key == SDLK_ESCAPE:
				running = False
			if event.key == SDLK_SPACE:
				Shot = True
				
				
		if event.type == SDL_KEYUP:
			if isRight == True:
				isRight = False
			if isLeft == True:
				isLeft = False
			

class BackGround:
	def __init__(self):
		self.image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\03.png')
		self.image2 = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\03.png')
		self.y1 = 0
		self.y2 = 800
	
	def update(self):
		self.y1 -= 10
		self.y2 -= 10
		if (self.y2 == 0):
			self.y1 = 0
			self.y2 = 800
	
	def draw(self):
		#self.image.clip_draw(0,0,500,900,250,self.y)
		self.image.draw_to_origin(0, self.y2, 600, 800)
	
	def draw2(self):
		#self.image.clip_draw(0,0,500,900,250,self.y)
		self.image.draw_to_origin(0, self.y1, 600, 800)


class Monster:
	def __init__(self):
		self.image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Boss\\slime.png')
		self.imageMob=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Monster\\Mon\\Mon1.png')
		self.Moby=1100
		self.y = 2100
		#self.x = 300
		self.frame = 0
	
	def update(self):
		self.y-=10
		self.Moby-=10
		if self.y<680:
			self.y=680
		self.frame = (self.frame+1 ) % 4
	
	def draw(self):
		self.imageMob.clip_draw(self.frame*180, 0, 180, 120, 256, self.Moby)
		self.image.clip_draw(self.frame*300,0,300,256,300,self.y )

class Player:
	global Shot
	global x
	global Bullet
	global Move
	def __init__(self):
		self.p_image=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\character1.png')
		self.b_image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\bullet_sunny.png')
		self.frame=0
		self.bX=x
		self.bY=50
	def update(self):
		self.frame = (self.frame + 1) % 3
		if Shot==False:
			self.bX = x
		elif Shot == True:
			self.bY += 10
		if self.bY>700:
			self.bX = x
			self.bY=50
			 
	def draw(self):
		self.p_image.clip_draw(self.frame * 170, 0, 170, 130, x, 50)
		if Shot==True:
			self.b_image.clip_draw(0,0,64,64,self.bX,self.bY)

		
open_canvas(600,800)
running = True
x = 100

isRight = False
isLeft = False
Shot = False
Move = False

character = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\Player\\character1.png')
Stage = BackGround()
Mob = Monster()
User=Player()

while (running):
	if isRight == True:
		x = x + 15
	elif isLeft == True:
		x = x - 15
	elif (isRight, isLeft) == (False, False):
		x = x + 0
	
	if User.bY > 800:
		Shot=False
		
	Stage.update()
	Mob.update()
	User.update()
		
	clear_canvas()
	
	Stage.draw()
	Stage.draw2()
	Mob.draw()
	User.draw()
	
	update_canvas()
	
	delay(0.05)
	handle_events()



