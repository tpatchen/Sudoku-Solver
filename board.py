import pygame, time, copy, sys
from Cell import Cell
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = []
        self.clicked_cell = None
        self.solution = None
    
    def draw(self, display):
        display.fill(WHITE)
        self.draw_grid(display)
        self.draw_cells(display)
        self.draw_clicked(display)

    def draw_grid(self, display):
        gap = self.height // 9
        for i in range(1,9):
            if i % 3 == 0:
                pygame.draw.line(display, BLACK, (gap*i,0), (gap*i, self.height), 3)
                pygame.draw.line(display, BLACK, (0, gap*i), (self.width, gap*i), 3)
            else:
                pygame.draw.line(display, BLACK, (gap*i, 0), (gap*i, self.height), 1)
                pygame.draw.line(display, BLACK, (0, gap*i), (self.width, gap*i), 1)
    def draw_clicked(self, display):
        if self.clicked_cell == None:
            return
        gap = self.height // 9
        cell_pos = self.clicked_cell
        cell = self.cells[cell_pos[0]][cell_pos[1]]
        pygame.draw.rect(display, BLUE, (cell.x, cell.y, gap, gap), 2)
   
    def fill_cells(self, start_board):
        gap = self.height // 9
        for i in range(len(start_board)):
            temp = []
            for j in range(len(start_board[i])):
                if start_board[i][j] != 0:
                    newCell = Cell(gap * j, gap * i, start_board[i][j], i, j, False)
                else:
                    newCell = Cell(gap * j, gap * i, start_board[i][j], i, j, True)
                temp.append(newCell)
            self.cells.append(temp)
    
    def draw_cells(self, display):
        for row in self.cells:
            for cell in row:
                cell.draw(display)
    
    def is_safe(self, row, col, val, array):
        for cell in array[row]:
            if cell.num == val:
                return False
        for r in array:
            if r[col].num == val:
                return False

        for i in range(row // 3 * 3, row // 3 * 3 + 3):
            for j in range(col // 3 * 3, col // 3 * 3 + 3):
                if array[i][j].num == val:
                    return False
        return True
    
    def find_zero(self, array):
        for row in array:
            for cell in row:
                if cell.num == 0:
                    return cell.row, cell.col
        return False

    def solve(self,display):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        time.sleep(0.2)
        self.draw(display)
        pygame.display.update()
        found_cell = self.find_zero(self.cells)
        if not found_cell:
            return True
        row,col = found_cell
        for i in range(1,10):
            if self.is_safe(row, col, i, self.cells):
                self.cells[row][col].num = i
                if self.solve(display):
                    return True
                self.cells[row][col].num = 0
        return False
    
    def fill_solution(self):
        self.solution = copy.deepcopy(self.cells)

    def generate_solution(self):
        found_cell = self.find_zero(self.solution)
        if not found_cell:
            return True
        row,col = found_cell
        for i in range(1,10):
            if self.is_safe(row, col, i, self.solution):
                self.solution[row][col].num = i
                if self.generate_solution():
                    return True
                self.solution[row][col].num = 0
        return False


    def set_clicked_cell(self, clicked_cell):
        self.clicked_cell = clicked_cell
    
    def cell_is_clicked(self):
        return self.clicked_cell != None

    def get_clicked_cell(self):
        return self.clicked_cell
    
    def change_cell_value(self, val):
        row, col = self.clicked_cell
        if self.cells[row][col].changeable == False:
            return
        if self.solution[row][col].num == val or val == 0:
            self.cells[row][col].color = BLACK
            self.cells[row][col].num = val
            
        else:
            self.cells[row][col].color = RED
            self.cells[row][col].num = val




        