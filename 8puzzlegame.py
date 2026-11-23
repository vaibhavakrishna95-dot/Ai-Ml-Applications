def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    for qc in win_conditions:
        if board[qc[0]] == board[qc[1]] == board[qc[2]] != ' ':
            return board[qc[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def play_game():
    while True:
        board = [' '] * 9
        current_player = 'X'

        print("\nWelcome to Tic-Tac-Toe!")
        print("The board positions are numbered 1 to 9 as shown below:")
        print_board([str(i) for i in range(1, 10)])
        print("\nStart playing!\n")

        while True:
            print_board(board)
            try:
                move = int(input(f"Player {current_player}, choose your position (1-9): ")) - 1
                if move < 0 or move > 8 or board[move] != ' ':
                    print("Invalid move! Please try again.")
                    continue
            except ValueError:
                print("Please enter a valid number between 1 and 9.")
                continue

            board[move] = current_player
            winner = check_winner(board)

            if winner:
                print_board(board)
                if winner == 'Tie':
                    print("It's a tie!")
                else:
                    print(f"Congratulations! Player {winner} wins!")
                break

            current_player = 'O' if current_player == 'X' else 'X'

        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing!")
            break

# Run the game
play_game()
