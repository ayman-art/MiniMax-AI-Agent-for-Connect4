
class Config:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    ROWS = 6
    COLS = 7
    SQUARESIZE = 100
    RADIUS = SQUARESIZE // 2 - 5
    WIDTH = COLS * SQUARESIZE
    HEIGHT = (ROWS + 1) * SQUARESIZE  # Extra row for the title or player turn display
    SIZE = (WIDTH, HEIGHT)