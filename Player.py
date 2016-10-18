from pico2d import *


def handle_events():
	global running
	global x
	global isRight, isLeft
	events = get_events()
	for event in events:
		if event.type == SDL_QUIT:
			running = False
		if event.type == SDL_KEYDOWN:
			if event.key == SDLK_RIGHT:
				isRight = True
			elif event.key == SDLK_LEFT:
				isLeft = True
			elif event.key == SDLK_ESCAPE:
				running = False
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
		# self.image.clip_draw(0,0,500,900,250,self.y)
		self.image.draw_to_origin(0, self.y2, 600, 800)
	
	def draw2(self):
		# self.image.clip_draw(0,0,500,900,250,self.y)
		self.image.draw_to_origin(0, self.y1, 600, 800)


class Monster:
	def __init__(self):
		self.image = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Plyaer\\Boss\\slime.png')
		self.y = 800
		self.x = 300
		self.Bframe = 0
	
	def update(self):
		self.Bframe = (self.Bframe + 1) % 4
	
	def draw(self):
		self.image.clip_draw(self.Bframe, self.x, self.y, 300, 200)


character = load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\Player\\character1.png')

running = True
x = 100
frame = 0
isRight = False
isLeft = False

Stage = BackGround()
Boss=Monster()

while (running):
	if isRight == True:
		x = x + 15
	elif isLeft == True:
		x = x - 15
	elif (isRight, isLeft) == (False, False):
		x = x + 0
	
	Stage.update()
	Boss.update()
	
	clear_canvas()
	
	Stage.draw()
	Stage.draw2()
	Boss.draw()
	character.clip_draw(frame * 170, 0, 170, 130, x, 120)
	
	update_canvas()
	frame = (frame + 1) % 3
	
	delay(0.05)
	handle_events()

close_canvas()

