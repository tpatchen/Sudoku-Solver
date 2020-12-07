import pygame

def get_clicked_cell(display_width, pos):
    gap = display_width // 9
    y = pos[0] // gap
    x = pos[1] // gap
    return x,y
 