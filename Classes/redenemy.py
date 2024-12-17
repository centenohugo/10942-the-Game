import pyxel
from enemy_blasts import Blast
RED_ENEMY_WIDTH = 16
RED_ENEMY_HEIGHT = 16
WIDTH = 140
HEIGHT = 160
RADIUS = WIDTH / 6
SPEED = 3
class RedEnemy:
    list = []
    def __init__(self, t):
        self.t = t
        self.x = self.position_x(t)
        self.y = self.position_y(t)
        self.dt = SPEED
        self.w = RED_ENEMY_WIDTH
        self.h = RED_ENEMY_HEIGHT
        self.alive = True
        RedEnemy.list.append(self)

    # A list for every enemy character is appended to the list. Each enemy has a tuple of 6 values.
    # (float, float, float, float, 0, True)
    # x position
    # y position
    # x velocity
    # y velocity
    # 0: not arrived to the center, 1: arrived and not rebound, 2: arrived and rebound
    # True, is alive


    # The formation is defined thanks to a piecewise function
    # t refers to its kind of x position, like a position on a railway, being the railway the shape
    # we want them to follow
    def position_x(self, t):
        tp = t
        if t > 200 and t <= 300:
            tp = 200
        if t > 300:
            tp = t - 100
        if t > 500:
            tp = t - 200
        if t > 400 and t<= 500:
            tp = 300
        x = -(WIDTH / 3 ) + (WIDTH / 300) * tp
        if (t > 200 and t <= 300) or (t > 400 and t<= 500):
            x = x + RADIUS * pyxel.sin(3.6 * (t - tp))
        return x

    def position_y(self, t):
        tp = t
        y = HEIGHT / 3
        if t > 200 and t <= 300:
            tp = 200
        if t > 300:
            tp = t - 100
        if t > 400 and t <= 500:
            tp = 400
        if t > 500:
            tp = t - 200
        if (t > 200 and t <= 300) or (t > 400 and t <= 500):
            y = y - RADIUS * (pyxel.cos(3.6 * (t - tp)) - 1)

        return y

    def update(self):
        #Check that enemy is alive
        if self.alive:
            self.t = self.t + self.dt
            if self.t>700:
                self.t=0
            self.x = self.position_x(self.t)
            self.y = self.position_y(self.t)
            shoot_no_shoot = pyxel.rndi(1, 400)
            if shoot_no_shoot == 1 and self.y > 0:
                Blast(self.x, self.y + RED_ENEMY_HEIGHT / 2)


    def draw(self):
        if self.alive:
            pyxel.blt(self.x, self.y, 1, 32, 24, self.w, self.h,
                      colkey=15)

    @property
    def t(self):
        return self.__t

    @t.setter
    def t(self, t):
        if type(t) == float or type(t) == int:
            self.__t = t
        else:
            raise TypeError("t type is not valid, must be int or float")


