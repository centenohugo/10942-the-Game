import pyxel
from planets import Planet
import random
NUM_STARS = 100
STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5
WIDTH = 140
HEIGHT = 160
class Background:
    def __init__(self, points):
        self.stars = []
        self.points = points
        self.planet_alive = True
        for i in range(NUM_STARS):
            self.stars.append(
                (
                    pyxel.rndi(0, 140 - 1),
                    pyxel.rndi(0, 160 - 1),
                    pyxel.rndf(1, 2.5),
                )
            )
        self.t_planets = 100

    def update(self, player_speed):
        for i, (x, y, speed) in enumerate(self.stars):
            #to increase the speed after second power up
            y += (speed * player_speed)/2
            if y >= HEIGHT:
                y -= HEIGHT
            self.stars[i] = (x, y, speed)

        #counter for the random background planets
        self.t_planets -= 1
        if self.planet_alive:
            if self.t_planets <= 0:
                Planet()
                self.t_planets = random.randint(150, 300)
        else:
            if self.t_planets <= 0:
                Planet()
                self.t_planets = random.randint(600, 800)
        for pl in Planet.list:
            pl.update(player_speed)

        self.clean_planets()


    def draw(self):
        # draw background planets
        for pl in Planet.list:
            pl.draw()

        for (x, y, speed) in self.stars:
            pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)

    #delete the planets
    def clean_planets(self):
        i = 0
        while i<len(Planet.list):
            if not Planet.list[i].alive:
                Planet.list.pop(i)
            else:
                i += 1