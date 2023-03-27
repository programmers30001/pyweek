import pygame
from pygame import gfxdraw
import numpy as np
class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("you are playing!", True, (255, 255, 255))

        self.play_text = self.font.render("having fun?", True, (255, 255, 255))
        self.radius=40
    def display(self):
        img = pygame.image.load("spacestation.jpg").convert()

        a, b = pygame.mouse.get_pos()
        self.screen.blit(img,(0,0))
        for i in range(self.width):
            for j in range(self.height):
                if ((i-a)**2+(j-b)**2)**0.5<self.radius:
                    self.drawpixel(pygame.Surface.get_at(self.screen, (i, j))[:3],(i,j))

                else:
                    self.drawpixel([0,0,0],(i,j))


    def drawpixel(self,color, pos):
        pygame.draw.line(self.screen, color, pos, pos)