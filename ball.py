from pico2d import *
import game_world
import game_framework
import zombie

from game_world import add_collision_pair
from zombie import Zombie


class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1, isFly = False):
        self.isFly = isFly
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity, self.isFly = x, y, velocity, isFly


    def draw(self):
        self.image.draw(self.x, self.y)
        if self.isFly:

            draw_rectangle(*self.get_bb())

    def update(self):
        self.x += self.velocity * 100 * game_framework.frame_time

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)


    def get_bb(self):
        # fill here
        return self.x-10, self.y -10, self.x + 10, self.y +10


    def handle_collision(self, group, other):
        # fill here
        if group == 'boy:ball':
            game_world.remove_object(self)
        elif group == 'zombie:ball':
            if self.isFly:
                print('공 좀비 충돌')
                game_world.remove_object(self)
        pass