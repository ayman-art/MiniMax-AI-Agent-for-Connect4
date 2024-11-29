import utils
from Algorithms.agentStrategy import Strategy
class ExpectedMinmax(Strategy):
    def __init__(self):
        self.utils = utils.Utils()
        self.memo = {}
    
    #function to maximize the score
    def maximize(self, board, k, count):
        # Convert the string board into a state key for memoization
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]
        #if node is termenal
        if k == 0 or count == 41:
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            result = player1_score - player2_score, None
            self.memo[state_key] = result
            return result
        #initialize utiliy
        maxUtility = float('-inf')
        maxCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                utility , _ = self.chance(board, col, 1, k,count)
                #maximize the value of the game
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
        result = maxUtility, maxCol
        self.memo[state_key] = result
        return result

    #function to minimize the score
    def minimize(self, board, k, count):
        # Convert the string board into a state key for memoization
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]
        #if node is termenal
        if k == 0 or count == 41:
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            result = player1_score - player2_score, None
            self.memo[state_key] = result
            return result
        #initialize utiliy
        minUtility = float('inf')
        minCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                utility , _ = self.chance(board, col, 2, k, count)
                #minimize the value of the game
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
        result = minUtility, minCol
        self.memo[state_key] = result
        return result

    #for chance nodes
    def chance(self, board, col, player, k,count):
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
                row = self.utils.get_valid_row(c)
                self.utils.apply_move(board, row, c, player)
                #calculate utility for all expected nodes
                if player == 1:
                    utility, _ = self.minimize(board, k - 1, count + 1)
                else:
                    utility, _ = self.maximize(board, k - 1, count + 1)
                self.utils.undo_move(board, row, c)
                if c == col:
                    expected_utility += correct_move * utility
                else:
                    expected_utility += wrong_move * utility
        return expected_utility,None   

    def minmax(self ,board , k):
        self.utils.get_valid_count(board)
        _ , maxCol = self.maximize(board , k, 0)
        return maxCol