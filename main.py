# from GUI.mainWindow import Window

# program = Window()
import Algorithms.alphaBetaPruning
import Algorithms.minmax
import Algorithms.expectedMinmax
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [2, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 2, 0, 0, 0],
    [1, 1, 1, 2, 2, 0, 0],
    [1, 1, 2, 1, 2, 1, 0],
]
res = Algorithms.alphaBetaPruning.AlphaBetaPruning()
# # print(res.get_valid_count(board))
# # print(res.minmax(board , 10))
res.minmax(board, 4)
res.render()


