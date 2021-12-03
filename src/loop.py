import pygame
from game_grid import draw_grid


class Loop:
    def __init__(self, gamestate, display):
        self._gamestate = gamestate
        self._display = display
        self._clock = pygame.time.Clock()
        self.prev_keystroke = "RIGHT"
        self._timer = 0
        self.pause = False

    def start(self):
        while True:
            if self._eventhandler() is False:
                break

            if not self.pause:
                self._gamestate.check_for_collision()
                self._draw_display()
                self.drop_piece()
                self._clock.tick(6)
            else:
                self._draw_display()

    def _eventhandler(self):
        for event in pygame.event.get():
            if not self.pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = not self.pause

                    if event.key == pygame.K_LEFT:
                        self._gamestate.move(x_coord=-32)
                        self._timer = 0
                    if event.key == pygame.K_RIGHT:
                        self._gamestate.move(x_coord=32)
                        self._timer = 0
                    if event.key == pygame.K_DOWN:
                        self._gamestate.move(y_coord=32)
                    if event.key == pygame.K_SPACE:
                        self.drop_to_bottom()
                    if event.key == pygame.K_UP:
                        self._gamestate.rotate()
                    if event.key == pygame.K_ESCAPE:
                        return False
            elif self.pause:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause = not self.pause
                    if event.key == pygame.K_ESCAPE:
                        return False

            elif event.type == pygame.QUIT:
                return False

    def _draw_display(self):
        self._gamestate.all_sprites.draw(self._display)
        draw_grid(self._display)
        pygame.display.update()

    def drop_piece(self):
        self._timer += self._clock.get_time()
        if self._timer > 600:
            self._gamestate.move(y_coord=32)
            self._timer = 0

    def drop_to_bottom(self):
        while not self._gamestate.check_for_collision():
            self._gamestate.move(y_coord=32)
        self._timer = 0
