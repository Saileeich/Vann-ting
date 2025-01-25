import pygame

class Camera:
    def __init__(self):
        self.width = pygame.display.get_window_size()[0]
        self.x = self.width/2

        self.bg1 = pygame.image.load("./Assets/bg1.png")
        self.bg2 = pygame.image.load("./Assets/bg2.png")
        self.bg2.set_colorkey((0,0,0))
        self.bg3 = pygame.image.load("./Assets/bg3.png")
        self.bg4 = pygame.image.load("./Assets/bg4.png")

    def follow(self, x):
        self.x = x

    def draw_background(self, screen):
        background = self.create_background()
        screen.blit(background, (0, 0))

    def create_background(self):
        background = pygame.surface.Surface(pygame.display.get_window_size())
        background.fill("black")
        background.blit(self.bg4, (-self.x*0.2 - self.width/2, 0))
        background.blit(self.bg3, (-self.x*0.5 - self.width/2, 0))
        background.blit(self.bg2, (-self.x*0.8 - self.width/2, 0))
        background.blit(self.bg1, (0, 0))
        return background