import pyxel
REGULAR_ENEMY_EXPLOSION_HEIGHT = 16
REGULAR_ENEMY_EXPLOSION_WIDTH = 16
#This explosion corresponds to the bombardier
class RegularEnemyExplosion:
    list = []
    def __init__(self, x, y, going_down):
        # Each position represents a stage of the explosion
        # The numbers are related with the duration of that stage
        self.x = x
        self.y = y
        # Depending on if the enemy is going up or down one set of 'animations' or another
        #So we need to know if the enemy is going up or down
        self.first_stage = 12
        self.second_stage = 8
        self.third_stage = 8
        self.alive = True
        # Depending on if the enemy is going up or down one set of 'animations' or another
        # So we need to know if the enemy is going up or down
        self.going_down = going_down
        RegularEnemyExplosion.list.append(self)

    def update(self):
        if self.alive:
            if self.first_stage != 0:
                self.first_stage -= 1
            elif self.first_stage == 0 and self.second_stage != 0:
                self.second_stage -= 1
            elif self.first_stage == 0 and self.second_stage == 0 and self.third_stage != 0:
                self.third_stage -= 1
            if self.first_stage == 0 and self.second_stage == 0 and self.third_stage == 0:
                self.alive = False

    #Depending on what phase of the explosion it is it draws one thing
    def draw(self):
        if self.going_down == 0 or self.going_down == 2:
            if self.first_stage !=0:
                pyxel.blt(self.x, self.y, 1, 136, 0, -REGULAR_ENEMY_EXPLOSION_WIDTH, -REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)
            elif self.first_stage == 0 and self.second_stage != 0:
                pyxel.blt(self.x, self.y, 1, 152, 0, -REGULAR_ENEMY_EXPLOSION_WIDTH, -REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)
            elif self.first_stage == 0 and self.second_stage == 0 and self.third_stage != 0:
                pyxel.blt(self.x, self.y, 1, 168, 0, -REGULAR_ENEMY_EXPLOSION_WIDTH, -REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)
        # Regular enemy is going up
        else:
            if self.first_stage != 0:
                pyxel.blt(self.x, self.y, 1, 136, 16, REGULAR_ENEMY_EXPLOSION_WIDTH, REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)
            elif self.first_stage == 0 and self.second_stage != 0 :
                pyxel.blt(self.x, self.y, 1, 152, 16, REGULAR_ENEMY_EXPLOSION_WIDTH, REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)
            elif self.first_stage == 0 and self.second_stage == 0 and self.third_stage != 0:
                pyxel.blt(self.x, self.y, 1, 168, 16, REGULAR_ENEMY_EXPLOSION_WIDTH, REGULAR_ENEMY_EXPLOSION_HEIGHT, colkey = 15)

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == float or type(x) == int:
            self.__x = x
        else:
            raise TypeError("x type is not valid, must be int or float")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y: float):
        if type(y) == float or type(y) == int:
            self.__y = y
        else:
            raise TypeError("y type is not valid, must be int or float")

    @property
    def going_down(self):
        return self.__going_down

    @going_down.setter
    def going_down(self, going_down: int):
        if type(going_down) == int:
            self.__going_down = going_down
        else:
            raise TypeError("going_down type is not valid, it must be int")