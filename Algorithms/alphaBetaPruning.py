from graphviz import Digraph
import utils
from Algorithms.agentStrategy import Strategy

class AlphaBetaPruning(Strategy):
    def __init__(self):
        self.utils = utils.Utils()
        self.memo = {}
        self.nodes_count = 0
        self.graph = Digraph("AlphaBetaPruning Tree") 
        self.node_id = 0

    def get_node_id(self):
        self.node_id += 1
        return f"Node{self.node_id}"

    def maximize(self, board, k, alpha, beta, parent_id=None):
        state_key = (str(board))

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]

        # Create a "Max" node 
        node_id = self.get_node_id()
        self.graph.node(
            node_id, label=f"Max: k={k}", shape="trapezium"
        )
        if parent_id:
            self.graph.edge(parent_id, node_id)

        # Terminal condition
        if self.utils.check_full():
            utility = self.utils.calculate_score(board,1) - self.utils.calculate_score(board,2)

            # Terminal node as rectangle
            self.graph.node(
                node_id, label=f"Terminal: Utility={utility}", shape="rectangle"
            )
            self.memo[state_key] = (utility, None)
            return utility, None
            
        elif k == 0:
            utility = self.utils.heuristic(board)

            # Terminal node
            self.graph.node(
                node_id, label=f"Terminal: Utility={utility}", shape="rectangle"
            )
            self.memo[state_key] = (utility, None)
            return utility, None

        maxUtility = float('-inf')
        maxCol = None

        for col in range(7):
            if board[0][col] == 0:
                row = self.utils.get_valid_row(col)
                self.utils.apply_move(board, row, col, 1)
                self.nodes_count += 1
                utility, _ = self.minimize(board, k - 1, alpha, beta, node_id)
                self.utils.undo_move(board, row, col)
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
                if maxUtility >= beta:
                    # Alpha-beta pruning
                    self.graph.node(
                        node_id, label=f"Pruned (maxUtility >= beta)", shape="trapezium", style="dashed"
                    )
                    break
                if maxUtility > alpha:
                    alpha = maxUtility

        self.graph.node(
            node_id, label=f"Max: Utility={maxUtility}", shape="trapezium"
        )
        result = maxUtility, maxCol
        self.memo[state_key] = result
        return result

    def minimize(self, board, k,  alpha, beta, parent_id=None):
        state_key = (str(board), k)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]

        # Create a "Min" node 
        node_id = self.get_node_id()
        self.graph.node(
            node_id, label=f"Min: k={k}", shape="invtrapezium"
        )
        if parent_id:
            self.graph.edge(parent_id, node_id)

        # Terminal condition
        if k == 0 or self.utils.check_full():
            utility = self.utils.heuristic(board)

            # Terminal node 
            self.graph.node(
                node_id, label=f"Terminal: Utility={utility}", shape="rectangle"
            )
            self.memo[state_key] = (utility, None)
            return utility, None

        minUtility = float('inf')
        minCol = None

        for col in range(7):
            if board[0][col] == 0:
                row = self.utils.get_valid_row(col)
                self.utils.apply_move(board, row, col, 2)
                self.nodes_count += 1
                utility, _ = self.maximize(board, k - 1,alpha, beta, node_id)
                self.utils.undo_move(board, row, col)
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
                if minUtility <= alpha:
                    # Alpha-beta pruning:
                    self.graph.node(
                        node_id, label=f"Pruned (minUtility <= alpha)", shape="invtrapezium", style="dashed"
                    )
                    break
                if minUtility < beta:
                    beta = minUtility

        self.graph.node(
            node_id, label=f"Min: Utility={minUtility}", shape="invtrapezium"
        )
        result = minUtility, minCol
        self.memo[state_key] = result
        return result

    def minmax(self, board, k):
        root_id = self.get_node_id()
        self.graph.node(root_id, label="Root", shape="trapezium")  
        self.utils.get_valid_count(board)
        _, maxCol = self.maximize(board, k,float('-inf'), float('inf'), root_id)
        print(f"Total nodes visited: {self.nodes_count}")
        return maxCol
    
    def render(self):
        self.graph.render("tree", format="svg", cleanup=True)
