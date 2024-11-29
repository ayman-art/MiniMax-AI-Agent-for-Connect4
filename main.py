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
# res = Algorithms.minmax.Minmax()
res1 = Algorithms.expectedMinmax.ExpectedMinmax()
res2 = Algorithms.alphaBetaPruning.AlphaBetaPruning()
# print(res.get_valid_count(board))
# print(res.minmax(board , 10))
# print(res1.expectedMinmax(board , 10))
print(res2.minmax(board, 17))