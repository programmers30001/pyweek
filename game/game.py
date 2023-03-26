import sys
import pygame
from game.screens.title import TitleScreen
from game.screens.game_screen import GameScreen
class Game:
    def __init__(self, width=604, height=480, caption="In The Shadows"):
        pygame.init()
        pygame.display.set_caption(caption)
        self.window_size=[width, height]
        self.screen = pygame.display.set_mode(self.window_size,pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)

        self.title_screen = TitleScreen(width, height)
        self.game_screen=GameScreen(width,height)
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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.is_playing=True
            elif event.type == pygame.VIDEORESIZE:
                self.window_size = event.size

    def update(self):
        pass

    def draw(self):
        if self.is_playing:
            self.game_screen.display(self.window_size[0],self.window_size[1])
        else:
            self.title_screen.display(self.window_size[0],self.window_size[1])

        pygame.display.flip()

