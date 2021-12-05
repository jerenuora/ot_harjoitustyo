import pygame
from ui.game_grid import draw_grid


def draw_display(gamestate,display):
    gamestate.all_sprites.draw(display)
    draw_grid(display)
    pygame.display.update()
