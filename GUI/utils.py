import pygame
import sys
class Config:
    BLUE = (81, 128, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    WHITE = (255, 255, 255)
    GRAY = (128,128,128)
    GREEN = (0,255,0)
    ROWS = 6
    COLS = 7
    SQUARESIZE = 100
    RADIUS = SQUARESIZE // 2 - 5
    WIDTH = COLS * SQUARESIZE
    HEIGHT = (ROWS + 1) * SQUARESIZE  # Extra row for the title or player turn display
    SIZE = (WIDTH, HEIGHT)
    FPS = 60