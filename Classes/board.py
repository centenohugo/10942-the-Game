import pyxel
import random
from player import Player
from background import  Background
from player_bullet import Bullet
from power_up import Power_up
from lives import Lives
from scoreboard import Scoreboard
from loop_counter import Counter
from enemy_blasts import Blast
from enemies import Enemy
from regularenemy import RegularEnemy
from bombardier import Bombardier
from superbombardier import SuperBombardier
from redenemy import RedEnemy
from bombardierexplosion import BombardierExplosion
from regularenemyexplosion import RegularEnemyExplosion

WIDTH = 140
HEIGHT = 160


class Board:
    def __init__(self):
        self.player = Player(pyxel.width / 2, pyxel.height - 20)
        self.width = WIDTH
        self.height = HEIGHT
        self.points = 0
        self.background = Background(0)
        self.background.planet_alive=False
        self.player = Player(WIDTH - 80, HEIGHT - 20)
        self.player_speed = 1
        self.enemies = Enemy()

        #score ,lives  and loop counters
        self.lives_list = []
        for i in range(3):
            self.lives_list.append(Lives(i+1))
        self.scoreboard = Scoreboard(0)
        self.counter = Counter(3)

        #random timing for power up
        self.t_power_up = 0
        self.rand_power_up = random.randint(1000, 2000)
        self.alive = True

    def update(self):
        #player speed for second power up(for the speed of the backgound
        # stars and planets)
        self.background.update(self.player_speed)

        #update scores
        for l in Lives.list:
            l.update(self.player.lives)
        self.scoreboard.update(self.points)
        self.counter.update(self.player.loops)

        #for the background speed
        if self.player.power_up>=2:
            self.player_speed=2
        else:
            self.player_speed=1

        #timer for spawning random power up
        self.t_power_up += 1
        if self.t_power_up % self.rand_power_up == 0:
            Power_up()
            self.t_power_up=0
            self.rand_power_up = random.randint(500, 1000)

        self.player.update()
        self.enemies.update()
        self.points = self.enemies.points

        for b in Bullet.list:
            b.update()
        for bl in Blast.blasts:
            bl.update()
        for p in Power_up.list:
            p.update()

        if not self.player.alive:
            self.dying()
            self.alive=False


        self.clean_bullets()
        self.clean_blasts()
        self.clean_power_ups()
        self.enemy_hit()
        #for not being damaged while looping
        if not self.player.looping and self.player.alive:
            self.touching_power_up()
            self.player_hit()
            self.collision()

    def draw(self):
        pyxel.cls(0)
        self.background.draw()

        #draw lives and points
        for l in Lives.list:
            l.draw()
        self.scoreboard.draw()
        self.counter.draw()

        self.player.draw()
        self.enemies.draw()

        for b in Bullet.list:
            b.draw()
        for bl in Blast.blasts:
            bl.draw()
        for p in Power_up.list:
            p.draw()

    def clean_bullets(self):
        i = 0
        while i<len(Bullet.list):
            if not Bullet.list[i].alive:
                Bullet.list.pop(i)
            else:
                i += 1

    def clean_blasts(self):
        i = 0
        while i<len(Blast.blasts):
            if not Blast.blasts[i].alive:
                Blast.blasts.pop(i)
            else:
                i += 1

    def clean_power_ups(self):
        i = 0
        while i<len(Power_up.list):
            if not Power_up.list[i].alive:
                Power_up.list.pop(i)
            else:
                i += 1

    #if the player makes contact with the power up
    def touching_power_up(self):
        for p in Power_up.list:
            if (
                    self.player.x + self.player.w > p.x
                    and p.x + p.w > self.player.x
                    and self.player.y + self.player.h > p.y
                    and p.y + p.h > self.player.y
            ):
                if self.player.power_up<3:
                    self.player.power_up += 1
                elif self.player.loops<9:
                    self.player.loops +=1

                p.alive = False

    #if the player has been hit
    def player_hit(self):
        for bl in Blast.blasts:
            if (
                    self.player.x + self.player.w > bl.x
                    and bl.x + bl.w > self.player.x
                    and self.player.y + self.player.h > bl.y
                    and bl.y + bl.h > self.player.y
            ):
                bl.alive = False
                self.player.lives-=1

    def enemy_hit(self):
        for bul in Bullet.list:
            for en in Enemy.list:
                if (bul.x + bul.w > en.x and bul.x < en.x + en.w and bul.y + bul.h > en.y and bul.y < en.y + en.h):
                    bul.alive = False

    def collision(self):
        for en in RegularEnemy.list:
            if (
                    self.player.x + self.player.w > en.x
                    and en.x + en.w > self.player.x
                    and self.player.y + self.player.h > en.y
                    and en.y + en.h > self.player.y
            ) and not self.player.dying:
                self.player.lives-=1
                RegularEnemyExplosion(en.x, en.y, en.going_down)
                en.alive = False

        for en in RedEnemy.list:
            if (
                    self.player.x + self.player.w > en.x
                    and en.x + en.w > self.player.x
                    and self.player.y + self.player.h > en.y
                    and en.y + en.h > self.player.y
            ) and not self.player.dying:
                BombardierExplosion(en.x + 6, en.y + 2)
                self.player.lives-=1
                en.alive = False

        for en in Bombardier.list:
            if (
                    self.player.x + self.player.w > en.x
                    and en.x + en.w > self.player.x
                    and self.player.y + self.player.h > en.y
                    and en.y + en.h > self.player.y
            ) and not self.player.dying:
                self.player.lives-=2
                BombardierExplosion(en.x + 6 , en.y + 2)
                en.alive = False

        for en in SuperBombardier.list:
            if (
                    self.player.x + self.player.w > en.x
                    and en.x + en.w > self.player.x
                    and self.player.y + self.player.h > en.y
                    and en.y + en.h > self.player.y
            ) and not self.player.dying:
                self.player.lives-=3

                BombardierExplosion(en.x, en.y)
                BombardierExplosion(en.x + 12, en.y)
                BombardierExplosion(en.x, en.y + 12)
                BombardierExplosion(en.x + 12, en.y + 12)
                en.alive = False

    def dying(self):
        self.scoreboard.delete()
        RegularEnemy.list = []
        RedEnemy.list = []
        Bombardier.list = []
        SuperBombardier.list = []
        Enemy.list = []
        BombardierExplosion.list = []
        RegularEnemyExplosion.list = []
        Blast.blasts = []
        Bullet.list = []
        Power_up.list = []
        del self.counter
        del self.lives_list