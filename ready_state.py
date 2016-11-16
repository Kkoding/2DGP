import game_framework
import title_state

from pico2d import *



name = "ready_state"
image = None
logo_time = 0.0


BGM = None

def enter():
    global image,BGM
    open_canvas(600,800)
    image=load_image('shop_1.png')


def exit():
    global image
    close_canvas()
    del(image)
    pass


def update():
    global logo_time
   
    logo_time= logo_time+0.01
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 550, 643, 300, 400, 600, 800)
   # image.draw(400,300)
    update_canvas()
    pass




def handle_events():
    events=get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(Main)
    pass


def pause(): pass


def resume(): pass




