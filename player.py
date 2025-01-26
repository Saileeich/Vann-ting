import pygame
from pygame.locals import *
from wave_function import wave_function, x_wave_function
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image_path), 2)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.copy()
        self.pos = pos.copy()
        self.draw_pos = pos.copy()

    def update(self, inputs, camera):
        self.move(inputs)
        camera.follow(self.pos[0])

        self.draw_pos[0] = x_wave_function(self.draw_pos[1], camera.width/2 - (self.rect.width/2))
        self.draw_pos[1] = wave_function(self.draw_pos[0] + (camera.x-camera.width/2) + (self.rect.width/2)) - self.rect.height
        self.rect.topleft = self.draw_pos
        
        self.image = pygame.transform.rotate(self.image_copy, (math.degrees(math.atan2(self.rect.width, wave_function(self.draw_pos[0] + (camera.x-camera.width/2) + self.rect.width) - wave_function(self.draw_pos[0] + (camera.x-camera.width/2)))) - 90))

    def move(self, inputs):
        horizontal = (1 if inputs[pygame.K_RIGHT] or inputs[pygame.K_d] else 0) - (1 if inputs[pygame.K_LEFT] or inputs[pygame.K_a] else 0)
        self.pos[0] += 1*horizontal
