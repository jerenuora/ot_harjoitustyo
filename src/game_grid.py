import pygame

def draw_grid(display):
    pygame.draw.line(display, (0,135,255), (341,10),(341,781),width=5)
    pygame.draw.line(display, (0,135,255), (794,10),(794,781),width=5)
    pygame.draw.line(display, (0,135,255), (341,10),(794,10),width=5)
    pygame.draw.line(display, (0,135,255), (341,781),(794,781),width=5)
