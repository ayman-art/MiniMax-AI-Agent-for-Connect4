class Utils:
    #function to calculate the score
    def calculate_score(self ,board, player):
        count = 0
        
        # Horizontal check
        for r in range(len(board)):
            for c in range(len(board[0]) - 3):
                if all(board[r][c+i] == player for i in range(4)):
                    count += 1

        # Vertical check
        for c in range(len(board[0])):
            for r in range(len(board) - 3):
                if all(board[r+i][c] == player for i in range(4)):
                    count += 1

        #right diagonal check
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                if all(board[r+i][c+i] == player for i in range(4)):
                    count += 1

        #left diagonal check
        for r in range(3, len(board)):
            for c in range(len(board[0]) - 3):
                if all(board[r-i][c+i] == player for i in range(4)):
                    count += 1

        return count

    #function to get the valid row
    def get_the_valid_row(self ,board , col):
        for i in range(len(board) - 1, -1, -1):
            if board[i][col] == 0:
                return i
    
    #function to check if the game end
    def check_full(self, board):
        for i in range(len(board[0])):
            if board[0][i] == 0:
                return False
        return True
    
    def board_to_tuple(self, board):
        # Converts a 2D list to a tuple of tuples for hashing
        return tuple(tuple(row) for row in board)

board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
]

player = 1
# print(calculate_score(board, player)) 
