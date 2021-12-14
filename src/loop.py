import pygame
from ui.draw_display import draw_display
from sprite_operations.actions import Actions


class Loop:
    """ A gameloop to render the screen, advance gameplay and handle keypresses.
    """

    def __init__(self, gamestate, display):
        """Set up the loop

        Args:
            gamestate (Class): Contains the state of the game
            display (Pygame.display): Pygame display  object to draw the game to
        """
        self.gamestate = gamestate
        self._display = display
        self._clock = pygame.time.Clock()
        self.actions = Actions(self.gamestate)

        self.prev_keystroke = "RIGHT"
        self.pause = True

    def start(self):
        """The actual gameplay loop
        """
        while True:
            if self._eventhandler() is False:
                break

            if not self.pause:
                # self._gamestate.check_for_collision()
                draw_display(self.gamestate, self._display)
                self.gamestate.check_for_full_row()
                self.actions.drop_piece(self._clock)

                self._clock.tick(60)

            else:
                draw_display(self.gamestate, self._display)

    def _eventhandler(self):
        """Handling the keys being pressed

        Returns:
            False: To close the game when esc is pressed
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if not self.pause:
                    if event.key == pygame.K_LEFT:
                        self.actions.left_once()
                    elif event.key == pygame.K_RIGHT:
                        self.actions.right_once()
                    elif event.key == pygame.K_DOWN:
                        self.actions.drop_once()
                    elif event.key == pygame.K_SPACE:
                        self.actions.drop_to_bottom()
                    elif event.key == pygame.K_UP:
                        self.actions.rotate()
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_p:
                    self.pause = not self.pause
                    self.gamestate.change_button()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_point = pygame.mouse.get_pos()
                if self.gamestate.button.rect.collidepoint(click_point):
                    self.pause = not self.pause
                    self.gamestate.change_button()
            elif event.type == pygame.QUIT:
                return False
