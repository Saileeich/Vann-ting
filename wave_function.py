import pygame
import math


def wave_function(x):
    AMPLITUDE = 20
    WAVE_SPEED = 1/1000
    WAVE_HEIGHT = pygame.display.get_window_size()[0]/4

    return AMPLITUDE * math.sin(x+WAVE_SPEED*pygame.time.get_ticks()) + WAVE_HEIGHT