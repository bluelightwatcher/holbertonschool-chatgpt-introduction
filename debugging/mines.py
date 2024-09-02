#!/usr/bin/python3
import random
import os

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    """
    A class to represent the Minesweeper game.
    
    Attributes:
        width (int): The width of the game board.
        height (int): The height of the game board.
        mines (set): A set containing the positions of mines.
        field (list): A 2D list representing the game board.
        revealed (list): A 2D list representing revealed cells.
        non_mine_cells (int): The total number of cells that are not mines.
        revealed_count (int): The count of non-mine cells that have been revealed.
    """
    
    def __init__(self, width=10, height=10, mines=10):
        """
        Initializes the Minesweeper game with a specified width, height, and number of mines.

        Args:
            width (int): The width of the game board (default is 10).
            height (int): The height of the game board (default is 10).
            mines (int): The number of mines on the board (default is 10).
        """
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))  # Randomly place mines
        self.field = [[' ' for _ in range(width)] for _ in range(height)]  # Initialize the game board
        self.revealed = [[False for _ in range(width)] for _ in range(height)]  # Track revealed cells
        self.non_mine_cells = width * height - mines  # Calculate the total number of non-mine cells
        self.revealed_count = 0  # Initialize the count of revealed non-mine cells

    def print_board(self, reveal=False):
        """
        Prints the current state of the game board to the terminal.

        Args:
            reveal (bool): If True, reveals all mines on the board.
        """
        clear_screen()  # Clear the screen before printing the board
        print('  ' + ' '.join(str(i) for i in range(self.width)))  # Print column headers
        for y in range(self.height):
            print(y, end=' ')  # Print row header
            for x in range(self.width):
                if reveal or self.revealed[y][x]:  # If revealing or cell is already revealed
                    if (y * self.width + x) in self.mines:  # Check if cell is a mine
                        print('*', end=' ')  # Print mine
                    else:
                        count = self.count_mines_nearby(x, y)  # Count nearby mines
                        print(count if count > 0 else ' ', end=' ')  # Print count or empty space
                else:
                    print('.', end=' ')  # Print unrevealed cell
            print()  # Newline after each row

    def count_mines_nearby(self, x, y):
        """
        Counts the number of mines adjacent to a given cell.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.

        Returns:
            int: The number of mines adjacent to the cell.
        """
        count = 0
        for dx in [-1, 0, 1]:  # Check adjacent cells in x-direction
            for dy in [-1, 0, 1]:  # Check adjacent cells in y-direction
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:  # Ensure cell is within bounds
                    if (ny * self.width + nx) in self.mines:  # Check if adjacent cell is a mine
                        count += 1  # Increment count if mine is found
        return count

    def reveal(self, x, y):
        """
        Reveals the cell at the specified coordinates. If the cell is not a mine and has no adjacent mines,
        recursively reveals adjacent cells.

        Args:
            x (int): The x-coordinate of the cell to reveal.
            y (int): The y-coordinate of the cell to reveal.

        Returns:
            bool: False if the cell is a mine, True otherwise.
        """
        if (y * self.width + x) in self.mines:  # Check if the cell is a mine
            return False  # Return False if the cell is a mine (game over)
        if not self.revealed[y][x]:  # Check if the cell was not revealed before
            self.revealed[y][x] = True  # Mark the cell as revealed
            self.revealed_count += 1  # Increment the count of revealed non-mine cells
            if self.count_mines_nearby(x, y) == 0:  # If no adjacent mines, reveal surrounding cells
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            self.reveal(nx, ny)  # Recursively reveal adjacent cells
        return True

    def play(self):
        """
        Starts the Minesweeper game and handles the game loop.
        """
        while True:
            self.print_board()  # Print the current game board
            try:
                x = int(input("Enter x coordinate: "))  # Get x-coordinate from user
                y = int(input("Enter y coordinate: "))  # Get y-coordinate from user
                if not self.reveal(x, y):  # If the cell is a mine
                    self.print_board(reveal=True)  # Reveal the entire board
                    print("Game Over! You hit a mine.")  # Game over message
                    break  # Exit the game loop
                if self.revealed_count == self.non_mine_cells:  # Check for win condition
                    self.print_board(reveal=True)  # Reveal the entire board
                    print("Congratulations! You've won the game.")  # Win message
                    break  # Exit the game loop
            except ValueError:
                print("Invalid input. Please enter numbers only.")  # Handle invalid input

if __name__ == "__main__":
    game = Minesweeper()  # Create a Minesweeper game instance
    game.play()  # Start the game

