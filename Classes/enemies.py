import pyxel
from enemy_blasts import Blast
import random
from regularenemy import RegularEnemy
from bombardier import Bombardier
from superbombardier import SuperBombardier
from redenemy import RedEnemy
from bombardierexplosion import BombardierExplosion
from regularenemyexplosion import RegularEnemyExplosion
from player_bullet import Bullet

FPS = 60
FIRST_STAGE = 2 * FPS
SECOND_STAGE = 15 * FPS
THIRD_STAGE = 30 * FPS
FORTH_STAGE = 50 * FPS

NUM_REGULAR_ENEMIES = 20
NUM_RED_ENEMIES = 5

class Enemy:
    list = []
    def __init__(self):
        self.points = 0
        self.frame_count = 0


    def update(self):
        self.frame_count += 1
        if self.frame_count == FIRST_STAGE:
            for i in range(5):
                Enemy.list.append(RegularEnemy())
                Enemy.list[i].type = 1
        if self.frame_count == SECOND_STAGE:
            for i in range(5):
                Enemy.list.append(RegularEnemy())
            for i in range(NUM_RED_ENEMIES):
                Enemy.list.append(RedEnemy(20 * (i - 1)))
        if self.frame_count == THIRD_STAGE:
            for i in range(8):
                Enemy.list.append(RegularEnemy())
            Enemy.list.append(Bombardier())
        if self.frame_count == FORTH_STAGE:
            for i in range(10):
                Enemy.list.append(RegularEnemy())
            Enemy.list.append(SuperBombardier())

        if self.frame_count >=3000 and len(Enemy.list) == 0:
            for i in range(NUM_REGULAR_ENEMIES):
                Enemy.list.append(RegularEnemy())
            #for periodic random spawning of enemies
            if random.randint(1,3) == 1:
                for i in range(NUM_RED_ENEMIES):
                    Enemy.list.append(RedEnemy(20 * (i - 1)))
            if random.randint(1,3) == 1:
                Enemy.list.append(Bombardier())
            if random.randint(1,3) == 1:
                Enemy.list.append(SuperBombardier())



        for re in RegularEnemy.list:
            re.update()
        for red in RedEnemy.list:
            red.update()
        for bomb in Bombardier.list:
            bomb.update()
        for sup in SuperBombardier.list:
            sup.update()
        for exp in BombardierExplosion.list:
            exp.update()
        for exp2 in RegularEnemyExplosion.list:
            exp2.update()

        self.clean_enemies()
        self.clean_regular_enemies()
        self.clean_red_enemies()
        self.clean_bombardier()
        self.clean_superbombardier()
        self.clean_bombardierexplosion()
        self.clean_regularenemyexplosion()
        self.enemy_hit()
        self.red_enemy_hit()
        self.bombardier_hit()
        self.superbombardier_hit()

    def draw(self):

        for re in RegularEnemy.list:
            re.draw()
        for red in RedEnemy.list:
            red.draw()
        for bomb in Bombardier.list:
            bomb.draw()
        for sup in SuperBombardier.list:
            sup.draw()
        for exp in BombardierExplosion.list:
            exp.draw()
        for exp2 in RegularEnemyExplosion.list:
            exp2.draw()


    def clean_enemies(self):
        i = 0
        while i<len(Enemy.list):
            if not Enemy.list[i].alive:
                Enemy.list.pop(i)
            else:
                i += 1


    def clean_regular_enemies(self):
        i = 0
        while i<len(RegularEnemy.list):
            if not RegularEnemy.list[i].alive:
                RegularEnemy.list.pop(i)
                self.points += 10
            else:
                i += 1

    def clean_red_enemies(self):
        i = 0
        while i<len(RedEnemy.list):
            if not RedEnemy.list[i].alive:
                RedEnemy.list.pop(i)
                self.points += 25
            else:
                i += 1

    def clean_bombardier(self):
        i = 0
        while i<len(Bombardier.list):
            if not Bombardier.list[i].alive:
                Bombardier.list.pop(i)
                self.points += 100
            else:
                i += 1

    def clean_superbombardier(self):
        i = 0
        while i < len(SuperBombardier.list):
            if not SuperBombardier.list[i].alive:
                SuperBombardier.list.pop(i)
                self.points += 200
            else:
                i += 1

    def clean_bombardierexplosion(self):
        i = 0
        while i<len(BombardierExplosion.list):
            if not BombardierExplosion.list[i].alive:
                BombardierExplosion.list.pop(i)
            else:
                i += 1
    def clean_regularenemyexplosion(self):
        i = 0
        while i<len(RegularEnemyExplosion.list):
            if not RegularEnemyExplosion.list[i].alive:
                RegularEnemyExplosion.list.pop(i)
            else:
                i += 1


    def enemy_hit(self):
        for bul in Bullet.list:
            for re in RegularEnemy.list:
                if (bul.x + bul.w > re.x and bul.x < re.x + re.w and
                            bul.y + bul.h > re.y and bul.y < re.y + re.h):
                    re.alive = False
                    RegularEnemyExplosion(re.x, re.y, re.going_down)


    def red_enemy_hit(self):
        for bul in Bullet.list:
            for red in RedEnemy.list:
                if (bul.x + bul.w > red.x and bul.x < red.x + red.w and
                            bul.y + bul.h > red.y and bul.y < red.y + red.h):
                    BombardierExplosion(red.x + 6, red.y + 2)
                    red.alive = False


    def bombardier_hit(self):
        for bul in Bullet.list:
            for bomb in Bombardier.list:
                if (bul.x + bul.w > bomb.x and bul.x < bomb.x + bomb.w and
                            bul.y + bul.h > bomb.y and bul.y < bomb.y + bomb.h):
                    bomb.lives = bomb.lives - 1
                    if bomb.lives == 0:
                        BombardierExplosion(bomb.x + 6 , bomb.y + 2)
                        bomb.alive = False


    def superbombardier_hit(self):
        for bul in Bullet.list:
            for sup in SuperBombardier.list:
                if (bul.x + bul.w > sup.x and bul.x < sup.x + sup.w and
                            bul.y + bul.h > sup.y and bul.y < sup.y + sup.h):
                    sup.lives = sup.lives - 1
                    if sup.lives == 0:
                        BombardierExplosion(sup.x, sup.y)
                        BombardierExplosion(sup.x + 12, sup.y)
                        BombardierExplosion(sup.x, sup.y + 12)
                        BombardierExplosion(sup.x + 12, sup.y + 12)
                        sup.alive = False