import utils
class Minmax():
    def __init__(self):
        self.utils = utils.Utils()
    
    #function to maximize the score
    def maximize(self,board , k):
        #if node is termenal
        if k == 0:
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            return player1_score - player2_score,None
        #initialize utiliy
        maxUtility = float('-inf')
        maxCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_the_valid_row(board , col)
                board[row][col] = 1
                utility , _ = self.minimize(board , k - 1)
                board[row][col] = 0
                #maximize the value of the game
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
        return maxUtility , maxCol

    #function to minimize the score
    def minimize(self,board , k):
        #if node is termenal
        if k == 0:
            player1_score = self.utils.calculate_score(board , 1)
            player2_score = self.utils.calculate_score(board , 2)
            return player1_score - player2_score,None
        #initialize utiliy
        minUtility = float('inf')
        minCol = None
        for col in range(7):
            #check if the column is not full
            if board[0][col] == 0:
                row = self.utils.get_the_valid_row(board , col)
                board[row][col] = 2
                utility , _ = self.maximize(board , k - 1)
                board[row][col] = 0
                #minimize the value of the game
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
        return minUtility , minCol


    def minmax(self ,board , k):
        _ , maxCol = self.maximize(board , k)
        return maxCol

        
    
