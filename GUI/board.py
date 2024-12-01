from GUI.utils import Config
import pygame as pg
class Board:
    def __init__(self, mat, x, y):
        self.rows = Config.ROWS
        self.cols = Config.COLS
        self.mat = mat
        self.x = x
        self.y = y
    
    def draw(self, surface):
        for i in range(self.rows):
            for j in range(self.cols):
                cellVal = self.mat[i][j]
                pg.draw.rect(surface, Config.BLUE, (self.x+j * Config.SQUARESIZE, self.y+(i) * Config.SQUARESIZE, Config.SQUARESIZE, Config.SQUARESIZE))
                pg.draw.circle(surface, Config.BLACK if cellVal == 0 else Config.RED if cellVal==1 else Config.YELLOW,
                                (self.x+j * Config.SQUARESIZE + Config.SQUARESIZE // 2, self.y+(i) * Config.SQUARESIZE + Config.SQUARESIZE // 2),
                                  Config.RADIUS)
    def get_column_from_click(self, mouse_x, mouse_y):
            if mouse_y < self.y or mouse_y > self.y+6*Config.SQUARESIZE:
                 return None
            if self.x <= mouse_x <= self.x + self.cols * Config.SQUARESIZE:
                col = (mouse_x - self.x) // Config.SQUARESIZE
                return col
            return None 

    def handle_click(self, mouse_x, mouse_y, turn, callback):
        col = self.get_column_from_click(mouse_x, mouse_y)
        if col is not None and turn != "Agent":
            print(f"Column {col} clicked!")
            if self.drop_piece_in_column(col, 2):
                callback() 
        
    def drop_piece_in_column(self, col, val):
        for row in range(self.rows - 1, -1, -1):  
            if self.mat[row][col] == 0: 
                self.mat[row][col] = val 
                return True
        return False
    
    def empty_board(self):
         self.mat = [[0] * 7 for _ in range(6)]

    def handle_event(self, event, turn, callback):
        if event.type == pg.MOUSEBUTTONDOWN:  
                if event.button == 1: 
                    self.handle_click(event.pos[0], event.pos[1], turn, callback) 