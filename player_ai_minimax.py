import random

class MinimaxAI:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        # TODO: Implement actual Minimax logic
        empty = [(i, j) for i in range(board.size) for j in range(board.size) if board.board[i][j] == "."]
        return random.choice(empty) if empty else (0, 0)