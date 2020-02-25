#Collin Kan

import pygame

class Button:

    def __init__(self, x: int, y: int, width: int, height: int, text: str):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text