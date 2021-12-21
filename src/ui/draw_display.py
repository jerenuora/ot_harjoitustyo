import pygame
from ui.game_grid import draw_grid
from database.database_actions import get_scores,get_lowest_shown_score

def draw_display(gamestate, display):
    gamestate.all_sprites.draw(display)
    draw_common_texts(display,gamestate.score)
    draw_scores(display)
    draw_grid(display)
    pygame.display.update()


def draw_display_gameover(gamestate, display,name):
    gamestate.all_sprites.draw(display)
    draw_grid(display)
    draw_common_texts(display,gamestate.score)
    font = pygame.font.Font(pygame.font.get_default_font(), 64)

    font_big = pygame.font.Font(pygame.font.get_default_font(), 120)
    game_over_text = font_big.render("GAME OVER",True,(39, 19, 95))
    if gamestate.score > get_lowest_shown_score():
        enter_initials = font.render("Enter your initials:", True, (39, 19, 95))
        show_name = font.render(name, True, (39, 19, 95))
        display.blit(enter_initials, (200, 600))
        display.blit(show_name,(200,700))
    else:
        no_new_hs = font.render("No new highscore, press enter to play again ", True, (39, 19, 95))
        display.blit(no_new_hs, (200, 600))
    draw_scores(display)
    display.blit(game_over_text, (200, 400))
    pygame.display.update()
    
def draw_common_texts(display,score):
    font_small = pygame.font.Font(pygame.font.get_default_font(), 35)
    font = pygame.font.Font(pygame.font.get_default_font(), 64)
    score = font.render(str(score), True, (39, 19, 95))
    display.blit(score, (200, 400))

    score_text = font_small.render("SCORE: ", True, (39, 19, 95))
    display.blit(score_text, (50, 425))
    high_scores = font_small.render("TOP 3 SCORES: ",  True, (39, 19, 95))
    display.blit(high_scores, (50, 490))

def draw_scores(display):
    SCORES = get_scores()
    SCORES.sort( key=lambda score:score["score"],reverse=True)
    font = pygame.font.Font(pygame.font.get_default_font(), 35)
    if len(SCORES) >= 1:

        text = f"1: {SCORES[0]['name']} {str(SCORES[0]['score'])}"
        scores = font.render(text,  True, (39, 19, 95))
        display.blit(scores, (50 , 552))
    if len(SCORES) >= 2:

        text = f"2: {SCORES[1]['name']} {str(SCORES[1]['score'])}"
        scores = font.render(text,  True, (39, 19, 95))
        display.blit(scores, (50 , 580))
    if len(SCORES) >= 3:

        text = f"3: {SCORES[2]['name']} {str(SCORES[2]['score'])}"
        scores = font.render(text,  True, (39, 19, 95))
        display.blit(scores, (50 , 620))


