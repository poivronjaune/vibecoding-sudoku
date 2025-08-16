# solver.py

class Solver:
    def __init__(self, board):
        """
        Accepts either a Board instance or a 2D list.
        Internally works with a 2D list.
        """
        if hasattr(board, "grid"):
            self.board = board.grid
        else:
            self.board = board

    def is_valid(self, row, col, num):
        """Check if placing 'num' at (row, col) is valid."""
        # Row and column
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # 3x3 box
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False

        return True

    def find_empty(self):
        """Return first empty cell (row, col), or None if board is full."""
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None

    def solve(self):
        """Solve the Sudoku puzzle using backtracking."""
        empty = self.find_empty()
        if not empty:
            return True  # Puzzle solved
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = 0  # Backtrack

        return False
