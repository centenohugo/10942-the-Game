import pyxel
from enemy_blasts import Blast
NUM_BOMBARDIERS = 1
BOMBARDIER_WIDTH = 32
BOMBARDIER_HEIGHT = 16
WIDTH = 140
HEIGHT = 160
Y_APPARITION_RANGE = -200
BOMBARDIER_SPEED= 0.15
BOMBARDIER_LIVES = 10
class Bombardier:
    list = []
    def __init__(self):
        self.x = pyxel.rndf(BOMBARDIER_WIDTH, WIDTH - BOMBARDIER_WIDTH)
        self.y = pyxel.rndf(Y_APPARITION_RANGE, -BOMBARDIER_HEIGHT)
        self.dx = pyxel.rndf(-0.5, 0.5)
        self.dy = BOMBARDIER_SPEED
        self.going_down = 0
        self.lives = BOMBARDIER_LIVES
        self.alive = True
        self.w = BOMBARDIER_WIDTH
        self.h = BOMBARDIER_HEIGHT
        Bombardier.list.append(self)

    def update(self):
        if self.alive:
            # lateral rebound
            if self.x < 0 or self.x > WIDTH - BOMBARDIER_WIDTH:
                self.dx = -self.dx
            # x movement
            self.x += self.dx
            # y movement
            self.y += self.dy
            # So it doesn't leave the screen by the lower part
            if self.y > HEIGHT:
                self.y = 0 - BOMBARDIER_HEIGHT
            shoot_no_shoot = pyxel.rndi(1, 50)
            if shoot_no_shoot == 1 and self.y > 0:
                Blast(self.x + BOMBARDIER_WIDTH / 2, self.y + BOMBARDIER_HEIGHT)

    def draw(self):
        if self.alive:
            pyxel.blt(self.x, self.y, 1, 0, 24, BOMBARDIER_WIDTH, BOMBARDIER_HEIGHT, colkey=15)