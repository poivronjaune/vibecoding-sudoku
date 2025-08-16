# ui.py
import pygame
import sys


class UI:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = None
        self.font = pygame.font.Font(None, 36)

    def draw(self, board=None, selected_number=None):
        """Main draw function: clears screen, draws grid and number panel."""
        self.clear()
        if board is not None:
            self.draw_grid(board)
        self.draw_number_panel(selected_number)


    def draw_grid(self, board):
        """Draws the Sudoku grid with thicker 3x3 block lines and a 5px border."""
        margin = 5  # 5-pixel border
        grid_size = self.width - 2 * margin
        cell_size = grid_size // 9

        # Draw numbers and thin cell borders
        for row in range(9):
            for col in range(9):
                x = margin + col * cell_size
                y = margin + row * cell_size
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                if board[row][col] != 0:
                    text = self.font.render(str(board[row][col]), True, (0, 0, 0))
                    self.screen.blit(text, (x + cell_size // 3, y + cell_size // 4))

        # Draw thicker 3x3 block lines inside the grid
        for i in range(10):
            line_width = 3 if i % 3 == 0 else 1

            if i < 9:  # draw inner lines
                # Horizontal
                start_pos = (margin, margin + i * cell_size)
                end_pos = (margin + 9 * cell_size, margin + i * cell_size)
                pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, line_width)
                # Vertical
                start_pos = (margin + i * cell_size, margin)
                end_pos = (margin + i * cell_size, margin + 9 * cell_size)
                pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos, line_width)

        # Draw outer border
        pygame.draw.rect(self.screen, (0, 0, 0), (margin, margin, 9 * cell_size, 9 * cell_size), 5)






#    def draw_grid(self, board):
#        """Draws the Sudoku grid and numbers."""
#        cell_size = self.width // 9
#        # Draw grid cells
#        for row in range(9):
#            for col in range(9):
#                rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
#                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)  # black borders
#                if board[row][col] != 0:
#                    text = self.font.render(str(board[row][col]), True, (0, 0, 0))
#                    self.screen.blit(text, (col * cell_size + cell_size // 3, row * cell_size + cell_size // 4))

    def draw_number_panel(self, selected_number):
        """Draws the number selection panel at the bottom."""
        panel_height = 100
        panel_rect = pygame.Rect(0, self.height - panel_height, self.width, panel_height)
        pygame.draw.rect(self.screen, (200, 200, 200), panel_rect)

        cell_width = self.width // 9
        for i in range(1, 10):
            text = self.font.render(str(i), True, (0, 0, 0))
            x = (i - 1) * cell_width + cell_width // 3
            self.screen.blit(text, (x, self.height - 80))

        # Highlight selected number
        if selected_number:
            highlight_rect = pygame.Rect((selected_number - 1) * cell_width, self.height - panel_height, cell_width, panel_height)
            pygame.draw.rect(self.screen, (255, 0, 0), highlight_rect, 3)

    def handle_input(self):
        """Handles mouse clicks and keyboard input for number selection."""
        selected_number = None
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if mouse_y > self.height - 100:
                    cell_width = self.width // 9
                    selected_number = mouse_x // cell_width + 1
            if e.type == pygame.KEYDOWN:
                if pygame.K_1 <= e.key <= pygame.K_9:
                    selected_number = e.key - pygame.K_0
        return selected_number

    def update(self):
        """Updates the display and ticks the clock."""
        pygame.display.flip()
        if self.clock:
            self.clock.tick(60)

    def set_clock(self, clock):
        self.clock = clock

    def clear(self):
        """Fill the screen with white before drawing."""
        self.screen.fill((255, 255, 255))
