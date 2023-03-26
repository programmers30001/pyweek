import pygame
class Polygon:
    def __init__(self, sides, color,screen):
        self.sides = sides
        self.color=color
        self.screen=screen

    def draw(self,x,y,zoom,point):
        scaledsides=[]

        for i in self.sides:
            scaledsides.append([x+(i[0]-point[0])*zoom**2,y+(i[1]-point[1])*zoom**2])
        pygame.draw.polygon(self.screen, self.color,scaledsides)
