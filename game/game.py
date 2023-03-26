import sys
import pygame
from game.screens.title import TitleScreen

class Game:
    def __init__(self, width=604, height=480, caption="In The Shadows"):
        pygame.init()
        pygame.display.set_caption(caption)

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)

        self.title_screen = TitleScreen(width, height)
        self.is_playing = False

    def run(self):
        while True:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        if self.is_playing:
            print()
        else:
            self.title_screen.display()

        pygame.display.flip()

