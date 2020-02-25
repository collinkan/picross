#Collin Kan

import pygame
from Button import *
from PicrossGame import *

class PicrossGUI:

    def __init__(self, pzl: Puzzle):
        self.pzl = pzl
        self.win = pygame.display.set_mode((800,900))
        self.buttons = [[] for r in self.get_pzl().get_grid()]

        dim = 500 / len(self.get_pzl().get_grid())
        for i in range(len(self.get_pzl().get_grid())):
            for j in range(len(self.get_pzl().get_grid()[0])):
                x = 300 + (dim * i)
                y = 300 + (dim * i)
                square = Button(x,y,dim,dim)
                self.buttons[i].append(square)


    def get_pzl(self) -> Puzzle:
        return self.pzl

    def get_win(self) -> pygame.display:
        return self.win

    def get_buttons(self) -> list:
        return self.buttons

    def drawGrid(self) -> None:
        for r in self.get_buttons():
            for b in r:
                b.draw(self.win)

                