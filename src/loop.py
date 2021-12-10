import pygame
from ui.draw_display import draw_display


class Loop:
    """ A gameloop to render the screen, advance gameplay and handle keypresses.
    """
    def __init__(self, gamestate, display):
        """Set up the loop

        Args:
            gamestate (Class): Contains the state of the game
            display (Pygame.display): Pygame display  object to draw the game to
        """
        self._gamestate = gamestate
        self._display = display
        self._clock = pygame.time.Clock()
        self.prev_keystroke = "RIGHT"
        self._timer = 0
        self.pause = True

    def start(self):
        """The actual gameplay loop
        """
        while True:
            if self._eventhandler() is False:
                break

            if not self.pause:
                self._gamestate.check_for_collision()
                draw_display(self._gamestate, self._display)
                self._drop_piece()
                self._clock.tick(6)
            else:
                draw_display(self._gamestate, self._display)

    def _eventhandler(self):
        """Handling the keys being pressed

        Returns:
            False: To close the game when esc is pressed
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not self.pause:
                    if event.key == pygame.K_LEFT:
                        self._gamestate.move(x_coord=-32)
                        self._timer = 0
                    elif event.key == pygame.K_RIGHT:
                        self._gamestate.move(x_coord=32)
                        self._timer = 0
                    elif event.key == pygame.K_DOWN:
                        self._gamestate.move(y_coord=32)
                    elif event.key == pygame.K_SPACE:
                        self.drop_to_bottom()
                    elif event.key == pygame.K_UP:
                        self._gamestate.rotate()
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_p:
                    self.pause = not self.pause
                    self._gamestate.change_button()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_point = pygame.mouse.get_pos()
                if self._gamestate.button.rect.collidepoint(click_point):
                    self.pause = not self.pause
                    self._gamestate.change_button()
            elif event.type == pygame.QUIT:
                return False

    def _drop_piece(self):
        """Countdown to dropping a gamepiece
        """
        self._timer += self._clock.get_time()
        if self._timer > 600:
            self._gamestate.move(y_coord=32)
            self._timer = 0

    def drop_to_bottom(self):
        """Drop a gamepiece to the bottom
        """
        while not self._gamestate.check_for_collision():
            self._gamestate.move(y_coord=32)
        self._timer = 0
