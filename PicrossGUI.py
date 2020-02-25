#Collin Kan

import pygame
from Button import *
from Puzzle import *

class PicrossGUI:

    def __init__(self, pzl: Puzzle):
        self.pzl = pzl
        self.win = pygame.display.set_mode((802,900))
        self.buttons = [[] for r in self.get_pzl().get_grid()]
        self.quit = Button(100,100,100,100,(200,0,0),(0,0,0), "Quit")

        dim = 500 / len(self.get_pzl().get_grid())
        for i in range(len(self.get_pzl().get_grid())):
            for j in range(len(self.get_pzl().get_grid()[0])):
                x = 300 + (dim * j)
                y = 300 + (dim * i)
                square = Button(x,y,dim,dim,(255,255,255),(102,255,204))
                self.buttons[i].append(square)
        pygame.display.set_caption("Collin's Picross")

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
        self.quit.draw(self.win)

    def drawRowHints(self) -> None:
        for i in range(len(self.get_buttons())):
            pygame.draw.rect(self.win, (0,204,136), (0, 302 + self.get_buttons()[i][0].width*i, 298, self.get_buttons()[i][0].width - 4), 0)

    def drawColHints(self) -> None:
        for i in range(len(self.get_buttons())):
            pygame.draw.rect(self.win, (0,204,136), (302 + self.get_buttons()[i][0].width*i, 0, self.get_buttons()[i][0].width - 4, 298), 0)

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

                if event.type == pygame.QUIT or self.get_pzl().solved():
                    pygame.quit()
                    done = True

                if event.type == pygame.MOUSEBUTTONDOWN:

                    if pygame.mouse.get_pressed() == (1,0,0):
                        if self.quit.isHover(pos):
                            pygame.quit()
                            done = True
                        for i in range(len(self.get_buttons())):
                            for j in range(len(self.get_buttons()[0])):
                                if self.get_buttons()[i][j].isHover(pos):
                                    self.get_buttons()[i][j].toggle()
                                    self.get_pzl().select(i, j)
                    
                    # if pygame.mouse.get_pressed() == (0,0,1):
                    #     for i in range(len(self.get_buttons())):
                    #         for j in range(len(self.get_buttons()[i])):
                    #             if self.get_buttons()[i][j].isHover(pos):
                    #                 self.get_buttons()[i][j].toggle()




pzl = Puzzle("Cross.png")
pg = PicrossGUI(pzl)
pg.game_loop()
                