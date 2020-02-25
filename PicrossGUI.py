#Collin Kan

import pygame
from Button import *
from Puzzle import *

class PicrossGUI:

    def __init__(self, pzl: Puzzle):
        self.pzl = pzl
        self.win = pygame.display.set_mode((802,900))
        self.buttons = [[] for r in self.get_pzl().get_grid()]

        dim = 500 / len(self.get_pzl().get_grid())
        for i in range(len(self.get_pzl().get_grid())):
            for j in range(len(self.get_pzl().get_grid()[0])):
                x = 300 + (dim * i)
                y = 300 + (dim * j)
                square = Button(x,y,dim,dim)
                self.buttons[i].append(square)

    def get_pzl(self) -> Puzzle:
        return self.pzl

    def get_win(self) -> pygame.display:
        return self.win

    def get_buttons(self) -> list:
        return self.buttons

    def drawGrid(self) -> None:
        for i in range(len(self.get_buttons())):
            for j in range(len(self.get_buttons()[i])):
                self.get_buttons()[i][j].draw(self.win)

    def drawRowHints(self) -> None:
        for i in range(len(self.get_buttons())):
            pygame.draw.rect(self.win, (0,204,136), (0, 300 + self.get_buttons()[i][0].height*i, 298, self.get_buttons()[i][0].height), 0)

    def drawColHints(self) -> None:
        for i in range(len(self.get_buttons())):
            pygame.draw.rect(self.win, (0,204,136), (300 + self.get_buttons()[i][0].height*i, 0, self.get_buttons()[i][0].height, 298), 0)

    def updateWin(self) -> None:
        self.win.fill((102,255,204))
        self.drawGrid()
        self.drawRowHints()
        self.drawColHints()

    def game_loop(self) -> None:
        done = False

        while not done:
            self.updateWin()
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(len(self.get_buttons())):
                        for j in range(len(self.get_buttons()[i])):
                            if self.get_buttons()[i][j].isHover(pos):
                                self.get_buttons()[i][j].toggle()




pzl = Puzzle("Cross.png")
pg = PicrossGUI(pzl)
pg.game_loop()
                