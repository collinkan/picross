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

def game_loop(pzl: puzzle) -> None:
    print("?")
    while(pzl.solved() == False):
        print(np.matrix(pzl.grid))
        input("Hi")

game_loop(pzl)