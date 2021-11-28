import pygame
from game_grid import draw_grid


class Loop:
    def __init__(self, gamestate, display):
        self._gamestate = gamestate
        self._display = display
        self._clock = pygame.time.Clock()
        self._timer = 0

    def start(self):
        while True:
            if self._eventhandler() is False:
                break
            self._gamestate.check_for_collision()


            self._draw_display()
            self.drop_piece()

            self._clock.tick(6)

    def _eventhandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._gamestate.move(x_coord=-32)
                if event.key == pygame.K_RIGHT:
                    self._gamestate.move(x_coord=32)
                if event.key == pygame.K_DOWN:
                    self._gamestate.move(y_coord=32)
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
