from board import Board
from background import Background
from options import Options
import pyxel


WIDTH = 140
HEIGHT = 160
FPS = 60


class Menu:
    def __init__(self):
        pyxel.init(WIDTH, HEIGHT, fps=FPS, title="10942")
        self.background = Background(0)
        self.first = True
        self.Options = Options(self.first)
        self.Board = Board()
        self.start = False
        self.playing = False
        self.player_speed = 1
        self.times_played = 0
        self.score, self.high_score = 0, 0

        pyxel.load("sprites.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        #update the background

        if not self.playing:
            self.Options.update(self.first, self.score, self.high_score)
            self.background.update(self.player_speed)
            if pyxel.btn(pyxel.KEY_S) or pyxel.btn(pyxel.KEY_RETURN) and self.Options.option_selected==1:
                self.start = True
                self.background.planet_alive = False
                self.Options.alive=False
                if self.times_played>0:
                    self.Board = Board()
                self.times_played +=1
                self.first = False
                del self.background
                self.Options.option_selected=0
        #pressing q to quit
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_RETURN) and self.Options.option_selected==3:
            pyxel.quit()
        #instructions
        if pyxel.btn(pyxel.KEY_I) or pyxel.btn(pyxel.KEY_RETURN) and self.Options.option_selected==2:
            self.Options.instructions=True
            self.Options.sentence=1
        if self.Options.instructions:
            if pyxel.btn(pyxel.KEY_B):
                self.Options.instructions = False
        #for restarting the game
        if self.start:
            self.Board.update()
            if self.Board.alive:
                self.playing=True
            else:
                self.playing=False
                #for the points
                self.score = self.Board.points
                if self.score > self.high_score:
                    self.high_score = self.score
                del self.Board
                self.Options.alive = True
                self.Options.update(self.first, self.score, self.high_score)
                self.Options.delete()
        if not self.playing:
            if self.start:
                self.background = Background(0)
            self.start=False

    def draw(self):
        pyxel.cls(0)

        if self.playing:
            self.Board.draw()
        else:
            self.background.draw()
            self.Options.draw()