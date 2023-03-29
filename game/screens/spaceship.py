
import pygame


class GameScreen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.Font(None, 50)
        self.radius = 40
        self.arr = []

        background = pygame.image.load("images/spacestation.png")
        self.background = pygame.transform.scale(background, (width, height))

        key = pygame.image.load("images/key.png")
        self.key = pygame.transform.scale(key, (25, 30))

    def display(self):
        self.screen.fill([0, 0, 0])

        # put objects onto the background before calling array3d()
        self.background.blit(self.key, (0, 0))

        # use native pygame functions to convert to a pixel array
        self.arr = pygame.surfarray.array3d(self.background)
        a, b = pygame.mouse.get_pos()

        if a < self.arr.shape[0] - self.radius and b < self.arr.shape[1] + self.radius:
            self.see(self.screen, a, b, self.radius, self.arr)

    def see(self, screen, a, b, radius, pixels):
        for i in range(a - radius, a + radius):
            # fixes error if moving the cursor down off the screen
            for j in range(max(0, b - radius), min(self.arr.shape[1], b + radius)):
                if ((i - a) ** 2 + (j - b) ** 2) ** 0.5 < radius:
                    pygame.draw.line(screen, pixels[i][j], (i, j), (i, j))

