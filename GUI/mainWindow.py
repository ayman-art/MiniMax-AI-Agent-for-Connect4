import pygame as pg
from GUI.board import Board

def start():
    pg.init()
    size = width, height = 1440, 900
    window = pg.display.set_mode(size)
    pg.display.set_caption("Connect 4")
    clock = pg.time.Clock()
    FPS = 60
    running = True
    mat = [[_%3 for _ in range(7)] for i in range(6)]
    board = Board(mat)
    board.draw(window)
    while running:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
        
    
    pg.quit()