"""
Draw a grip to be the borders of the game
"""
import pygame

def draw_grid(display):
    pygame.draw.line(display, (0, 135, 255), (341, 4), (341, 781), width=5)
    pygame.draw.line(display, (0, 135, 255), (794, 4), (794, 781), width=5)
    pygame.draw.line(display, (0, 135, 255), (341, 4), (794, 4), width=5)
    pygame.draw.line(display, (0, 135, 255), (341, 781), (794, 781), width=5)
