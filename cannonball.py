import pygame
import math

class Cannonball(pygame.sprite.Sprite):
    def __init__(self, pos: pygame.Vector2, angle: float):
        super().__init__()
        self.image = pygame.image.load("./Assets/cannonball.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = pos.copy()
        self.pos = pos.copy()
        self.angle = math.radians(angle)
        self.speed = 20

    def update(self, inputs, camera, all_sprites):
        self.move(camera)
        self.rect.topleft = self.pos

    def move(self, camera):
        move_vector = pygame.Vector2(math.sin(self.angle), math.cos(self.angle)).normalize()
        self.pos = pygame.Vector2(self.pos[0] + move_vector[0]*self.speed, self.pos[1] + move_vector[1]*self.speed)