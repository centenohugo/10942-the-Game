import pyxel

HEART_WIDTH = 10
HEART_HEIGHT = 9

class Lives:
    list=[]
    def __init__(self, heart_num:int):
        self.x = pyxel.width - 11*heart_num
        self.y = 1
        self.w = HEART_WIDTH
        self.h = HEART_HEIGHT
        self.heart_num = heart_num
        self.life = True
        self.alive = True

        Lives.list.append(self)

    def update(self, player_lives):
        if player_lives<self.heart_num:
            self.life = False

    def draw(self):
        if self.life:
            pyxel.blt(self.x, self.y, 1, 90, 0, self.w, self.h, colkey=0)
        else:
            pyxel.blt(self.x, self.y, 1, 90, 16, self.w, self.h, colkey=1)
