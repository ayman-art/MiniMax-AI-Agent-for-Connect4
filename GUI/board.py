from GUI.utils import Config
import pygame as pg
class Board:
    def __init__(self, mat):
        self.rows = Config.ROWS
        self.cols = Config.COLS
        self.mat = mat
    
    def draw(self, surface):
        for i in range(self.rows):
            for j in range(self.cols):
                cellVal = self.mat[i][j]
                pg.draw.rect(surface, Config.BLUE, (j * Config.SQUARESIZE, (i + 1) * Config.SQUARESIZE, Config.SQUARESIZE, Config.SQUARESIZE))
                pg.draw.circle(surface, Config.BLACK if cellVal == 0 else Config.RED if cellVal==1 else Config.YELLOW,
                                (j * Config.SQUARESIZE + Config.SQUARESIZE // 2, (i + 1) * Config.SQUARESIZE + Config.SQUARESIZE // 2), Config.RADIUS)
        pg.display.update()
