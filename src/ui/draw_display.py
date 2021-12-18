import pygame
from ui.game_grid import draw_grid


def draw_display(gamestate, display, game_over=False):
    gamestate.all_sprites.draw(display)

    font = pygame.font.Font(pygame.font.get_default_font(), 64)
    score = font.render(str(gamestate.score), True, (39, 19, 95))
    if game_over:
        game_over_text = font.render("GAME OVER",True,(39, 19, 95))
        display.blit(game_over_text, (350, 400))
    display.blit(score, (180, 289))

    draw_grid(display)
    pygame.display.update()
