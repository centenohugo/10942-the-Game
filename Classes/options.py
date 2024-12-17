import pyxel
from numbers import Number

TITLE_WIDTH = 76
TITLE_HEIGHT = 22

class Options:
    def __init__(self, first):
        self.alive = True
        self.option_selected = 1 #1 for playing, 2 for intructions, 3 to quit
        self.first = first #first time playing
        self.score, self.highscore = 0, 0
        self.score_list = [0, 0, 0, 0, 0, 0]
        self.highscore_list = [0, 0, 0, 0, 0, 0]
        self.instructions = False
        self.sentence = 1 #for the instructions

    def update(self, first, score, highscore):
        if not self.alive:
            self.delete()
        else:
            #to move in the menu
            self.first = first
            if self.first:
                if not self.instructions:
                    if pyxel.btnp(pyxel.KEY_UP):
                        if self.option_selected==1:
                            self.option_selected=3
                        else:
                            self.option_selected-=1
                    if pyxel.btnp(pyxel.KEY_DOWN):
                        if self.option_selected == 3:
                            self.option_selected = 1
                        else:
                            self.option_selected += 1
                else:
                    #for the instructions
                    if pyxel.btnp(pyxel.KEY_RIGHT):
                        if self.sentence == 4:
                            self.instructions=False
                        else:
                            self.sentence +=1
            else:
                self.score = score
                self.update_list(self.score_list, self.score)
                for i in range(len(self.score_list)):
                    Number(58 + i * 6, 52, self.score_list[i], 2)

                self.highscore = highscore
                self.update_list(self.highscore_list, self.highscore)
                for i in range(len(self.highscore_list)):
                    Number(90 + i * 6, 72, self.highscore_list[i], 3)

    def draw(self):
        if self.alive:
            if self.first:
                #Title
                pyxel.blt((pyxel.width-TITLE_WIDTH)/2, 20, 1, 152, 120,
                          TITLE_WIDTH,TITLE_HEIGHT,colkey=0)

                if not self.instructions:
                    #Press enter
                    pyxel.blt((pyxel.width-52)/2, 140, 1,
                              2+(pyxel.frame_count // 30 % 2) * 52,
                              220, 52, 7, colkey=0)
                    #options
                    #Start button
                    if self.option_selected==1:
                        pyxel.blt((pyxel.width-38)/2, 70, 1, 41, 169,
                                  38,12,colkey=0)
                    else:
                        pyxel.blt((pyxel.width - 38) / 2, 70, 1, 1, 169,
                                  38, 12, colkey=0)
                    #Instructions button
                    if self.option_selected==2:
                        pyxel.blt((pyxel.width-94)/2, 90, 1, 97, 185,
                                  94,12,colkey=0)
                    else:
                        pyxel.blt((pyxel.width - 94) / 2, 90, 1, 1, 185,
                                  94, 12, colkey=0)
                    #Quit button
                    if self.option_selected==3:
                        pyxel.blt((pyxel.width-30)/2, 110, 1, 33, 201,
                                  30,12,colkey=0)
                    else:
                        pyxel.blt((pyxel.width - 30) / 2, 110, 1, 1, 201,
                                  30, 12, colkey=0)
                else:
                    #Instructions
                    pyxel.blt(1, pyxel.height-42, 1, 41, 40, 150, 45, colkey=0)
                    pyxel.blt(pyxel.width-34, pyxel.height - 8, 1, 180, 41,
                              32, 7, colkey=0)
                    if self.sentence==1:
                        pyxel.text(34, pyxel.height-38, "Press space to shoot and", 1)
                        pyxel.text(34, pyxel.height-28, "try to eliminate the", 1)
                        pyxel.text(34, pyxel.height-18, "enemies. You have 3 lives", 1)
                    elif self.sentence==2:
                        pyxel.text(34, pyxel.height - 38,
                                   "You will obtain power-ups", 1)
                        pyxel.text(34, pyxel.height - 28,
                                   "which can boost your ", 1)
                        pyxel.text(34, pyxel.height - 18,
                                   "shooting and your speed.", 1)
                    elif self.sentence==3:
                        pyxel.text(34, pyxel.height - 38,
                                   "Press Z for making a loop.", 1)
                        pyxel.text(34, pyxel.height - 28,
                                   "You won't be damaged while ", 1)
                        pyxel.text(34, pyxel.height - 18, "you are looping.", 1)
                    elif self.sentence==4:
                        pyxel.text(34, pyxel.height - 38,
                                   "If you collide with an", 1)
                        pyxel.text(34, pyxel.height - 28,
                                   "enemy, you will be damaged", 1)
                        pyxel.text(34, pyxel.height - 18, "Have fun!", 1)

            else:
                #game over
                pyxel.blt((pyxel.width-70)/2, 10, 1, 73, 201, 70, 12, colkey=0)
                #score
                pyxel.blt(10, 50, 1, 113, 169, 48, 12, colkey=0)
                for n in Number.list2:
                    n.draw()
                #highscore
                pyxel.blt(10, 70, 1, 81, 169, 72, 12, colkey=0)
                for n in Number.list3:
                    n.draw()
                #restart
                pyxel.blt((pyxel.width-80)/2, 140, 1, 2+(pyxel.frame_count// 30 % 2)*80, 232,
                          80, 7, colkey=0)

    def update_list(self, list, score):
        str_points = str(score)
        if len(str_points)<6:
            for i in range(6-len(str_points)):
                str_points= "0"+str_points
        for i in range(len(str_points)):
            if len(list)>i:
                list[i] = int(str_points[i])

    def delete(self):
        if not self.first:
            for i in range(len(self.score_list)):
                self.score_list.pop(0)
            for i in range(len(self.highscore_list)):
                self.highscore_list.pop(0)
            for n in range(len(Number.list2)):
                Number.list2.pop(0)
            for n in range(len(Number.list3)):
                Number.list3.pop(0)
            self.reset_lists()

    def reset_lists(self):
        self.score_list = [0, 0, 0, 0, 0, 0]
        self.highscore_list = [0, 0, 0, 0, 0, 0]