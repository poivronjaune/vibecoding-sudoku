class Board:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def render(self, screen):
        # Code to render the Sudoku grid on the Pygame screen
        pass

    def place_number(self, row, col, number):
        if self.is_valid_move(row, col, number):
            self.grid[row][col] = number
            return True
        return False

    def is_valid_move(self, row, col, number):
        # Check if placing the number violates Sudoku rules
        for i in range(9):
            if self.grid[row][i] == number or self.grid[i][col] == number:
                return False

        box_row = (row // 3) * 3
        box_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_row + i][box_col + j] == number:
                    return False

        return True

    def reset(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]