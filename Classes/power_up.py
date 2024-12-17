import pyxel
import random

POWER_UP_WIDTH = 8
POWER_UP_HEIGHT = 8
POWER_UP_SPEED = 2


class Power_up:
    list = []
    def __init__(self):
        self.x = random.randint(0, pyxel.width - POWER_UP_WIDTH)
        self.y = 0 - POWER_UP_HEIGHT
        self.w = POWER_UP_WIDTH
        self.h = POWER_UP_HEIGHT
        self.alive = True
        Power_up.list.append(self)

    def update(self):
        self.y += POWER_UP_SPEED
        if self.y - self.h> pyxel.height:
            self.alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 56, 112, self.w, self.h, colkey=0)