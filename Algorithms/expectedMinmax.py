import utils
class ExpectedMinmax():
    def __init__(self):
        self.utils = utils.Utils()
    
    #function to maximize the score
    def maximize(self, board, k):
        #if node is termenal
        if k == 0 or self.utils.check_full(board):
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            return player1_score - player2_score,None
        #initialize utiliy
        maxUtility = float('-inf')
        maxCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                utility , _ = self.chance(board, col, 1, k)
                #maximize the value of the game
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
        return maxUtility , maxCol

    #function to minimize the score
    def minimize(self, board, k):
        #if node is termenal
        if k == 0 or self.utils.check_full(board):
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            return player1_score - player2_score,None
        #initialize utiliy
        minUtility = float('inf')
        minCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                utility , _ = self.chance(board, col, 2, k)
                #minimize the value of the game
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
        return minUtility , minCol

    #for chance nodes
    def chance(self, board, col, player, k):
        correct_move = 1
        wrong_move = 0
        valid_columns = [col]
        #insert the valid columns and calculate probabilities based on the number of valid columns
        if col - 1 > 0 and col + 1 < 7:
            if board[0][col - 1] == 0 and board[0][col + 1] == 0:
                wrong_move = 0.2
                correct_move = 0.6
                valid_columns.append(col + 1)
                valid_columns.append(col - 1)
        elif col - 1 > 0:
            if board[0][col - 1] == 0:
                wrong_move = 0.4
                valid_columns.append(col - 1)
        elif col + 1 < 7:
            if board[0][col + 1] == 0:
                wrong_move = 0.4
                valid_columns.append(col + 1)
        #initialize expected utility
        expected_utility = 0
        for c in valid_columns:
            if board[0][c] == 0:
                row = self.utils.get_the_valid_row(board, c)
                board[row][c] = player
                #calculate utility for all expected nodes
                if player == 1:
                    utility, _ = self.minimize(board, k - 1)
                else:
                    utility, _ = self.maximize(board, k - 1)
                board[row][c] = 0
                if c == col:
                    expected_utility += correct_move * utility
                else:
                    expected_utility += wrong_move * utility
        return expected_utility,None   

    def expectedMinmax(self ,board , k):
        _ , maxCol = self.maximize(board , k)
        return maxCol