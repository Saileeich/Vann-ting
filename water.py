import pygame
from pygame.locals import *
import math

class Water(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.surface.Surface(pygame.display.get_window_size())
        self.rect = self.image.get_rect()
        self.rect.topleft = pos

        self.amplitude = 20
        self.wave_speed = 1/1000
        self.wave_height = self.rect.bottom/2
        self.density = 10

    def update(self, *args, **kwargs):
        self.create_water()

    def wave(self, x):
        return self.amplitude * math.sin(x+self.wave_speed*pygame.time.get_ticks()) + self.wave_height

    def create_column(self, x, width):
        print(self.wave(x))
        pygame.draw.polygon(self.image, (0,100,200), [pygame.Vector2(x, self.rect.bottom), pygame.Vector2(x+width, self.rect.bottom), pygame.Vector2(x+width, self.wave(x+width)), pygame.Vector2(x, self.wave(x))])

    def create_water(self):
        self.image.fill((0,0,0,0))
        width = self.rect.right / self.density
        for i in range(self.density):
            self.create_column(i*width, width)