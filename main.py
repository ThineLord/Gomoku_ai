if __name__ == "__main__":
    from board import Board
    from player_human import HumanPlayer
    from player_ai_minimax import MinimaxAI

    board = Board()
    human = HumanPlayer("X")
    ai = MinimaxAI("O")

    current_player = human
    while True:
        board.display()
        move = current_player.get_move(board)
        board.make_move(move, current_player.symbol)

        if board.check_win(current_player.symbol):
            board.display()
            print(f"{current_player.symbol} wins!")
            break

        current_player = ai if current_player == human else human