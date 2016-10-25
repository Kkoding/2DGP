import game_framework

from pico2d import *
import Main

name = "TitleState"
image = None


def enter():
    global  image
    open_canvas(600,800)
    image=load_image('D:\\2-2\\2DGameProgramming\\0FlightResource\\BackGround\\Title.png')

def exit():
    global image
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
                game_framework.change_state(Main)
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass







def update():
    pass


def pause():
    pass


def resume():
    pass





