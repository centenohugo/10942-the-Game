import pyxel
import random
from player_bullet import Bullet
PLAYER_WIDTH = 16
PLAYER_HEIGHT = 19
player_speed = 1
lives = 3
#the x_bank is for the player loop(for the different sprites)
x_bank_list = (80, 112, 96, 48, 96, 128, 80, 64)
x_bank = x_bank_list[7]

#the x_bank is for the player loop(for the different sprites)
dying_x_bank_list = ((0,104,7,7), (10,104,12,12), (24,106,16,24))

class Player:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.lives = lives
        self.power_up = 0
        #for making the loop
        self.loops = 3
        self.imag = 0
        self.t_loop = 0
        self.x_bank = x_bank
        self.y_bank = 0
        self.x_bank_list = x_bank_list
        self.dying_x_bank_list = dying_x_bank_list
        self.looping = False
        self.can_shoot = True

        #for the explosion after dying
        self.dying = False
        self.t_dying = 0
        self.alive = True


    def update(self):
        #Speed defined as a constant so it is easier to modify when getting bonus
        if self.power_up>=2:
            player_speed=1.5
        else:
            player_speed=1

        if self.alive and not self.dying:
            if pyxel.btn(pyxel.KEY_LEFT):
                self.x -= player_speed
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += player_speed
            if pyxel.btn(pyxel.KEY_UP):
                self.y -= player_speed
            if pyxel.btn(pyxel.KEY_DOWN):
                self.y += player_speed
            if pyxel.btnp(pyxel.KEY_SPACE) and self.can_shoot:
                if self.power_up <1:
                    Bullet((self.x+PLAYER_WIDTH/2)-2, self.y)
                elif self.power_up<3:
                    Bullet((self.x + PLAYER_WIDTH / 2), self.y)
                    Bullet((self.x + PLAYER_WIDTH / 2) - 4, self.y)
                else:
                    Bullet((self.x + PLAYER_WIDTH / 2) - 2, self.y)
                    Bullet((self.x + PLAYER_WIDTH / 2) + 2, self.y)
                    Bullet((self.x + PLAYER_WIDTH / 2) - 6, self.y)
            if pyxel.btn(pyxel.KEY_Z) and not self.looping and self.loops>0:
                self.y -= 10
                self.looping = True
                self.can_shoot = False
                self.loops -=1

        if self.lives<=0:
            self.dying=True

        self.t_loop += 1
        #delay for the loop
        if self.looping and self.t_loop%20==0:
            self.loop()
            self.t_loop = 0

        self.t_dying +=1
        if self.dying and self.t_dying % 10 == 0:
            self.die()
            self.t_dying=0

        #So it doesn't leave the screen
        self.x = max(self.x, 0)
        self.x = min(self.x, pyxel.width - self.w)
        self.y = max(self.y, 12)
        self.y = min(self.y, pyxel.height - self.h)

    def draw(self):
        #different sprites if looping or dying
        if self.looping:
            pyxel.blt(self.x, self.y, 1, self.x_bank, 88, self.w, self.h,
                      colkey=15)
        elif self.dying:
            pyxel.blt(self.x, self.y, 1, self.x_bank, self.y_bank, self.w,
                      self.h, colkey=0)
        else:
            pyxel.blt(self.x, self.y, 1, 152+(pyxel.frame_count // 10 % 4)*16,
                      88, self.w, self.h, colkey=15)

    #method for the loop(it changes the player's sprite)
    def loop(self):
        self.x_bank = self.x_bank_list[(self.imag-1)]
        self.draw()
        self.imag+=1
        if self.imag <= 4:
            self.y +=10
        else:
            self.y-=10

        if self.imag == 8:
            self.looping=False
            self.can_shoot = True
            self.imag=0
        if self.imag >=6:
            self.can_shoot = True

    #die animation
    def die(self):
        if self.imag >=3:
            self.alive=False
            self.imag = 0
        else:
            self.x_bank = self.dying_x_bank_list[self.imag][0]
            self.y_bank = self.dying_x_bank_list[self.imag][1]
            self.w = self.dying_x_bank_list[self.imag][2]
            self.h = self.dying_x_bank_list[self.imag][3]
            self.draw()
            self.imag += 1