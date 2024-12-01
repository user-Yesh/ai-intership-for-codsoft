import math

# Initialize the board
def create_board():
    return [" " for _ in range(9)]

# Print the board
def print_board(board):
    for row in range(3):
        print("|".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("-" * 5)

# Check for a winner
def check_winner(board):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]             # diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    if " " not in board:
        return "Draw"
    return None

# Get available moves
def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == "X":
        return -10 + depth
    elif winner == "O":
        return 10 - depth
    elif winner == "Draw":
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = "O"
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = "X"
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# AI's move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = " "
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the AI is 'O'.")
    print_board(board)

    while True:
        # Human player's turn
        while True:
            try:
                human_move = int(input("Enter your move (0-8): "))
                if board[human_move] == " ":
                    board[human_move] = "X"
                    break
                else:
                    print("Invalid move. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please choose a number between 0 and 8.")

        print_board(board)
        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

        # AI's turn
        print("AI is making a move...")
        ai_move_index = ai_move(board)
        board[ai_move_index] = "O"
        print_board(board)
        result = check_winner(board)
        if result:
            if result == "Draw":
                print("It's a draw!")
            else:
                print(f"{result} wins!")
            break

# Run the game
if __name__ == "__main__":
    play_game()