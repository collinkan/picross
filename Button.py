#Collin Kan

import pygame

class Button:

    def __init__(self, x: int, y: int, width: int, height: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255,255,255)
        #self.text = text

    def draw(self, win: pygame.display) -> None:
        pygame.draw.rect(win, (0,0,0), (self.x, self.y, self.width, self.height), 0)
        pygame.draw.rect(win, self.color, (self.x+2, self.y+2, self.width-4, self.height-4))
        # font = pygame.font.Font('arial', 60)
        # text = font.render(self.text, 1, (0,0,0))
        # win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def toggle(self) -> None:
        if self.color == (0,0,0): self.color = (255,255,255)
        elif self.color == (255,255,255): self.color = (0,0,0)

    def isHover(self, pos) -> bool:
        if (pos[0] > self.x and pos[0] < self.x + self.width
        and pos[1] > self.y and pos[1] < self.y + self.height):
            return True
        return False