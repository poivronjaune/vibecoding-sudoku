# generator.py
import random
from copy import deepcopy

class PuzzleGenerator:
    def __init__(self, difficulty='medium'):
        """
        difficulty: 'easy', 'medium', 'hard'
        """
        self.difficulty = difficulty
        self.board = self.generate_board()

    def generate_board(self):
        """Generate a full valid Sudoku board using backtracking."""
        board = [[0 for _ in range(9)] for _ in range(9)]
        self._fill_board(board)
        self.remove_numbers(board)
        return board

    def _fill_board(self, board):
        """Recursive backtracking to fill the board completely."""
        empty = self._find_empty(board)
        if not empty:
            return True  # Board completely filled
        row, col = empty
        numbers = list(range(1, 10))
        random.shuffle(numbers)
        for num in numbers:
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self._fill_board(board):
                    return True
                board[row][col] = 0  # Backtrack
        return False

    def remove_numbers(self, board):
        """Remove numbers from the filled board to create a puzzle."""
        if self.difficulty == 'easy':
            removals = 35
        elif self.difficulty == 'medium':
            removals = 45
        else:  # hard
            removals = 55

        while removals > 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if board[row][col] != 0:
                board[row][col] = 0
                removals -= 1

    def is_valid(self, board, row, col, num):
        """Check if placing num at (row,col) is valid."""
        # Row and column
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def _find_empty(self, board):
        """Return the first empty cell (row,col), or None if full."""
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None

    def get_puzzle(self):
        """Return a copy of the generated puzzle."""
        return deepcopy(self.board)

