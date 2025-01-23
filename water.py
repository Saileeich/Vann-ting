import pygame
from pygame.locals import *
from wave_function import wave_function, boat_wave_function

class Water(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, player):
        super().__init__()
        self.image = pygame.surface.Surface(pygame.display.get_window_size(), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.density = 250
        self.player = player

    def update(self, *args, **kwargs):
        self.create_water()

    def create_column(self, x, width):
        base_wave = wave_function(x + width)
        boat_wave = boat_wave_function(x + width, self.player.rect.centerx)
        total_wave = base_wave + boat_wave
        pygame.draw.polygon(self.image, (0,100,200), [pygame.Vector2(x, self.rect.bottom), pygame.Vector2(x+width, self.rect.bottom), pygame.Vector2(x+width, total_wave), pygame.Vector2(x, total_wave)])

    def create_water(self):
        self.image.fill((0,0,0,0))
        width = self.rect.right / self.density
        for i in range(self.density):
            self.create_column(i*width, width)