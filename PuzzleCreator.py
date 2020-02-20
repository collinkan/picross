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

    return row_hints

def col_hints_maker(solution: list) -> list:
    col_hints = [[] for n in solution[0]]

    for j in range(len(solution[0])):
        i = 0
        while(i < len(solution)):
            if(solution[i][j] == 1):
                counter = 0
                while(i < len(solution) and solution[i][j] == 1):
                    counter +=1
                    i += 1 
                col_hints[j].append(counter)
            i +=1

    return col_hints