import pygame
import math

AMPLITUDE = 20
WAVE_SPEED = 1/1000
WAVE_LENGTH = 0.01

def wave_function(x):
    WAVE_HEIGHT = pygame.display.get_window_size()[0]/4
    return AMPLITUDE * math.sin(WAVE_LENGTH*x + WAVE_SPEED*pygame.time.get_ticks()) + WAVE_HEIGHT

def x_wave_function(y):
    WAVE_HEIGHT = (pygame.display.get_window_size()[0]/2) + 32
    return AMPLITUDE * math.cos(WAVE_LENGTH*y + WAVE_SPEED*pygame.time.get_ticks()) + WAVE_HEIGHT