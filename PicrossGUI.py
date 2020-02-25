#Collin Kan

import pygame
from Button import *
from PicrossGame import *

class PicrossGUI(PicrossGame):

    def __init__(self, pzl: Puzzle, win: pygame.display):
        super.__init__(self, pzl)
        self.win = win
