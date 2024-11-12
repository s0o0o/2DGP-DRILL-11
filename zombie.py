import random
import math
import game_framework
import game_world
import game_world

from pico2d import *

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10.0

animation_names = ['Walk']

zombieSize = 200
zombieY = 0

class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombie/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]

    def __init__(self):
        self.x, self.y = random.randint(1600-800, 1600), 150
        self.load_images()
        self.frame = random.randint(0, 9)
        self.dir = random.choice([-1,1])


    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += RUN_SPEED_PPS * self.dir * game_framework.frame_time
        if self.x > 1600:
            self.dir = -1
        elif self.x < 800:
            self.dir = 1
        self.x = clamp(800, self.x, 1600)
        pass


    def draw(self):
        global zombieSize
        if self.dir < 0:
            Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y - zombieY, zombieSize, zombieSize)
        else:
            Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y- zombieY, zombieSize, zombieSize)
        #draw_rectangle(*self.get_bb())


    def handle_event(self, event):
        pass

    def get_bb(self):
        # fill here
        # 4개의 값, x1,x2,y1,y2
        return self.x - 60 , self.y - 70, self.x + 60, self.y + 100

    def handle_collision(self, group, other):
        # fill here
        global zombieSize, zombieY
        if group == 'zombie:ball':
            print('공 좀비 충돌')
            zombieSize -= 100
            zombieY += 50
            if zombieSize < 100:
                game_world.remove_object(self)


        if group == 'boy:zombie':
            print('좀비랑 소년 충돌')
            game_framework.quit()