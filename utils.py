class Utils:
    def __init__(self):
        self.valid_rows = []
        self.player1_score = 0
        self.player2_score = 0

    # Merged function to calculate score and winning opportunities
    def score_and_winning_opportunities(self, board, player):
        score = 0
        winning_opportunities = 0

        # Horizontal check
        for r in range(len(board)):
            for c in range(len(board[0]) - 3):
                match = True
                empty = False
                for i in range(4):
                    if board[r][c + i] == player:
                        continue
                    elif board[r][c + i] == 0:
                        empty = True
                    else:
                        match = False
                        break
                if match:
                    score += 1
                    if empty:
                        winning_opportunities += 1

        # Vertical check
        for c in range(len(board[0])):
            for r in range(len(board) - 3):
                match = True
                empty = False
                for i in range(4):
                    if board[r + i][c] == player:
                        continue
                    elif board[r + i][c] == 0:
                        empty = True
                    else:
                        match = False
                        break
                if match:
                    score += 1
                    if empty:
                        winning_opportunities += 1

        # Down-right diagonal check
        for r in range(len(board) - 3):
            for c in range(len(board[0]) - 3):
                match = True
                empty = False
                for i in range(4):
                    if board[r + i][c + i] == player:
                        continue
                    elif board[r + i][c + i] == 0:
                        empty = True
                    else:
                        match = False
                        break
                if match:
                    score += 1
                    if empty:
                        winning_opportunities += 1

        # Down-left diagonal check
        for r in range(3, len(board)):
            for c in range(len(board[0]) - 3):
                match = True
                empty = False
                for i in range(4):
                    if board[r - i][c + i] == player:
                        continue
                    elif board[r - i][c + i] == 0:
                        empty = True
                    else:
                        match = False
                        break
                if match:
                    score += 1
                    if empty:
                        winning_opportunities += 1

        return score, winning_opportunities

    # Function to check for blocking opponent's winning opportunities
    def score_and_blocking_opportunities(self, board, opponent):
        score, blocking_opportunities = self.score_and_winning_opportunities(board, opponent)
        return score, -blocking_opportunities
    
    # Function for center control
    def center_control(self, board, player):
        center_cols = [2, 3, 4]
        center_count = 0
        for r in range(len(board)):
            for c in center_cols:
                if board[r][c] == player:
                    center_count += 1
                    
        return center_count // 3 + sum(board[-1][c] == player for c in center_cols) - 1

    # Edge penalization to avoid placing pieces on the edges
    def edge_penalization(self, board, player):
        penalty = 0
        for r in range(len(board)):
            if board[r][0] == player or board[r][-1] == player:
                penalty += 1
        return penalty * -1
    
    
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

    def caclulate_score_for_heuristic(self, board, player):
        count = 0
        
        # Horizontal check
        for r in range(len(board)):
            cnt = 0
            c = 3
            while c < len(board[0]) and board[r][c] == player:
                cnt += 1
                c += 1
            c = 2
            while c >= 0 and board[r][c] == player:
                cnt += 1
                c -= 1
            if cnt >= 4:
                count += cnt - 3        
        
        # Vertical check
        for c in range(len(board[0])):
            cnt = 0
            r = 2
            while r >= 0 and board[r][c] == player:
                cnt += 1
                r -= 1
            r = 3
            while r < len(board) and board[r][c] == player:
                cnt += 1
                r += 1
            if cnt >= 4:
                count += cnt - 3
            

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
        
    
    # Heuristic function to evaluate board state
    def heuristic(self, board, computer=1, human=2):
        # Compute current scores
        computer_score = self.caclulate_score_for_heuristic(board, computer)
        human_score = self.caclulate_score_for_heuristic(board, human)
        center_control = self.center_control(board, computer)
        edge_penalization = self.edge_penalization(board, computer)
        
        score_difference = self.player1_score - self.player2_score
        
        # Determine the state
        state = "close_game"
        if score_difference >= 3:
            state = "winning"
        elif score_difference <= -3:
            state = "losing"
            
        score = 10 * (computer_score - human_score) + (center_control + edge_penalization) / 2
        
        if state == "winning": # Focus On Blocking the Opponent
            score -= human_score * 2
        elif state == "losing": # Focus on Scoring Points
            score += computer_score * 2

            
            
            
        return score
    
    def get_valid_row(self, col):
        return self.valid_rows[col]
    
    def get_valid_count(self, board):
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
    
    def undo_move(self, board, row, col):
        board[row][col] = 0
        if self.valid_rows[col] == -1:
            self.valid_rows[col] = 0
        else:
            self.valid_rows[col] += 1 
    
    def apply_move(self, board, row, col, player):
        board[row][col] = player
        if self.valid_rows[col] == 0:
            self.valid_rows[col] = -1
        else:
            self.valid_rows[col] -= 1

    def check_full(self):
        for i in range(len(self.valid_rows)):
            if self.valid_rows[i] != -1:
                return False
        return True


board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
    [0, 1, 2, 0, 0, 0, 0],
]

player = 1
# Example usage
utils = Utils()
score, winning_opportunities = utils.score_and_winning_opportunities(board, player)
print(f"Score: {score}, Winning Opportunities: {winning_opportunities}")
