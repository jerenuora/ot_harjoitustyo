import pygame
from ui.draw_display import draw_display

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
                draw_display(self._gamestate,self._display)
                self._drop_piece()
                self._clock.tick(6)
            else:
                self._draw_display()

    def _eventhandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not self.pause:
                    if event.key == pygame.K_LEFT:
                        self._gamestate.move(x_coord=-32)
                        self._timer = 0
                    if event.key == pygame.K_RIGHT:
                        self._gamestate.move(x_coord=32)
                        self._timer = 0
                    if event.key == pygame.K_DOWN:
                        self._gamestate.move(y_coord=32)
                    if event.key == pygame.K_SPACE:
                        self._drop_to_bottom()
                    if event.key == pygame.K_UP:
                        self._gamestate.rotate()
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_p:
                    self.pause = not self.pause
            elif event.type == pygame.QUIT:
                return False


    def _drop_piece(self):
        self._timer += self._clock.get_time()
        if self._timer > 600:
            self._gamestate.move(y_coord=32)
            self._timer = 0

    def _drop_to_bottom(self):
        while not self._gamestate.check_for_collision():
            self._gamestate.move(y_coord=32)
        self._timer = 0
