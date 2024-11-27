import Algorithms.minmax
import Algorithms.expectedMinmax
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [0, 1, 2, 2, 0, 0, 0],
    [0, 1, 2, 2, 2, 0, 0],
]
res = Algorithms.minmax.Minmax()
res1 = Algorithms.expectedMinmax.ExpectedMinmax()
print(res.minmax(board , 7))
print(res1.expectedMinmax(board , 4))