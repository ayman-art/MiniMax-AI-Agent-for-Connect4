from graphviz import Digraph
import utils
from Algorithms.agentStrategy import Strategy

class AlphaBetaPruning(Strategy):
    def __init__(self):
        self.utils = utils.Utils()
        self.memo = {}
        self.nodes_count = 0
        self.graph = Digraph("AlphaBetaPruning Tree")  # Graphviz tree
        self.node_id = 0  # Unique ID for each node in the tree

    def get_node_id(self):
        """Generate a unique node ID."""
        self.node_id += 1
        return f"Node{self.node_id}"

    def maximize(self, board, k, count, alpha, beta, parent_id=None):
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]

        # Create a "Max" node with a trapezium shape
        node_id = self.get_node_id()
        self.graph.node(
            node_id, label=f"Max: k={k}, count={count}", shape="trapezium"
        )
        if parent_id:
            self.graph.edge(parent_id, node_id)

        # Terminal condition
        if k == 0 or count == 41:
            utility = self.utils.heuristic(board)

            # Terminal node as rectangle
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
                utility, _ = self.minimize(board, k - 1, count + 1, alpha, beta, node_id)
                self.utils.undo_move(board, row, col)
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col
                if maxUtility >= beta:
                    # Alpha-beta pruning: if maxUtility >= beta, prune
                    self.graph.node(
                        node_id, label=f"Pruned (maxUtility >= beta)", shape="trapezium", style="dashed"
                    )
                    break
                if maxUtility > alpha:
                    alpha = maxUtility

        result = maxUtility, maxCol
        self.memo[state_key] = result
        return result

    def minimize(self, board, k, count, alpha, beta, parent_id=None):
        state_key = (str(board), k, count)

        # Check if state is already evaluated
        if state_key in self.memo:
            return self.memo[state_key]

        # Create a "Min" node with an inverted trapezium shape
        node_id = self.get_node_id()
        self.graph.node(
            node_id, label=f"Min: k={k}, count={count}", shape="invtrapezium"
        )
        if parent_id:
            self.graph.edge(parent_id, node_id)

        # Terminal condition
        if k == 0 or count == 41:
            utility = self.utils.heuristic(board)

            # Terminal node as rectangle
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
                utility, _ = self.maximize(board, k - 1, count + 1, alpha, beta, node_id)
                self.utils.undo_move(board, row, col)
                if utility < minUtility:
                    minUtility = utility
                    minCol = col
                if minUtility <= alpha:
                    # Alpha-beta pruning: if minUtility <= alpha, prune
                    self.graph.node(
                        node_id, label=f"Pruned (minUtility <= alpha)", shape="invtrapezium", style="dashed"
                    )
                    break
                if minUtility < beta:
                    beta = minUtility

        result = minUtility, minCol
        self.memo[state_key] = result
        return result

    def minmax(self, board, k):
        """Start the Alpha-Beta pruning process and export the Graphviz tree."""
        root_id = self.get_node_id()
        self.graph.node(root_id, label="Root", shape="trapezium")  # Root node
        self.utils.get_valid_count(board)
        _, maxCol = self.maximize(board, k, 0, float('-inf'), float('inf'), root_id)
        print(f"Total nodes visited: {self.nodes_count}")

        # Save the Graphviz tree
        
        return maxCol
    
    def render(self):
        self.graph.render("tree", format="svg", cleanup=True)
