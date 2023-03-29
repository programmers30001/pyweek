
import pygame
import random

class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 50)

        self.arr = []
        self.backgrounds=[]
        self.background = pygame.image.load("images/first_room.png")
        self.backgrounds.append(self.background)
        self.background = pygame.transform.scale(self.background, (width, height))

        key = pygame.image.load("images/key.png")
        self.key = pygame.transform.scale(key, (25, 30))
        self.battery=10000000
        self.used=0
        self.xkey=random.randint(0,self.width-30)
        self.ykey=random.randint(0,self.height-30)
        self.gotkey=0
        self.widthkey=25
        self.heightkey=30
    def display(self,lighton,radius):
        self.screen.fill([0, 0, 0])

        # put objects onto the background before calling array3d()
        if not self.gotkey:
            self.background.blit(self.key, (self.xkey, self.ykey))

        a, b = pygame.mouse.get_pos()
        self.clickedkey(a,b)
        color = (255*self.used/self.battery, 255*(1-self.used/self.battery), 0)

        # Drawing Rectangle
        pygame.draw.rect(self.screen, color, pygame.Rect(self.width*1/3, 0, self.width/3*(1-self.used/self.battery), 60))
        pygame.draw.rect(self.screen, color, pygame.Rect(self.width*1/3, 0, self.width/3*(1-self.used/self.battery), 60))

        # use native pygame functions to convert to a pixel array
        self.arr = pygame.surfarray.array3d(self.background)


        #if a < self.arr.shape[0] - self.radius and b < self.arr.shape[1] + self.radius:
        if lighton and random.random()<0.95 and self.used/self.battery<1:
            self.used+=1*radius*radius*3.14159265358979323
            self.see(self.screen, a, b,radius, self.arr)

    def see(self, screen, a, b, radius, pixels):
        for i in range(max(0,a - radius),min(self.arr.shape[0], a + radius)):
            # fixes error if moving the cursor down off the screen
            for j in range(max(0, b - radius), min(self.arr.shape[1], b + radius)):
                if ((i - a) ** 2 + (j - b) ** 2) ** 0.5 < radius:
                    pygame.draw.line(screen, pixels[i][j], (i, j), (i, j))

    def clickedkey(self,a,b):
        if a>self.xkey and a<self.widthkey+self.xkey and b>self.ykey and b<self.heightkey+self.ykey:
            self.gotkey=1
            self.background = pygame.image.load("images/first_room.png")
            self.background = pygame.transform.scale(self.background, (self.width, self.height))