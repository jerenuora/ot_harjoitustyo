import pygame
from ui.game_grid import draw_grid


def draw_display(gamestate, display):
    gamestate.all_sprites.draw(display)

    font = pygame.font.Font(pygame.font.get_default_font(), 64)
    score = font.render(str(gamestate.score), True, (39, 19, 95))
    display.blit(score, (180, 289))

    draw_grid(display)
    pygame.display.update()


def draw_display_gameover(gamestate, display):
    gamestate.all_sprites.draw(display)
    draw_grid(display)

    font = pygame.font.Font(pygame.font.get_default_font(), 64)
    font_big = pygame.font.Font(pygame.font.get_default_font(), 120)
    score = font.render(str(gamestate.score), True, (39, 19, 95))
    game_over_text = font_big.render("GAME OVER",True,(39, 19, 95))
    enter_initials = font.render("Enter your initials:", True, (39, 19, 95))
    display.blit(game_over_text, (200, 400))
    display.blit(enter_initials, (200, 600))
    display.blit(score, (180, 289))

    pygame.display.update()

