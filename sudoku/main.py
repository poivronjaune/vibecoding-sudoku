import pygame
import sys
from sudoku.board import Board
from sudoku.ui import UI

def main():
    width, height = 600, 700  # or whatever dimensions you want
    ui = UI(width, height)

    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku Game")

    clock = pygame.time.Clock()
    board = Board()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            ui.handle_event(event, board)

        screen.fill((255, 255, 255))
        board.draw(screen)
        ui.draw()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()