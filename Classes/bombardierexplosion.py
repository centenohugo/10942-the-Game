import pyxel
BOMBARDIER_EXPLOSION_HEIGHT = 16
BOMBARDIER_EXPLOSION_WIDTH = 16
#This explosion corresponds to the bombardier and to the superbombardier
class BombardierExplosion:
    list = []
    def __init__(self, x, y):
        # Each position represents a stage of the explosion
        # The numbers are related with the duration of that stage
        self.x = x
        self.y = y
        self.first_stage = 18
        self.second_stage = 12
        self.third_stage = 12
        self.alive = True
        BombardierExplosion.list.append(self)

    def update(self):
        if self.alive:
            if self.first_stage != 0:
                self.first_stage -= 1
            elif self.first_stage == 0 and self.second_stage != 0:
                self.second_stage -= 1
            elif self.first_stage == 0 and self.second_stage == 0 and self.third_stage != 0:
                self.third_stage -= 1
            if self.first_stage == 0 and self.second_stage == 0 and self.third_stage == 0:
                self.alive = False

    #Depending on what phase of the explosion it is it draws one thing
    def draw(self):
        if self.first_stage != 0:
            pyxel.blt(self.x, self.y, 1, 32, 88, BOMBARDIER_EXPLOSION_WIDTH, BOMBARDIER_EXPLOSION_HEIGHT, colkey = 0)
        elif self.first_stage == 0 and self.second_stage != 0:
            pyxel.blt(self.x, self.y, 1, 16, 88, BOMBARDIER_EXPLOSION_WIDTH, BOMBARDIER_EXPLOSION_HEIGHT, colkey = 0)
        elif self.first_stage == 0 and self.second_stage == 0 and self.third_stage != 0:
            pyxel.blt(self.x, self.y, 1, 0, 88, BOMBARDIER_EXPLOSION_WIDTH, BOMBARDIER_EXPLOSION_HEIGHT, colkey = 0)

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