import math

# Initialize the board as a list of 9 empty spaces
board = [' ' for _ in range(9)]

# Display the board
def print_board():
    for row in range(3):
        print(" | ".join(board[row * 3:(row + 1) * 3]))
        if row < 2:
            print("--+---+--")

# Check for a winner or a draw
def check_winner():
    # Define the winning combinations
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != ' ':
            return board[combo[0]]  # Return the winner ('X' or 'O')
    return None if ' ' in board else 'D'  # 'D' for draw

# Minimax algorithm with Alpha-Beta Pruning
def minimax(is_maximizing, alpha=-math.inf, beta=math.inf):
    winner = check_winner()
    if winner == 'O':  # AI wins
        return 10
    elif winner == 'X':  # Player wins
        return -10
    elif winner == 'D':  # Draw
        return 0

    if is_maximizing:  # AI's turn
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False, alpha, beta)
                board[i] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
        return best_score
    else:  # Player's turn
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True, alpha, beta)
                board[i] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:  # Alpha-Beta pruning
                    break
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

# Player move
def player_move():
    try:
        move = int(input("Enter your move (1-9): ")) - 1
        while move not in range(9) or board[move] != ' ':
            move = int(input("Invalid move. Try again (1-9): ")) - 1
        board[move] = 'X'
    except ValueError:
        print("Please enter a valid number!")
        player_move()

# Main game loop
def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X', and the AI is 'O'.")
    print_board()

    while True:
        if check_winner() is None:
            player_move()
            print_board()
        else:
            break

        if check_winner() is None:
            ai_move()
            print_board()
        else:
            break

    result = check_winner()
    if result == 'X':
        print("Congratulations! You win!")
    elif result == 'O':
        print("AI wins. Better luck next time!")
    else:
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    main()
