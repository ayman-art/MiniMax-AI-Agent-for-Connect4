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
                pg.draw.rect(surface, Config.BLUE, (self.x+j * Config.SQUARESIZE, self.y+(i + 1) * Config.SQUARESIZE, Config.SQUARESIZE, Config.SQUARESIZE))
                pg.draw.circle(surface, Config.BLACK if cellVal == 0 else Config.RED if cellVal==1 else Config.YELLOW,
                                (self.x+j * Config.SQUARESIZE + Config.SQUARESIZE // 2, self.y+(i + 1) * Config.SQUARESIZE + Config.SQUARESIZE // 2), Config.RADIUS)
    def get_column_from_click(self, mouse_x):
            """Returns the column index from the mouse click (x position)."""
            if self.x <= mouse_x <= self.x + self.cols * Config.SQUARESIZE:
                col = (mouse_x - self.x) // Config.SQUARESIZE
                return col
            return None  # Clicked outside the board

    def handle_click(self, mouse_x):
        """Handles the mouse click event by calling the action for the specific column."""
        col = self.get_column_from_click(mouse_x)
        if col is not None:
            # Perform action with the column number
            print(f"Column {col} clicked!")
            #self.drop_piece_in_column(col)  # Implement your dropping logic here

    def drop_piece_in_column(self, col):
        """Drops a piece in the selected column (dummy implementation)."""
        for row in range(self.rows - 1, -1, -1):  # Start from the bottom row
            if self.mat[row][col] == 0:  # Find the first empty row in this column
                self.mat[row][col] = 1  # Assume player 1 drops a piece (red)
                break
    
    def empty_board(self):
         self.mat = [[0] * 7 for _ in range(6)]
         pg.display.update() 

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:  # Detect mouse clicks
                if event.button == 1:  # Left mouse button click
                    self.handle_click(event.pos[0]) 