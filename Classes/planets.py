import pyxel
import random

PLANET_SPEED = 0.5
PLANET_SELECTION = ((64,112,16,16), (80,112,16,16), (96,112,16,16), (116,114,25,14))

class Planet:
    list = []
    def __init__(self):
        self.type = random.randint(0, 3)
        self.w = PLANET_SELECTION[self.type][2]
        self.h = PLANET_SELECTION[self.type][3]
        self.x = random.randint(0 - (self.w//2), pyxel.width - (self.w//2))
        self.y = 0 - self.h
        self.alive = True
        Planet.list.append(self)

    def update(self, player_speed):
        self.y += PLANET_SPEED * player_speed
        if self.y - self.h> pyxel.height:
            self.alive = False

    def draw(self):
        pyxel.blt(self.x, self.y, 1, PLANET_SELECTION[self.type][0], 
                  PLANET_SELECTION[self.type][1], self.w, self.h, colkey=0)