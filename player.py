import pygame
from pygame.locals import *
import math
import random
from wave_function import wave_function
from cannonball import Cannonball

class Player(pygame.sprite.Sprite):
    def __init__(self, image_path: str, pos: pygame.Vector2):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load(image_path), 2)
        self.image_copy = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.copy()
        self.pos = pos.copy()
        self.draw_pos = pos.copy()
        self.angle = 90

    def update(self, inputs, camera, all_sprites: pygame.sprite.Group):
        self.move(inputs)
        camera.follow(self.pos[0])

        self.draw_pos[0] = -wave_function(self.pos[0] + math.pi/2) + camera.width/2 - (self.rect.width/2)
        self.draw_pos[1] = wave_function(self.draw_pos[0] + (camera.x-camera.width/2) + (self.rect.width/2)) - self.rect.height + pygame.display.get_window_size()[0]/4
        self.rect.topleft = self.draw_pos

        self.angle = (math.degrees(math.atan2(self.rect.width, wave_function(self.draw_pos[0] + (camera.x-camera.width/2) + self.rect.width) - wave_function(self.draw_pos[0] + (camera.x-camera.width/2)))) - 90)        
        self.image = pygame.transform.rotate(self.image_copy, self.angle)

        if inputs[pygame.K_SPACE]:
            all_sprites.add(Cannonball(pygame.Vector2(self.rect.centerx, self.rect.bottom), self.angle))

    def move(self, inputs):
        horizontal = (1 if inputs[pygame.K_RIGHT] or inputs[pygame.K_d] else 0) - (1 if inputs[pygame.K_LEFT] or inputs[pygame.K_a] else 0)
        self.pos[0] += 1*horizontal
