import game_framework
import select_state
import start_state

from pico2d import *


name = "TitleState"
image = None
image2=None
image3=None
BG_Sound=None
YPos=400
Y2Pos=1600

BGM = None
def enter():
    global  image,BG_Sound,image2,image3,YPos,Y2Pos
    open_canvas(600, 800)
    YPos=400
    Y2Pos=YPos+1200
    image=load_image('BackGround\\title1.png')
    image2 = load_image('BackGround\\01.png')
    image3 = load_image('BackGround\\01.png')
    global BGM
    BGM = load_music('Sound\\gameclear.mp3')
    BGM.set_volume(64)
    BGM.repeat_play()
    
    
def exit():
    global image,BG_Sound
    close_canvas()
    del(image)
   
def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(select_state)
    pass


def draw():
    global BG_Sound,image2,image3,YPos,Y2Pos
    clear_canvas()
    image3.clip_draw(0, 0, 800, 1200, 300, Y2Pos)
    image2.clip_draw(0, 0, 800, 1200, 300, YPos)
    image.clip_draw(0,0,384,512,300,400,600,800)
    #image.draw(192,256)
    update_canvas()
    delay(0.01)
    pass

def update():
    global YPos, Y2Pos
    YPos -= 2
    Y2Pos -= 2
    if YPos < -400:
        YPos = 400
    if Y2Pos < 800:
        Y2Pos = 1600
    pass


def pause():
    pass


def resume():
    pass






