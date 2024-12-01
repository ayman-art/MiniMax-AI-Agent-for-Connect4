class Utils:
    def __init__(self):
        self.valid_rows = []
        self.player1_score = 0
        self.player2_score = 0

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
    
    # Function to check for winning opportunities in all directions
    def winning_opportunities(self, board, player):
        score = 0

        # Horizontal check
        for r in range(len(board)):
            for c in range(len(board[0]) - 3):
                if all(board[r][c+i] == player or board[r][c+i] == 0 for i in range(4)) and any(board[r][c+i] == player for i in range(4)):
                    score += 1

        # Vertical check
        for c in range(len(board[0])):
            for r in range(len(board) - 3):
                if all(board[r+i][c] == player or board[r+i][c] == 0 for i in range(4)) and any(board[r+i][c] == player for i in range(4)):
                    score += 1

        # Down-right diagonal check
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                if all(board[r+i][c+i] == player or board[r+i][c+i] == 0 for i in range(4)) and any(board[r+i][c+i] == player for i in range(4)):
                    score += 1

        # Down-left diagonal check
        for r in range(3, len(board)):
            for c in range(len(board[0]) - 3):
                if all(board[r-i][c+i] == player or board[r-i][c+i] == 0 for i in range(4)) and any(board[r-i][c+i] == player for i in range(4)):
                    score += 1

        return score
    
    def center_control(self, board, player):
        center_cols = [2, 3, 4]
        center_count = 0
        for r in range(len(board)):
            for c in center_cols:
                if board[r][c] == player:
                    center_count += 1
        return center_count // 3


    # Blocking opponent's winning opportunities
    def blocking_opportunities(self, board, opponent):
        return self.winning_opportunities(board, opponent) * -1
    
       # Edge penalization to avoid placing pieces on the edges
    def edge_penalization(self, board, player):
        penalty = 0
        for r in range(len(board)):
            if board[r][0] == player or board[r][-1] == player:
                penalty += 1
        return penalty * -1
    
    

    
    # Heuristic function to evaluate board state
    def heuristic(self, board, computer=1, human=2):
        # Compute current scores

        # Determine the state
        score_difference = self.player1_score - self.player2_score
        state = "close_game"
        if score_difference >= 3:
            state = "winning"
        elif score_difference <= -3:
            state = "losing"


        computer_score = self.calculate_score(board, computer)
        human_score = self.calculate_score(board, human)
        score = computer_score - human_score
        
        # Adjust heuristic based on state
        if state == "winning":
            # Focus on blocking and consolidating
            score += self.blocking_opportunities(board, human) * 10  # trying to block the opponent
            score += self.center_control(board, computer) * 5
            score += self.winning_opportunities(board, computer) * 3
            score += self.edge_penalization(board, computer) * 2

        elif state == "losing":
            # Focus on creating winning opportunities
            score += self.winning_opportunities(board, computer) * 10  # Higher focus on opening winning opportunities
            score += self.center_control(board, computer) * 5
            score += self.edge_penalization(board, computer) * 3

        else:  # close_game
            # Balance offense and defense
            score += self.winning_opportunities(board, computer) * 5
            score += self.blocking_opportunities(board, human) * 5
            score += self.center_control(board, computer) * 5
            score += self.edge_penalization(board, computer) * 5
        # print(f"(block: {self.blocking_opportunities(board, human)}, win: {self.winning_opportunities(board, computer)}, center: {self.center_control(board, computer)}, edge: {self.edge_penalization(board, computer)})")
        return score
    
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

