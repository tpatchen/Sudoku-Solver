import pygame
BLACK = (0,0,0)
RED = (255, 0, 0)
class Cell:
    def __init__(self, x, y, num, row, col, changeable):
        self.x = x
        self.y = y 
        self.num = num
        self.row = row
        self.col = col
        self.color = BLACK
        self.changeable = changeable

    def draw(self, display):
        if self.num == 0:
            return
        font = pygame.font.SysFont(None, 50)
        img = font.render(str(self.num), True, self.color)
        display.blit(img, (self.x + 40, self.y + 30))
