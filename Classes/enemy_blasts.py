import pyxel
WIDTH = 140
HEIGHT = 160
BLAST_WIDTH = 4
BLAST_HEIGHT = 4
BLAST_SPEED = 1.5
class Blast:
    blasts = []
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = BLAST_WIDTH
        self.h = BLAST_HEIGHT
        self.alive = True
        Blast.blasts.append(self)

    def update(self):
        for element in Blast.blasts:
            element.y += BLAST_SPEED/len(Blast.blasts)
            if element.y + element.h - 1 > HEIGHT:
                #The blast has left the map
                element.alive = False

    def draw(self):
        for element in Blast.blasts:
            pyxel.blt(element.x, element.y, 1, 48, 120, BLAST_WIDTH, BLAST_HEIGHT, colkey=0)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == float or type(x) == int:
            self.__x = x
        else:
            raise TypeError("x type is not valid, must be int or float")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        if type(y) == float or type(y) == int:
            self.__y = y
        else:
            raise TypeError("y type is not valid, must be int or float")
