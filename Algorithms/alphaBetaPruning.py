import utils
from Algorithms.agentStrategy import Strategy
class AlphaBetaPruning(Strategy):
    def __init__(self):
        self.utils = utils.Utils()
        self.memo = {}
        self.nodes_count = 0

    # Function to maximize the score
    def maximize(self, board, k, count, alpha, beta):
        # Convert the string board into a state key for memoization
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]
        if k == 0 or count == 41:
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            result = player1_score - player2_score, None
            self.memo[state_key] = result
            return result
        #initialize utility
        maxUtility = float('-inf')
        maxCol = None
        #explore neighbors
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_valid_row(col)
                self.utils.apply_move(board, row, col, 1)
                #maximize the value of the game
                self.nodes_count += 1
                utility, _ = self.minimize(board, k - 1, count +1, alpha, beta)
                self.utils.undo_move(board,row,col)
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
                if maxUtility >= beta:
                    break
                if maxUtility > alpha:
                    alpha = maxUtility
        result = maxUtility, maxCol
        self.memo[state_key] = result
        return result

    # Function to minimize the score
    def minimize(self, board, k, count, alpha, beta):
        # Convert the string board into a state key for memoization
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]
        if k == 0 or count == 41:
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            result = player1_score - player2_score, None
            self.memo[state_key] = result
            return result
        #initialize utility
        minUtility = float('inf')
        minCol = None
        #explore neighbors
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_valid_row(col)
                self.utils.apply_move(board, row, col, 2)
                #minimize the value of the game
                self.nodes_count += 1
                utility, _ = self.maximize(board, k - 1, count+1, alpha, beta)
                self.utils.undo_move(board,row,col)
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
                if minUtility <= alpha:
                    break
                if minUtility < beta:
                    beta = minUtility
        result = minUtility, minCol
        self.memo[state_key] = result
        return result

    def minmax(self, board, k):
        self.utils.get_valid_count(board)
        _, maxCol = self.maximize(board, k, 0, float('-inf'), float('inf'))
        print(self.nodes_count)
        return maxCol