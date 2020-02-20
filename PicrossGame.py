#Collin Kan

from Puzzle import *
import numpy as np

class PicrossGame:

    def __init__(self, pzl: Puzzle):
        self.pzl = pzl

    def get_pzl(self) -> Puzzle:
        return self.pzl

    def game_loop(self) -> None:
        while(self.get_pzl().solved() == False):
            print(" "*3, self.get_pzl().get_col_hints())
            print(np.matrix(self.get_pzl().get_row_hints()))
            print(np.matrix(self.get_pzl().get_grid()))
            self.user_input()
        print(np.matrix(self.get_pzl().get_grid()))
        print("You solved the Puzzle!")

    def user_input(self) -> None:
        move = [ int(x) for x in input("Row and Column (x,y): ").split(",") ]
        mode = input("Select (s) or Mark (m) :")
        if (move[0] in range(1, len(self.get_pzl().get_grid())+1) 
        and move[1] in range(1, len(self.get_pzl().get_grid())+1)):
            if mode == 'm': self.get_pzl().mark(move[0] - 1, move[1] - 1)
            elif mode == 's': self.get_pzl().select(move[0] - 1, move[1] - 1)
            else: print("Invalid mode, try again.\n") 
        else: print("Invalid square, try again.\n")


pzl = Puzzle("Cross.png")

pg = PicrossGame(pzl)
pg.game_loop()