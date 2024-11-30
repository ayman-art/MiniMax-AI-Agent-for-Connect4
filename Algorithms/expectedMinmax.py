from graphviz import Digraph
import utils
from Algorithms.agentStrategy import Strategy

class ExpectedMinmax(Strategy):
    def __init__(self):
        self.utils = utils.Utils()
        self.memo = {}
        self.graph = Digraph("ExpectedMinmax Tree")  # Graphviz tree
        self.node_id = 0  # Unique ID for each node in the tree

    def get_node_id(self):
        """Generate a unique node ID."""
        self.node_id += 1
        return f"Node{self.node_id}"

    # Function to maximize the score
    def maximize(self, board, k, count, parent_id=None):
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
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            utility = player1_score - player2_score

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
                utility, _ = self.chance(board, col, 1, k, count, node_id)
                # Maximize the value of the game
                if utility > maxUtility:
                    maxUtility = utility
                    maxCol = col

        result = maxUtility, maxCol
        self.memo[state_key] = result
        return result

    # Function to minimize the score
    def minimize(self, board, k, count, parent_id=None):
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
            player1_score = self.utils.calculate_score(board, 1)
            player2_score = self.utils.calculate_score(board, 2)
            utility = player1_score - player2_score

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
                utility, _ = self.chance(board, col, 2, k, count, node_id)
                # Minimize the value of the game
                if utility < minUtility:
                    minUtility = utility
                    minCol = col

        result = minUtility, minCol
        self.memo[state_key] = result
        return result

    # For chance nodes
    def chance(self, board, col, player, k, count, parent_id=None):
        correct_move = 1
        wrong_move = 0
        valid_columns = [col]

        # Insert the valid columns and calculate probabilities based on the number of valid columns
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

        # Create a "Chance" node with a smaller circle shape
        node_id = self.get_node_id()
        self.graph.node(
            node_id, label=f"Chance: col={col}", shape="circle", width="0.128", height="0.128"
        )
        if parent_id:
            # Add edge with probability label
            self.graph.edge(
                parent_id, node_id, label=f"{correct_move}, Wrong: {wrong_move}"
            )

        # Initialize expected utility
        expected_utility = 0
        for c in valid_columns:
            if board[0][c] == 0:
                row = self.utils.get_valid_row(c)
                self.utils.apply_move(board, row, c, player)
                # Calculate utility for all expected nodes
                if player == 1:
                    utility, _ = self.minimize(board, k - 1, count + 1, node_id)
                else:
                    utility, _ = self.maximize(board, k - 1, count + 1, node_id)
                self.utils.undo_move(board, row, c)
                if c == col:
                    expected_utility += correct_move * utility
                else:
                    expected_utility += wrong_move * utility

        return expected_utility, None

    def minmax(self, board, k):
        root_id = self.get_node_id()
        self.graph.node(root_id, label="Root", shape="trapezium")  # Root node
        self.utils.get_valid_count(board)
        _, maxCol = self.maximize(board, k, 0, root_id)
        print(f"Total nodes visited: {self.node_id}")

        # Save the Graphviz tree
        
        return maxCol
    
    def render(self):
        self.graph.render("tree", format="svg", cleanup=True)
