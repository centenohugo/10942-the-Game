import pyxel

NUMBER_WIDTH = 5
NUMBER_HEIGHT = 8

class Number:
    list = []
    list2, list3 = [], []
    def __init__(self, x, y, num: int, list):
        self.x = x
        self.y = y
        self.w = NUMBER_WIDTH
        self.h = NUMBER_HEIGHT
        self.num = num
        self.alive = True
        #lits one for score and loop counter, list 2 and 3 for highscores
        if list==1:
            Number.list.append(self)
        elif list==2:
            Number.list2.append(self)
        elif list ==3:
            Number.list3.append(self)

    def update(self, num):
        self.num = num
        self.draw()

    def draw(self):
        pyxel.blt(self.x, self.y, 1,(184+6*self.num), 0, self.w, self.h,
                  colkey=0)