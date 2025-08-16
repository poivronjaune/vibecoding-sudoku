class Solver:
    def __init__(self, board):
        self.board = board

    def is_valid(self, row, col, num):
        # Check if the number is not in the current row
        for x in range(9):
            if self.board[row][x] == num:
                return False

        # Check if the number is not in the current column
        for x in range(9):
            if self.board[x][col] == num:
                return False

        # Check if the number is not in the current 3x3 box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Puzzle solved
        else:
            row, col = empty

        for num in range(1, 10):
            if self.is_valid(row, col, num):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0  # Reset on backtrack

        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)  # Row, Col
        return None