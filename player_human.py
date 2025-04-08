class HumanPlayer:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_move(self, board):
        while True:
            try:
                x, y = map(int, input(f"Enter move for {self.symbol} (row col): ").split())
                if board.is_valid_move((x, y)):
                    return x, y
                else:
                    print("Invalid move. Try again.")
            except Exception as e:
                print("Invalid input. Try again.")