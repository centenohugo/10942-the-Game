import pyxel
from enemy_blasts import Blast
REGULAR_ENEMY_WIDTH = 16
REGULAR_ENEMY_HEIGHT = 16
WIDTH = 140
HEIGHT = 160
Y_APPARITION_RANGE = -200
class RegularEnemy:
    list = []
    def __init__(self):
        self.x = pyxel.rndf(REGULAR_ENEMY_WIDTH, WIDTH - REGULAR_ENEMY_WIDTH)
        self.y = pyxel.rndf(Y_APPARITION_RANGE, -REGULAR_ENEMY_HEIGHT)
        self.dx = pyxel.rndf(-1, 1)
        self.dy = pyxel.rndf(0.1, 1)
        self.going_down = 0
        self.alive = True
        self.w = REGULAR_ENEMY_WIDTH
        self.h = REGULAR_ENEMY_HEIGHT
        RegularEnemy.list.append(self)

            # A list for every enemy character is appended to the list. Each enemy has a tuple of 6 values.
            # (float, float, float, float, 0, True)
            # x position
            # y position
            # x velocity
            # y velocity
            # 0: not arrived to the center, 1: arrived and not rebound, 2: arrived and rebound
            # True, is alive

    def update(self):
        #Check that enemy is alive
        if self.alive:
             #lateral rebound
            if self.x < 0 or self.x > WIDTH - REGULAR_ENEMY_WIDTH:
                 self.dx = -self.dx
            # x movement
            self.x += self.dx
            # y movement
            self.y += self.dy
            #It appears again if it is alive
            if self.y > HEIGHT and self.going_down == 2:
                 self.y = -REGULAR_ENEMY_HEIGHT
                 self.going_down = 0
            '''if self.y < -REGULAR_ENEMY_HEIGHT and self.going_down == 1:
                self.dy = -self.dy
                self.going_down = 0 '''

            if self.y > HEIGHT / 2 - REGULAR_ENEMY_HEIGHT and self.going_down == 0:
                # 0.5 chances of returning or keep on moving when it reaches half of the screen
                rebound = pyxel.rndi(1, 2)
                self.going_down = rebound
                if rebound == 1:
                    self.dy = -self.dy
            #If it has rebounded and hasn't been killed appears again
            if self.going_down == 1 and self.y < -REGULAR_ENEMY_HEIGHT:
                    self.dy = -self.dy
                    self.going_down = 0
            #Shooting: only enemies going down
            if self.going_down == 0 or self.going_down == 2:
                #Only the ones above or almost above the player. Prob of 0.1
                shoot_no_shoot = pyxel.rndi(1, 100)
                if shoot_no_shoot == 1 and self.y > 0:
                    Blast(self.x + REGULAR_ENEMY_WIDTH / 2, self.y + REGULAR_ENEMY_HEIGHT)


    def draw(self):
        if self.alive:
            if self.going_down == 1:
                pyxel.blt(self.x, self.y, 1, 16, 0, REGULAR_ENEMY_WIDTH, REGULAR_ENEMY_HEIGHT, colkey=15)
            else:
                pyxel.blt(self.x, self.y, 1, 0, 0, -REGULAR_ENEMY_WIDTH, -REGULAR_ENEMY_HEIGHT, colkey=15)


