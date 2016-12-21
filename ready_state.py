import game_framework
import title_state
import main_state

from pico2d import *

from BackGround import *
from Obj_Monster import *
from Obj_Player import *
from Obj_Bullet import *
from Obj_Boss import *
from Collision import *

name = "ready_state"
image = None
logo_time = 0.0

Sound_Button = None

BGM = None
shop_bgm = None

def enter():
    global image,BGM,shop_bgm,Sound_Button
    open_canvas(600,800)
    image=load_image('shop_3.png')


def exit():
	global image
	close_canvas()
	del (image)


def update():
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 550, 643, 300, 400, 600, 800)
    #image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    global shop_bgm
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                print ( event.x,800-event.y)
                if(event.x> 16 and event.x< 88 and 800-event.y>39 and 800-event.y < 89):
                    game_framework.change_state(main_state)
                elif (event.x > 50 and event.x < 189 and 800 - event.y > 357 and 800 - event.y < 519):
                    #print("OKEY")
                    Player.Bullet(None)
                elif(event.x > 431 and event.x < 548 and 800 - event.y > 373 and 800 - event.y < 519):
                    if( Player.R_Hatch == True):
                        Player.L_Hatch = True
                    else:
                        Player.R_Hatch = True
                elif (event.x > 244 and event.x < 338 and 800 - event.y > 605 and 800 - event.y < 712):
                    Player.Protect=True
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

    pass


def pause(): pass


def resume(): pass




