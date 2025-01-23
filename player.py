import pygame
from pygame.locals import *
from wave_function import wave_function
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image_path), 2)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.pos = pos

    def update(self):
        self.image = pygame.transform.rotate(self.image_copy, (math.degrees(math.atan2(self.rect.width, wave_function(self.pos[0] + self.rect.width) - wave_function(self.pos[0]))) - 90))
        
        self.pos[1] = wave_function(self.pos[0] + (self.rect.width/2)) - self.rect.height
        self.rect.topleft = self.pos
