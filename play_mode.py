import random

from pico2d import *
from pygame.examples.go_over_there import balls

import game_framework

import game_world
import zombie
from game_world import add_collision_pair
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init(flyball=None):
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


    balls = [Ball(random.randint(100,1500),60,0, False) for _ in range(30)]
    game_world.add_objects(balls,1)


    zombie = Zombie()
    game_world.add_object(zombie, 1)
    # fill here

    # 충돌 대상들 등록해주기
    add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        print('공들 등록')
        add_collision_pair('boy:ball',None,ball)

    add_collision_pair('boy:zombie', boy, zombie)

    add_collision_pair('zombie:ball', zombie, None)
    add_collision_pair('zombie:ball', zombie, flyball)

    # { 'boy:ball' : [boy], [ball1, ball2, .... ball30 이런식] }

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    # fill here

    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

