import game_framework
import select_state

from pico2d import *
import Main

name = "TitleState"
image = None
BG_Sound=None



def enter():
    global  image,BG_Sound
    open_canvas(600,800)
    image=load_image('D:\\2-2\\2DGP\\BackGround\\Title.png')
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
    global BG_Sound
    
 
    clear_canvas()
    image.clip_draw(0,0,384,512,300,400,600,800)
    #image.draw(192,256)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass






