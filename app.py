import pygame
from pygame.locals import *

from water import Water
from player import Player
from camera import Camera

class App():
    def __init__(self, WIDTH, HEIGHT, CAPTION, FPS):
        self.awake((WIDTH, HEIGHT), CAPTION, FPS)
        self.start()

    def awake(self, screen_dimensions, caption, fps):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_dimensions)
        pygame.display.set_caption(caption)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.all_sprites = pygame.sprite.Group()
        self.key_codes = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]
        self.inputs = {}
        for key_code in self.key_codes:
            self.inputs[key_code] = 0

    def start(self):
        self.camera = Camera()

        self.floating_objects = []
        self.floating_objects.append(Player("./Assets/boat.png", pygame.Vector2(168, 0)))
        #self.floating_objects.append(Player("./Assets/boat.png", pygame.Vector2(318, 0)))
        for floater in self.floating_objects:
            self.all_sprites.add(floater)
        self.all_sprites.add(Water(pygame.Vector2(0, 0), self.floating_objects))

    def handle_events(self):        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in self.key_codes:
                    self.inputs[event.key] = 1
            elif event.type == KEYUP:
                if event.key in self.key_codes:
                    self.inputs[event.key] = 0
            elif event.type == QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update(self.inputs, self.camera)

    def draw(self):
        self.screen.fill("black")
        #self.screen.blit(pygame.image.load("./Assets/bg1.png"), (0,0))
        self.camera.draw_background(self.screen)
        self.all_sprites.draw(self.screen)
        pygame.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)