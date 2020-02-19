#Collin Kan

from puzzle import *
import numpy as np

class PicrossGame:

    def __init__(self, pzl: puzzle):
        self.pzl = pzl

    def get_pzl(self) -> puzzle:
        return self.pzl

    def game_loop(self) -> None:
        while(self.get_pzl().solved() == False):
            print(np.c_[self.get_pzl().get_row_hints(), self.get_pzl().get_grid()])
            self.user_input()
        print("You solved the puzzle!")

    def user_input(self) -> None:
        move = [ int(x) for x in input("Row and Column (x,y): ").split(",") ]
        if (move[0] in range(1, len(self.get_pzl().get_grid())+1) 
        and move[1] in range(1, len(self.get_pzl().get_grid())+1)):
            self.get_pzl().select(move[0] - 1, move[1] - 1)
        else: print("Invalid square, try again.\n")


solution = [[0,0,1,0,0],
            [0,1,1,1,0],
            [0,0,1,0,0],
            [0,0,1,0,0],
            [0,0,1,0,0]]
rhints = [[1],
          [3],
          [1],
          [1],
          [1]]
chints = [[0],[1],[5],[1],[0]]
pzl = puzzle(solution,rhints,chints)

pg = PicrossGame(pzl)
pg.game_loop()