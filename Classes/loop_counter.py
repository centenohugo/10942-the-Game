import pyxel
from numbers import Number


COUNTER_WIDTH = 11
COUNTER_HEIGHT = 9

class Counter:
    def __init__(self, loops):
        self.w = COUNTER_WIDTH
        self.h = COUNTER_HEIGHT
        self.x = pyxel.width - self.w - 10
        self. y = pyxel.height - self.h - 2
        self.alive = True
        self.count = Number(self.x + 13, self.y + 1, loops, 1)

    def update(self, loops):
        self.count.update(loops)

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 185, 9, self.w, self.h, colkey=0)


