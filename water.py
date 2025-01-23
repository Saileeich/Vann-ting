import pygame
from pygame.locals import *
import math

class Water(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2):
        self.image = pygame.surface.Surface()
        self.rect = pygame.rect.Rect(pos, pygame.display.get_window_size())

        self.amplitude = 10
        self.wave_speed = 2

    def wave(self, x):
        return self.amplitude * math.sin(x+self.wave_speed*pygame.time.get_ticks())
