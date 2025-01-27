import pygame
import math

AMPLITUDE = 20
WAVE_SPEED = 1/1000
WAVE_LENGTH = 0.015

def wave_function(x):
    return AMPLITUDE * math.sin(WAVE_LENGTH*x - WAVE_SPEED*pygame.time.get_ticks())

def boat_wave_function(x, boat_x):
    a = 2
    b = 0.1
    c = 0.005
    d = 0.0001
    
    if x >= boat_x:
        return math.exp(-d*math.pow(x-boat_x, 2)) * a * math.sin(b*(x-boat_x) - c*pygame.time.get_ticks())
    else:
        return -math.exp(-d*math.pow(x-boat_x, 2)) * a * math.sin(b*(x-boat_x) + c*pygame.time.get_ticks())
