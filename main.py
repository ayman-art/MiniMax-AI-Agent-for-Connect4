import Algorithms.minmax
board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 0, 0, 0],
    [0, 0, 2, 2, 0, 0, 0],
    [1, 1, 2, 2, 0, 0, 0],
]
res = Algorithms.minmax.Minmax()
print(res.minmax(board , 4))