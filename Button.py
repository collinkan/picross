#Collin Kan

import pygame

class Button:

    pygame.init()

    def __init__(self, x: int, y: int, width: int, height: int, color: tuple, outline: tuple, text=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.outline = outline
        self.text = text
        self.selected = False
        self.crossed = False

    def draw(self, win: pygame.display, textfont='freesansbold.ttf') -> None:
        pygame.draw.rect(win, self.outline, (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (self.x+2, self.y+2, self.width-4, self.height-4))
        if self.text != "":
            font = pygame.font.Font(textfont, 40)
            text = font.render(self.text, 1, self.outline)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def toggle(self) -> None:
        if self.selected: 
            self.selected = False
            self.color = (255,255,255)
        elif not self.selected: 
            self.selected = True
            self.color = (0,0,0)

    def crossout(self, win: pygame.display) -> None:
        if not self.selected and not self.crossed: self.crossed = True
        elif self.crossed: self.crossed = False

    def isHover(self, pos) -> bool:
        if (pos[0] > self.x and pos[0] < self.x + self.width
        and pos[1] > self.y and pos[1] < self.y + self.height):
            return True
        return False