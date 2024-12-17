import pyxel
from enemy_blasts import Blast
NUM_SUPERBOMBARDIERS = 1
SUPERBOMBARDIER_WIDTH = 40
SUPERBOMBARDIER_HEIGHT = 40
WIDTH = 140
HEIGHT = 160
Y_APPARITION_RANGE = -200
SUPERBOMBARDIER_SPEED= 0.15
SUPERBOMBARDIER_LIVES = 30
class SuperBombardier:
    list = []
    def __init__(self):
        self.x = pyxel.rndf(SUPERBOMBARDIER_WIDTH, WIDTH - SUPERBOMBARDIER_WIDTH)
        self.y = pyxel.rndf(Y_APPARITION_RANGE, -SUPERBOMBARDIER_HEIGHT)
        self.dx = pyxel.rndf(-0.5, 0.5)
        self.dy = SUPERBOMBARDIER_SPEED
        self.going_down = 0
        self.lives = SUPERBOMBARDIER_LIVES
        self.alive = True
        self.w = SUPERBOMBARDIER_WIDTH
        self.h = SUPERBOMBARDIER_HEIGHT
        SuperBombardier.list.append(self)

    def update(self):
        if self.alive:
            # lateral rebound
            if self.x < 0 or self.x > WIDTH - SUPERBOMBARDIER_HEIGHT:
                self.dx = -self.dx
            # x movement
            self.x += self.dx
            # y movement
            self.y += self.dy
            # So it doesn't leave the screen by the lower part
            if self.y > HEIGHT:
                self.y = - SUPERBOMBARDIER_HEIGHT
                #Depends on what movement we want to implement to the bombardier

            #SuperBombardier shoots more often 1/20 chances of shooting per frame
            shoot_no_shoot = pyxel.rndi(1, 50)
            if shoot_no_shoot == 1 and self.y > 0:
                #The commented shot is deleted, very difficult to kill it
                #Blast(self.x + SUPERBOMBARDIER_WIDTH / 2, self.y + SUPERBOMBARDIER_HEIGHT)
                Blast(self.x, self.y + SUPERBOMBARDIER_HEIGHT)
                Blast(self.x +SUPERBOMBARDIER_WIDTH, self.y +SUPERBOMBARDIER_HEIGHT)
    def draw(self):
        if self.alive:
            pyxel.blt(self.x, self.y, 1, 0, 48, SUPERBOMBARDIER_WIDTH, SUPERBOMBARDIER_HEIGHT, colkey=15)