#Collin Kan

import pygame
from Button import *
from Puzzle import *
import math

class PicrossGUI:

    def __init__(self, pzl: Puzzle):
        self.pzl = pzl
        self.win = pygame.display.set_mode((802,900))
        self.buttons = [[] for r in self.get_pzl().get_grid()]
        self.bdim = 500 / len(self.get_pzl().get_grid())
        self.quit = Button(100,100,100,100,(200,0,0),(0,0,0), "Quit")
        self.bg = (102,255,204)

        for i in range(len(self.get_pzl().get_grid())):
            for j in range(len(self.get_pzl().get_grid()[0])):
                x = 300 + (self.bdim * j)
                y = 300 + (self.bdim * i)
                square = Button(x,y,self.bdim,self.bdim,(255,255,255),self.bg)
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
                if self.get_buttons()[i][j].crossed:
                    pygame.draw.line(self.win, (75,75,75), 
                    (self.get_buttons()[i][j].x+self.get_buttons()[i][j].width-2, self.get_buttons()[i][j].y+2),
                    (self.get_buttons()[i][j].x+2, self.get_buttons()[i][j].y+self.get_buttons()[i][j].height-2), 3)
                    pygame.draw.line(self.win, (75,75,75), 
                    (self.get_buttons()[i][j].x+2, self.get_buttons()[i][j].y+2), 
                    (self.get_buttons()[i][j].x+self.get_buttons()[i][j].width-2, self.get_buttons()[i][j].y+self.get_buttons()[i][j].height-2), 3)
        self.quit.draw(self.win)


    def drawRowHints(self) -> None:
        font = pygame.font.Font('freesansbold.ttf', round(200 / len(self.get_pzl().get_grid())))
        for i in range(len(self.get_pzl().get_row_hints())):
            pygame.draw.rect(self.win, (0,204,136),(0, 302 + self.bdim*i, 298, self.bdim - 4), 0)
            for j in range(len(self.get_pzl().get_row_hints()[i])):
                text = font.render(str(self.get_pzl().get_row_hints()[i][-(j+1)]), 1, (0,0,0))
                self.win.blit(text, (298 - round(298 / math.ceil(len(self.get_pzl().get_grid())/2)) * (j+1) + (round(298 / math.ceil(len(self.get_pzl().get_grid())/2)) - text.get_width())/2, 
                302 + self.bdim*i + (self.bdim - text.get_height())/2))

    def drawColHints(self) -> None:
        font = pygame.font.Font('freesansbold.ttf', round(200 / len(self.get_pzl().get_grid())))
        for i in range(len(self.get_buttons())):
            pygame.draw.rect(self.win, (0,204,136),(302 + self.bdim*i, 0, self.bdim - 4, 298), 0)
            for j in range(len(self.get_pzl().get_col_hints()[i])):
                text = font.render(str(self.get_pzl().get_col_hints()[i][-(j+1)]), 1, (0,0,0))
                self.win.blit(text, (302 + self.bdim*i + (self.bdim - text.get_width())/2, 
                298 - round(298 / math.ceil(len(self.get_pzl().get_grid())/2)) * (j+1) + (round(298 / math.ceil(len(self.get_pzl().get_grid())/2)) - text.get_height())/2))

    def updateWin(self) -> None:
        self.win.fill(self.bg)
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
                            done = True
                        for i in range(len(self.get_buttons())):
                            for j in range(len(self.get_buttons()[0])):
                                if (self.get_buttons()[i][j].isHover(pos)
                                and self.get_buttons()[i][j].crossed == False):
                                    self.get_buttons()[i][j].toggle()
                                    self.get_pzl().select(i, j)
                    
                    if pygame.mouse.get_pressed() == (0,0,1):
                        for i in range(len(self.get_buttons())):
                            for j in range(len(self.get_buttons()[i])):
                                if self.get_buttons()[i][j].isHover(pos):
                                    self.get_buttons()[i][j].crossout(self.win)



pzl = Puzzle("Pickaxe.png")
pg = PicrossGUI(pzl)
pg.game_loop()
                