import pygame as pg
from GUI.board import Board
from GUI.utils import Config
import pygame_widgets
#from GUI.dropdown import DropdownMenu
from pygame_widgets.dropdown import Dropdown
def start():
    pg.init()
    size = width, height = 1440, 900
    window = pg.display.set_mode(size)
    pg.display.set_caption("Connect 4")
    clock = pg.time.Clock()
    FPS = 60
    running = True
    mat = [[0 for _ in range(7)] for i in range(6)]
    board = Board(mat, 20, 20)
    dropdown = Dropdown(window, 20, 20, 200, 50, name="Select Algorithm",
                        choices=["Minimax", "Minimax-Pruning", "Expected Minimax"],
                        borderRadius= 1, colour=Config.GREEN, values=[1, 2, 3], direction='down', textHAlign='centre'
                        )
    

    while running:
        clock.tick(FPS)
        window.fill(Config.BLACK)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
        
        board.draw(window)
        pygame_widgets.update(events)
        pg.display.update()
    pg.quit()