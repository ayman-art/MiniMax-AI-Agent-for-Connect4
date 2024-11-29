class Utils:
    def __init__(self):
        self.valid_rows = []

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

    def get_valid_row(self, col):
        return self.valid_rows[col]
    
    def get_valid_count(self,board):
        valid_rows = []

        for col in range(7):  
            valid_row = -1 
            
            for row in range(5, -1, -1): 
                if board[row][col] == 0:  
                    valid_row = row 
                    break  
            
            valid_rows.append(valid_row)
        self.valid_rows = valid_rows
        print(self.valid_rows)
    
    def undo_move(self, board ,row, col):
        board[row][col] = 0
        if self.valid_rows[col] == -1:
            self.valid_rows[col] = 0
        else:
            self.valid_rows[col] += 1 
    
    def apply_move(self, board ,row, col, player):
        board[row][col] = player
        if self.valid_rows[col] == 0:
            self.valid_rows[col] = -1
        else:
            self.valid_rows[col] -= 1

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
