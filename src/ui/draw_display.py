"""
Different "screens", and their texts to be drawn at different game situations. 
Also, drawing the sprites, updating pygame display
"""
import pygame
from database.database_actions import get_scores, get_lowest_shown_score


class DrawDisplay:

    def __init__(self, gamestate, display):
        self._gamestate = gamestate
        self._display = display

    def draw_display(self):
        self._gamestate.all_sprites.draw(self._display)
        self.draw_common_texts(self._gamestate.score)
        self.draw_scores()
        self.draw_grid(self._display)
        pygame.display.update()

    def draw_display_gameover(self, name):
        self._gamestate.all_sprites.draw(self._display)
        self.draw_grid(self._display)
        self.draw_common_texts(self._gamestate.score)
        self.draw_game_over()
        if self._gamestate.score > get_lowest_shown_score():
            self.draw_ask_for_initials(name)
        else:
            self.draw_press_enter()
        self.draw_scores()
        pygame.display.update()

    def draw_ask_for_initials(self, name):
        font_small = pygame.font.Font(pygame.font.get_default_font(), 35)
        enter_initials = font_small.render(
            "Enter initials:", True, (39, 19, 95))
        show_name = font_small.render(name, True, (39, 19, 95))
        self._display.blit(enter_initials, (820, 355))
        self._display.blit(show_name, (820, 390))

    def draw_press_enter(self):
        font_small = pygame.font.Font(pygame.font.get_default_font(), 35)
        press_enter = font_small.render("Press enter ", True, (39, 19, 95))
        to_play = font_small.render("to play again ", True, (39, 19, 95))
        self._display.blit(press_enter, (820, 355))
        self._display.blit(to_play, (820, 390))

    def draw_game_over(self):
        font_big = pygame.font.Font(pygame.font.get_default_font(), 105)
        game_text = font_big.render("GAME", True, (39, 19, 95))
        over_text = font_big.render("OVER", True, (39, 19, 95))
        self._display.blit(game_text, (10, 200))
        self._display.blit(over_text, (820, 200))

    def draw_common_texts(self, score):
        font_small = pygame.font.Font(pygame.font.get_default_font(), 35)
        font = pygame.font.Font(pygame.font.get_default_font(), 64)
        score = font.render(str(score), True, (39, 19, 95))
        self._display.blit(score, (200, 400))

        score_text = font_small.render("SCORE: ", True, (39, 19, 95))
        self._display.blit(score_text, (50, 425))
        high_scores = font_small.render("TOP 3 SCORES: ",  True, (39, 19, 95))
        self._display.blit(high_scores, (50, 490))

    def draw_scores(self):
        SCORES = get_scores()
        SCORES.sort(key=lambda score: score["score"], reverse=True)
        font = pygame.font.Font(pygame.font.get_default_font(), 35)
        if len(SCORES) >= 1:

            text = f"1: {SCORES[0]['name']} {str(SCORES[0]['score'])}"
            scores = font.render(text,  True, (39, 19, 95))
            self._display.blit(scores, (50, 552))
        if len(SCORES) >= 2:

            text = f"2: {SCORES[1]['name']} {str(SCORES[1]['score'])}"
            scores = font.render(text,  True, (39, 19, 95))
            self._display.blit(scores, (50, 580))
        if len(SCORES) >= 3:

            text = f"3: {SCORES[2]['name']} {str(SCORES[2]['score'])}"
            scores = font.render(text,  True, (39, 19, 95))
            self._display.blit(scores, (50, 620))

    def draw_grid(self, display):
        pygame.draw.line(self._display, (0, 135, 255),
                         (341, 4), (341, 781), width=5)
        pygame.draw.line(self._display, (0, 135, 255),
                         (794, 4), (794, 781), width=5)
        pygame.draw.line(self._display, (0, 135, 255),
                         (341, 4), (794, 4), width=5)
        pygame.draw.line(self._display, (0, 135, 255),
                         (341, 781), (794, 781), width=5)
