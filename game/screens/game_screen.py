import pygame
from pygame import gfxdraw
import numpy as np
from PIL import Image
import visionlight
class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 50)

        self.title_text = self.font.render("you are playing!", True, (255, 255, 255))

        self.play_text = self.font.render("having fun?", True, (255, 255, 255))
        self.radius=40
        self.img = Image.open("spacestation.jpg")
        self.arr = np.array(self.img)
    def display(self):

        self.screen.fill([0,0,0])
        a, b = pygame.mouse.get_pos()
        if a<self.arr.shape[0]-self.radius and b<self.arr.shape[1]+self.radius:
            visionlight.see(self.width,self.height,self.screen,a,b,self.radius,self.arr)

    def drawpixel(self,color, pos):
        pygame.draw.line(self.screen, color, pos, pos)