import pyxel
from numbers import Number

class Scoreboard:
    def __init__(self, points):
        self.scoreboard_list= [0,0,0,0,0,0]
        self.points = points
        for i in range(len(self.scoreboard_list)):
            Number(2 + i * 6, 2, self.scoreboard_list[i], 1)

    def update(self, points):
        if points > 999999:
            points = 999999
        self.update_list(points)
        for n in range(len(self.scoreboard_list)):
            Number.list[n].update(self.scoreboard_list[n])

    def draw(self):
        for n in Number.list:
            n.draw()

    def update_list(self, points):
        str_points = str(points)
        if len(str_points)<6:
            for i in range(6-len(str_points)):
                str_points= "0"+str_points
        for i in range(len(str_points)):
            self.scoreboard_list[i]=int(str_points[i])

    def delete(self):
        for i in range(len(self.scoreboard_list)):
            self.scoreboard_list.pop(0)
        for n in range(len(Number.list)):
            Number.list.pop(0)

