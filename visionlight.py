import pygame
def see(screen, a, b, radius,pixels):

    for i in range(a-radius,a+radius):
        for j in range(b-radius,b+radius):
            if ((i-a)**2+(j-b)**2)**0.5<radius:
                pygame.draw.line(screen, pixels[i][j], (i,j), (i,j))