import game_framework
import ready_state
import title_state

from pico2d import *



name = "LoseState"
image = None
image2=None
image3=None
logo_time = 0.0


BGM = None
YPos=400
Y2Pos=1600
def enter():
    global image,image2,image3,YPos,Y2Pos
    open_canvas(600,800)
    YPos=400
    Y2Pos=YPos+1200
    image=load_image('BackGround\\gameover.png')
    image2 = load_image('BackGround\\01.png')
    image3 = load_image('BackGround\\01.png')
    global BGM
   # BGM = load_music('Sound\\boss_background.mp3')
   # BGM.set_volume(64)
   # BGM.repeat_play()
    pass


def exit():
    global image,BGM,image2
    close_canvas()
    del(image)
    del(image2)
    del(BGM)
    pass


def update():
    global logo_time,YPos,Y2Pos
    YPos-=2
    Y2Pos-=2
	
	    
    if(logo_time>2.0):
        logo_time=0
       #game_framework.quit()
        game_framework.push_state(ready_state)
    delay(0.01)
    logo_time= logo_time+0.01
    pass


def draw():
    global image,YPos,image3,image2
    clear_canvas()
    image3.clip_draw(0, 0, 800, 1200, 300, Y2Pos)
    image2.clip_draw(0, 0, 800, 1200, 300, YPos)
    image.clip_draw(0, 0, 550, 643, 300, 400)
   # image.draw(400,300)
    update_canvas()
    pass




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




