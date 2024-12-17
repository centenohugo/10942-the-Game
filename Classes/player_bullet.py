import pyxel
BULLET_WIDTH = 3
BULLET_HEIGHT = 8
BULLET_SPEED = 3.5

class Bullet:
    list=[]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.alive = True
        Bullet.list.append(self)

    def update(self):
        self.y -= BULLET_SPEED
        if self.y + self.h < 0:
            self.alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 1, 48, 112, self.w, self.h,
                  colkey=0)
