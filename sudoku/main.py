# main.py
import pygame
import sys
from sudoku.board import Board
from sudoku.ui import UI

def main():
    width, height = 600, 700
    ui = UI(width, height)

    pygame.init()
    pygame.display.set_caption("Sudoku Game")

    clock = pygame.time.Clock()
    board = Board()

    selected_number = None

    while True:
        # Handle input
        selected_number = ui.handle_input() or selected_number

        # Clear and redraw everything
        ui.draw(board=board.grid, selected_number=selected_number)
        ui.set_clock(clock)
        ui.update()

if __name__ == "__main__":
    main()
