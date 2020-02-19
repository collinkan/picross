#Collin Kan

from puzzle import *
import numpy as np

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
chints = [[],[1],[5],[1],[]]
pzl = puzzle(solution,rhints,chints)

class PicrossGame:

    def __init__(self, pzl: puzzle):
        self.pzl = pzl

    def get_pzl(self) -> puzzle:
        return self.pzl

    def game_loop(self) -> None:
        while(pzl.solved() == False):
            print(np.matrix(pzl.grid))
            self.user_input()

    def user_input(self) -> None:
        move = [ int(x) for x in input("Row and Column (x,y): ").split(",") ]
        if move[0] in range(1,6) and move[1] in range(1,6):
            pzl.select(move[0] - 1, move[1] - 1)
        else: print("Invalid square, try again.\n")


pg = PicrossGame(pzl)
pg.game_loop()