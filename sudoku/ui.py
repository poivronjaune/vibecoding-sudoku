from pygame import display, draw, font, event, KEYDOWN, QUIT, MOUSEBUTTONDOWN, Rect

class UI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = display.set_mode((self.width, self.height))
        self.clock = None
        self.font = font.Font(None, 36)

    def draw_grid(self, board):
        cell_size = self.width // 9
        for row in range(9):
            for col in range(9):
                rect = Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                draw.rect(self.screen, (255, 255, 255), rect, 1)
                if board[row][col] != 0:
                    text = self.font.render(str(board[row][col]), True, (0, 0, 0))
                    self.screen.blit(text, (col * cell_size + cell_size // 3, row * cell_size + cell_size // 4))

    def draw_number_panel(self, selected_number):
        panel_rect = Rect(0, self.height - 100, self.width, 100)
        draw.rect(self.screen, (200, 200, 200), panel_rect)
        for i in range(1, 10):
            text = self.font.render(str(i), True, (0, 0, 0))
            x = (i - 1) * (self.width // 9) + (self.width // 18)
            self.screen.blit(text, (x, self.height - 80))

        if selected_number:
            highlight_rect = Rect((selected_number - 1) * (self.width // 9), self.height - 100, self.width // 9, 100)
            draw.rect(self.screen, (255, 0, 0), highlight_rect, 3)

    def handle_input(self):
        selected_number = None
        for e in event.get():
            if e.type == QUIT:
                return None
            if e.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = e.pos
                if mouse_y > self.height - 100:
                    selected_number = mouse_x // (self.width // 9) + 1
            if e.type == KEYDOWN:
                if e.key in range(49, 58):  # Keys 1-9
                    selected_number = e.key - 48
        return selected_number

    def update(self):
        display.flip()
        if self.clock:
            self.clock.tick(60)

    def set_clock(self, clock):
        self.clock = clock

    def clear(self):
        self.screen.fill((0, 0, 0))