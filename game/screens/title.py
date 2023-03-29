import pygame

class TitleScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("Game Title", True, (255, 255, 255))

        self.play_text = self.font.render("Press SPACE to Play", True, (255, 255, 255))

    def display(self):
            self.title_rect = self.title_text.get_rect(center=(self.width // 2, self.height // 3))
            self.play_rect = self.play_text.get_rect(center=(self.width // 2, self.height // 2))

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.title_text, self.title_rect)
            self.screen.blit(self.play_text, self.play_rect)
