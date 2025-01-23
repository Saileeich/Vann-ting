import pygame
from pygame.locals import *
from wave_function import wave_function

class Water(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.surface.Surface(pygame.display.get_window_size())
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.density = 20

    def update(self, *args, **kwargs):
        self.create_water()

    def create_column(self, x, width):
        pygame.draw.polygon(self.image, (0,100,200), [pygame.Vector2(x, self.rect.bottom), pygame.Vector2(x+width, self.rect.bottom), pygame.Vector2(x+width, wave_function(x+width)), pygame.Vector2(x, wave_function(x))])

    def create_water(self):
        self.image.fill((0,0,0,0))
        width = self.rect.right / self.density
        for i in range(self.density):
            self.create_column(i*width, width)