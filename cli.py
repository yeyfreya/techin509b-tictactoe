# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    now_player = 'X'

    while winner == None:
        print("TODO: take a turn!")

        # TODO: Show the board to the user.
        for row in board:
            print(" | ".join(str(n) if n is not None else " " for n in row))
   
        # TODO: Input a move from the player.
        while True:
            move = int(input(f"Player {now_player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row][col] is None:
                break
            else:
                print("Invalid input. Please enter a valid number between 1 and 9.")
   
        # TODO: Update the board.
        board[row][col] = now_player

        def get_winner(board):

            for row in board:
                if all(cell == row[0] and cell is not None for cell in row):
                    return row[0]

            for col in range(3):
                if all(board[row][col] == board[0][col] and board[row][col] is not None for row in range(3)):
                    return board[0][col]

            if all(board[i][i] == board[0][0] and board[i][i] is not None for i in range(3)):
                return board[0][0]

            if all(board[i][2 - i] == board[0][2] and board[i][2 - i] is not None for i in range(3)):
                return board[0][2]

            return None
        
        # Check for a win.
        winner = get_winner(board)
        if winner is not None:
            for row in board:
                print(" | ".join(str(n) if n is not None else " " for n in row))
            print(f"Winner: {winner}")
            break

        # Check for a tie.
        if all(cell is not None for row in board for cell in row):
            for row in board:
                print(" | ".join(str(n) if n is not None else " " for n in row))
            print("We have a tie!")
            break

        # TODO: Update who's turn it is.

        def other_player(player):
            return 'O' if player == 'X' else 'X'
        
        now_player = other_player(now_player)
