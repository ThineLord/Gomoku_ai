class Board:
    def __init__(self, size=15):
        self.size = size
        self.board = [["." for _ in range(size)] for _ in range(size)]

    def display(self):
        for row in self.board:
            print(" ".join(row))

    def make_move(self, move, symbol):
        x, y = move
        self.board[x][y] = symbol

    def is_valid_move(self, move):
        x, y = move
        return 0 <= x < self.size and 0 <= y < self.size and self.board[x][y] == "."

    def check_win(self, symbol):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != symbol:
                    continue
                for dx, dy in directions:
                    if all(0 <= x + dx * i < self.size and 0 <= y + dy * i < self.size and 
                           self.board[x + dx * i][y + dy * i] == symbol for i in range(5)):
                        return True
        return False