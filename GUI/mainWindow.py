
import pygame as pg
from GUI.board import Board
from GUI.utils import Config
from utils import Utils
from Algorithms.minmax import Minmax
from Algorithms.alphaBetaPruning import AlphaBetaPruning
from Algorithms.expectedMinmax import ExpectedMinmax
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
from pygame_widgets.button import Button
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import webbrowser
import os
import time

def draw_label(font, sur, text, pos):
    label = font.render(text, 1, (255,255,0))
    sur.blit(label, pos)
class Window:

    def open_in_browser(self):
        if self.turn == "Player" and self.started: 
            self.algo.render()
            webbrowser.open(f"file://{self.absolute_path}")
    def reset_turn(self):
            self.__init__()
    def player_callback(self):
            self.started = True
            self.board.draw(self.window)
            pg.display.update()
            self.turn = "Agent"
            self.p1_score = self.util.calculate_score(self.mat, 1)
            self.p2_score = self.util.calculate_score(self.mat, 2)
            
            self.start_buttonHandler()
    def make_algo(self, mode):
        if mode == 1:
            print("minimax")
            self.algo = Minmax()
        elif mode == 2:
            print("a-b")
            self.algo = AlphaBetaPruning()
        else:
            print("expected")
            self.algo = ExpectedMinmax()

    def start_buttonHandler(self):
            mode = self.dropdown.getSelected()
            self.make_algo(mode)
            k = int(self.output.getText())
            if self.started == False or self.turn == "Agent":
                self.started = True
                self.turn = "Agent"
                
                start_time = time.time()
                val = self.algo.minmax(self.mat, k)
                end_time = time.time()
                print(f"Time taken: {end_time - start_time} seconds")
                self.time = end_time - start_time
                
                if val is None:
                     self.__init__()
                print(val)
                self.board.drop_piece_in_column(val, 1)
                self.turn = "Player"
                self.p1_score = self.util.calculate_score(self.mat, 1)
                self.util.player1_score = self.p1_score
                self.p2_score = self.util.calculate_score(self.mat, 2)
                self.util.player2_score = self.p2_score

    def __init__(self):
        self.util = Utils()
        self.algo = None
        svg_file = "tree.svg"
        self.absolute_path = os.path.abspath(svg_file)
        pg.init()
        self.size = width, height = 750, 900
        self.label_font = pg.font.SysFont("monospace", 20)
        self.window = pg.display.set_mode(self.size)
        pg.display.set_caption("Connect 4 Agent")
        self.clock = pg.time.Clock()
        running = True
        self.mat = [[0 for _ in range(7)] for i in range(6)]
        self.board = Board(self.mat, 20, 150)
        self.dropdown = Dropdown(self.window, 20, 20, 200, 30, name="Expected Minimax",
                            choices=["Minimax", "Minimax-Pruning", "Expected Minimax"],
                            borderRadius= 1, colour=Config.GREEN, values=[1, 2, 3], direction='down', textHAlign='centre',
                            font=pg.font.SysFont("Arial", 12)
                            )
        self.button = Button(self.window, 230, 20, 100, 50, text="AI Start",
                              onClick=self.start_buttonHandler, pressedColour=Config.GREEN)
        self.render_button = Button(self.window, 600, 20, 100, 50, text="Show Tree",
                              onClick=self.open_in_browser, pressedColour=Config.GREEN)
        self.reset_button = Button(self.window, 600, 800, 100, 50, text="Restart",
                              onClick=self.reset_turn, pressedColour=Config.GREEN)
        self.slider = Slider(self.window, 370, 50, 200, 40, min=1, max=42, step=1, initial=5, handleColour=Config.BLUE)
        self.output = TextBox(self.window, 470, 20, 25, 25, fontSize=15)
        self.output.disable()
        self.p1_score = ""
        self.p2_score = ""
        self.turn = "-"
        self.time = 0
        self.started = False


        while running:
            self.clock.tick(Config.FPS)
            self.window.fill(Config.BLACK)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    running = False
                self.board.handle_event(event, self.turn, self.player_callback)
            self.board.draw(self.window)
            pygame_widgets.update(events)
            draw_label(self.label_font, self.window, "P1 Score: "+ str(self.p1_score), (20, 800))
            draw_label(self.label_font, self.window, "P2 Score: "+ str(self.p2_score), (20, 850))
            draw_label(self.label_font, self.window, "Turn: "+ self.turn, (350, 800))
            draw_label(self.label_font, self.window, "Time: "+ str(round(self.time, 2)), (350, 850))
            self.output.setText(self.slider.getValue())
            pg.display.update()
        pg.quit()

