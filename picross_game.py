#Collin Kan

from tkinter import *
from puzzle import *

W_WIDTH = 1000
W_HEIGHT = 1000
pzl = [[1,2], [3, 4]]

def game_display() -> None:
    gamew = Tk()
    gamew.title("Collin's Picross")
    boxes = [[Button(gamew, command=clicked(toggle()), height=7, width=15) for r in pzl[0]] for n in pzl]
    for i in range(len(boxes)):
        for j in range(len(boxes[0])):
            boxes[i][j].grid(column=i, row=j)
    gamew.mainloop()

def toggle() -> bool:
    return True

def clicked(mode: bool) -> None:
    return

game_display()