import pygame
from pygame.locals import *
from wave_function import wave_function, boat_wave_function

class Water(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, floating_objects):
        super().__init__()
        self.image = pygame.surface.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.density = 500
        self.floating_objects = floating_objects

    def update(self, inputs, *args, **kwargs):
        self.create_water()

    def create_column(self, x, width):
        pygame.draw.polygon(self.image, (0,100,200, 100), [pygame.Vector2(x, self.rect.bottom), pygame.Vector2(x+width, self.rect.bottom), pygame.Vector2(x+width, self.total_wave(x+width)), pygame.Vector2(x, self.total_wave(x))])

    def total_wave(self, x):
        total_wave = wave_function(x)
        for floater in self.floating_objects:
            total_wave += boat_wave_function(x, floater.rect.centerx)
        return total_wave

    def create_water(self):
        self.image.fill((0,0,0,0))
        width = self.rect.right / self.density
        for i in range(self.density):
            self.create_column(i*width, width)