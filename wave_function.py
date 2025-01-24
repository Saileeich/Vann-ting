import pygame
import math

AMPLITUDE = 20
WAVE_SPEED = 1/1000
WAVE_LENGTH = 0.015

def wave_function(x):
    WAVE_HEIGHT = pygame.display.get_window_size()[0]/4
    return AMPLITUDE * math.sin(WAVE_LENGTH*x - WAVE_SPEED*pygame.time.get_ticks()) + WAVE_HEIGHT

def x_wave_function(y, x):
    return AMPLITUDE * math.sin(WAVE_LENGTH*(y-math.pi) - WAVE_SPEED*pygame.time.get_ticks()) + x

def boat_wave_function(x, boat_x):
    a = 2
    b = 0.1
    c = 0.005
    d = 0.0001
    
    if x >= boat_x:
        return math.exp(-d*math.pow(x-boat_x, 2)) * a * math.sin(b*(x-boat_x) - c*pygame.time.get_ticks())
    else:
        return -math.exp(-d*math.pow(x-boat_x, 2)) * a * math.sin(b*(x-boat_x) + c*pygame.time.get_ticks())
