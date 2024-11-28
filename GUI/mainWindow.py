import pygame as pg
from GUI.board import Board
from GUI.utils import Config
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
def start_buttonHandler(name):
    print(name)
    pass
def draw_label(font, sur, text, pos):
    label = font.render(text, 1, (255,255,0))
    sur.blit(label, pos)
def start():
    
    def start_buttonHandler():
        print(dropdown.getSelected())
        pass
    pg.init()
    size = width, height = 1440, 900
    label_font = pg.font.SysFont("monospace", 20)
    window = pg.display.set_mode(size)
    pg.display.set_caption("Connect 4")
    clock = pg.time.Clock()
    FPS = 60
    running = True
    mat = [[_%3 for _ in range(7)] for i in range(6)]
    board = Board(mat, 20, 20)
    dropdown = Dropdown(window, 20, 20, 200, 50, name="Select Algorithm",
                        choices=["Minimax", "Minimax-Pruning", "Expected Minimax"],
                        borderRadius= 1, colour=Config.GREEN, values=[1, 2, 3], direction='down', textHAlign='centre'
                        )
    button = Button(window, 300, 20, 100, 50, text="AI Start", onClick=start_buttonHandler, pressedColour=Config.GREEN)
    slider = Slider(window, 450, 50, 200, 40, min=1, max=42, step=1, initial=1, handleColour=Config.BLUE)
    output = TextBox(window, 537, 20, 25, 25, fontSize=15)
    output.disable()
    p1_score = ""
    p2_score = ""
    turn = "-"
    


    while running:
        clock.tick(FPS)
        window.fill(Config.BLACK)
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False
            board.handle_event(event)
        board.draw(window)
        pygame_widgets.update(events)
        draw_label(label_font, window, "P1 Score: "+ str(p1_score), (20, 800))
        draw_label(label_font, window, "P2 Score: "+ str(p1_score), (20, 850))
        draw_label(label_font, window, "Turn: "+ turn, (350, 825))
        output.setText(slider.getValue())
        pg.display.update()
    pg.quit()