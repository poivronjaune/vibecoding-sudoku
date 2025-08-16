# board.py
class Board:
    def __init__(self):
        # 9x9 grid initialized with zeros
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def place_number(self, row, col, number):
        """Place a number if the move is valid."""
        if self.is_valid_move(row, col, number):
            self.grid[row][col] = number
            return True
        return False

    def is_valid_move(self, row, col, number):
        """Check if placing 'number' at (row, col) is valid according to Sudoku rules."""
        # Check row and column
        for i in range(9):
            if self.grid[row][i] == number or self.grid[i][col] == number:
                return False

        # Check 3x3 box
        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == number:
                    return False

        return True

    def reset(self):
        """Reset the board to all zeros."""
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
