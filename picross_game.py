#Collin Kan

from tkinter import *
from puzzle import *

W_WIDTH = 1000
W_HEIGHT = 1000

def game_display(pzl : puzzle) -> None:
    gamew = Tk()
    gamew.geometry('1000x1000')
    gamew.title("Collin's Picross")

