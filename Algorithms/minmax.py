import utils
class Minmax():
    def __init__(self):
        self.utils = utils.Utils()
        

    # Function to maximize the score
    def maximize(self, board, k, count):
        if k == 0 or count == 41:
            print("hit")
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            return player1_score - player2_score, None
        #initialize utility
        maxUtility = float('-inf')
        maxCol = None
        #explore neighbors
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_the_valid_row(board, col)
                board[row][col] = 1
                #maximize the value of the game
                utility, _ = self.minimize(board, k - 1, count +1)
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col

                board[row][col] = 0
        return maxUtility, maxCol

    # Function to minimize the score
    def minimize(self, board, k, count):
        if k == 0 or count == 41:
            print("hit")
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            return player1_score - player2_score, None
        #initialize utility
        minUtility = float('inf')
        minCol = None
        #explore neighbors
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_the_valid_row(board, col)
                board[row][col] = 2
                #minimize the value of the game
                utility, _ = self.maximize(board, k - 1, count+1)
                if utility < minUtility:
                    minUtility = utility
                    minCol = col

                board[row][col] = 0
        return minUtility, minCol

    def minmax(self, board, k):
        _, maxCol = self.maximize(board, k, 0)
        return maxCol


        
    
