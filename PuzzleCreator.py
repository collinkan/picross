#Collin Kan

import numpy as np
import imageio

def solution_maker(imgname: str) -> list:
    img = imageio.imread("PuzzleImages\\"+imgname).tolist()
    solution = [[] for pixel in img]

    for i in range(len(img)):
        for j in range(len(img)):
            solution[i].append(int(img[i][j][0] == 0))

    return solution

def row_hints_maker(solution: list) -> list:
    row_hints = [[] for r in solution]
    
    for i in range(len(solution)):
        j = 0
        while(j < len(solution[i])):
            if(solution[i][j] == 1):
                counter = 0
                while(j < len(solution[i]) and solution[i][j] == 1):
                    counter +=1
                    j += 1 
                row_hints[i].append(counter)
            j +=1

    print(row_hints) 
        

#sol = solution_maker("Cross.png")
sol = [[0,0,1,0,0],
        [0,1,1,1,0],
        [1,1,0,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0]]
row_hints_maker(sol)
