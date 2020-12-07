import pygame
import sys
from board import Board
from helpers import get_clicked_cell

start_board = [[0,0,0,0,0,3,0,8,4],
               [0,1,0,0,0,0,0,7,0],
               [0,2,8,9,0,1,0,5,3],
               [3,0,1,0,9,8,0,0,6],
               [8,0,0,0,4,0,0,0,5],
               [7,0,0,3,5,0,9,0,8],
               [2,3,0,4,0,9,8,6,0],
               [0,8,0,0,0,0,0,9,0],
               [9,7,0,6,0,0,0,0,0]]
pygame.init()
WHITE = (255,255,255)
BLUE = (0, 0, 255)
display_width = 900
DISPLAY = pygame.display.set_mode((display_width, display_width),0,32)
pygame.display.set_caption("Sudoku Solver")
DISPLAY.fill(WHITE)

board = Board(display_width, display_width)
board.draw_grid(DISPLAY)
board.fill_cells(start_board)
board.fill_solution()
board.generate_solution()

pygame.display.update()
while True:
    board.draw(DISPLAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                result = board.solve(DISPLAY)
                if not result:
                    print('Not solvable!')
            if event.key == pygame.K_0:
                if board.cell_is_clicked():
                    board.change_cell_value(0)
            if event.key == pygame.K_1:
                if board.cell_is_clicked():
                    board.change_cell_value(1)
            if event.key == pygame.K_2:
                if board.cell_is_clicked():
                    board.change_cell_value(2)
            if event.key == pygame.K_3:
                if board.cell_is_clicked():
                    board.change_cell_value(3)
            if event.key == pygame.K_4:
                if board.cell_is_clicked():
                    board.change_cell_value(4)
            if event.key == pygame.K_5:
                if board.cell_is_clicked():
                    board.change_cell_value(5)
            if event.key == pygame.K_6:
                if board.cell_is_clicked():
                    board.change_cell_value(6)
            if event.key == pygame.K_7:
                if board.cell_is_clicked():
                    board.change_cell_value(7)
            if event.key == pygame.K_8:
                if board.cell_is_clicked():
                    board.change_cell_value(8)
            if event.key == pygame.K_9:
                if board.cell_is_clicked():
                    board.change_cell_value(9)
            if event.key == pygame.K_BACKSPACE:
                if board.cell_is_clicked():
                    board.change_cell_value(0)

        if pygame.mouse.get_pressed()[0]: #left click
            pos = pygame.mouse.get_pos()
            cell_pos = get_clicked_cell(display_width, pos)
            board.set_clicked_cell(cell_pos)
        
            

    pygame.display.update()