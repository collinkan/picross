#Collin Kan

import numpy as np
import imageio

def PuzzleCreator(img: str) -> list:
    img = imageio.imread(img).tolist()
    solution = [[] for pixel in img]

    for i in range(len(img)):
        for j in range(len(img)):
            solution[i].append(int(img[i][j][0] == 0))

    return solution

PuzzleCreator("PuzzleImages\\Cross.png")