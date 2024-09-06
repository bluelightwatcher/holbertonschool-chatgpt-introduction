#!/usr/bin/python3
def print_board(board):
    """
    Prints the current state of the Tic-Tac-Toe board to the console.

    Parameters:
        board (list of list of str): A 2D list representing the Tic-Tac-Toe board where each element is either 'X', 'O', or ' '.

    Returns:
        None
    """
    for row in board:
        print(" | ".join(row))  # Join elements in the row with ' | ' separator
        print("-" * 5)  # Print a horizontal separator line

def check_winner(board):
    """
    Checks if there is a winner on the Tic-Tac-Toe board.

    Parameters:
        board (list of list of str): A 2D list representing the Tic-Tac-Toe board where each element is either 'X', 'O', or ' '.

    Returns:
        bool: True if there is a winner; False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    """
    Main function to run a Tic-Tac-Toe game between two players.

    This function initializes the game board, alternates turns between players 'X' and 'O', and checks for a winner.
    The game continues until there is a winner. It prints the board and prompts players to enter their moves.

    Returns:
        None
    """
    board = [[" "] * 3 for _ in range(3)]  # Initialize a 3x3 board with empty spaces
    player = "X"  # Starting player

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            # Check if the input is within the board's range and the spot is not taken
            if 0 <= row < 3 and 0 <= col < 3:
                if board[row][col] == " ":
                    board[row][col] = player
                    winner = check_winner(board)
                    if winner:
                        print_board(board)
                        print(f"Player {winner} wins!")
                        return
                    # Switch players
                    player = "O" if player == "X" else "X"
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")

        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    tic_tac_toe()
