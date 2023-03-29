import sys
import pygame
from game.screens.title import TitleScreen
from game.screens.spaceship import GameScreen
from pygame import gfxdraw
import numpy as np
class Game:
    def __init__(self, width=604, height=480, caption="In The Shadows"):
        pygame.init()
        pygame.display.set_caption(caption)
        self.window_size=[width, height]
        self.screen = pygame.display.set_mode(self.window_size)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)

        self.title_screen = TitleScreen(width, height)
        self.game_screen=GameScreen(width,height)
        self.is_playing = False
        self.lighton=1
        self.radius=30
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
                    self.is_playing=1-self.is_playing
                elif event.key==pygame.K_f:
                    self.lighton=1-self.lighton
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button==4 or event.button==5:
                    if event.button == 4 and self.radius<80:
                        self.radius +=5
                    if event.button == 5 and self.radius>10 :
                        self.radius-=5
    def update(self):
        pass

    def draw(self):
        if self.is_playing:
            self.game_screen.display(self.lighton,self.radius)
        else:
            self.title_screen.display()

        pygame.display.flip()

