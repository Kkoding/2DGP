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
image2=None
image3=None
YPos=400
Y2Pos=1600

def enter():
    global image,BGM,shop_bgm,Sound_Button,image2,image3,YPos,Y2Pos
    YPos=400
    Y2Pos=YPos+1200
    open_canvas(600,800)
    image=load_image('BackGround\\shop_33.png')
    global BGM
    BGM = load_music('Sound\\gameclear.mp3')
    BGM.set_volume(64)
    BGM.repeat_play()
    image2 = load_image('BackGround\\01.png')
    image3 = load_image('BackGround\\01.png')
    

def exit():
    global image,image2,image3
    del (image)
    del (image2)
    del (image3)
    close_canvas()
    

def update():
    global YPos,Y2Pos
    YPos-=2
    Y2Pos-=2
    if YPos <-400:
        YPos=400
    if Y2Pos <800:
        Y2Pos = 1600
    delay(0.01)
    pass


def draw():
    global image,Y2Pos,YPos,image3,image2
    clear_canvas()
    image3.clip_draw(0, 0, 800, 1200, 300, Y2Pos)
    image2.clip_draw(0, 0, 800, 1200, 300, YPos)
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
               # print ( event.x,800-event.y)
                if(event.x> 16 and event.x< 88 and 800-event.y>39 and 800-event.y < 89):
                    game_framework.change_state(main_state)
                elif (event.x > 50 and event.x < 189 and 800 - event.y > 357 and 800 - event.y < 519):
                    #print("OKEY")
                    Player.Bullet(None)
                    Player.Money-=1
                elif(event.x > 431 and event.x < 548 and 800 - event.y > 373 and 800 - event.y < 519):
                    Player.Money -= 1
                    if( Player.R_Hatch == True):
                        Player.L_Hatch = True
                    else:
                        Player.R_Hatch = True
                elif (event.x > 244 and event.x < 338 and 800 - event.y > 605 and 800 - event.y < 712):
                    Player.Protect=True
                    Player.Money -= 1
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(main_state)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

    pass


def pause(): pass


def resume(): pass




