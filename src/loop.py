"""
A gameplay loop
"""
import pygame
from sprite_operations.actions import Actions


class Loop:
    """ A gameloop to render the screen, advance gameplay and handle keypresses.
    """

    def __init__(self, gamestate, draw_display, events, clock):
        """Set up the loop

        Args:
            gamestate (Class): Contains the state of the game
            display (Pygame.display): Pygame display  object to draw the game to
        """
        self.gamestate = gamestate
        self.events = events
        self._clock = clock
        self._actions = Actions(self.gamestate)
        self._draw_display = draw_display
        self.name = ""
        self.pause = True
        self.game_over = False
        self.level = 600

    def start(self):
        """The actual gameplay loop
        """
        while True:
            if self._eventhandler() is False:
                break

            if not self.pause:
                self._draw_display.draw_display()
                self.gamestate.check_for_full_row()
                if self.gamestate.check_for_top_reach():
                    self.pause = not self.pause
                    self.game_over = True
                self._actions.drop_piece(self.level, self._clock)
                self.level = max(50, (600 - (self.gamestate.score * 10)))
                self._clock.tick(60)
            elif self.pause and not self.game_over:
                self._draw_display.draw_display()
            if self.game_over:
                self._draw_display.draw_display_gameover(self.name)

    def _eventhandler(self):
        """Handling the keys being pressed

        Returns:
            False: To close the game when esc is pressed
        """
        for event in self.events.get_events():
            if event.type == pygame.KEYDOWN:
                self.handle_basic_keydowns(event)
                if event.key == pygame.K_ESCAPE:
                    return False

            if not self.game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_point = pygame.mouse.get_pos()
                    if self.gamestate.button.rect.collidepoint(click_point):
                        self.pause = not self.pause
                        self.gamestate.change_button()
            elif event.type == pygame.QUIT:
                return False

    def handle_basic_keydowns(self,event):
        if not self.pause:
            if event.key == pygame.K_LEFT:
                self._actions.left_once()
            elif event.key == pygame.K_RIGHT:
                self._actions.right_once()
            elif event.key == pygame.K_DOWN:
                self._actions.drop_once()
            elif event.key == pygame.K_SPACE:
                self._actions.drop_to_bottom()
            elif event.key == pygame.K_UP:
                self._actions.rotate()
        if self.game_over:
            self.handle_game_over(event)
        if event.key == pygame.K_RETURN:
            self.pause = not self.pause
            self.gamestate.change_button()

    def handle_game_over(self, event):
            if event.key == pygame.K_RETURN:
                self.start_new()
            elif event.key == pygame.K_BACKSPACE:
                self.name = self.name[:-1]
            else:
                if len(self.name) < 3 and event.unicode != " ":
                    self.name += event.unicode.upper()

    def start_new(self):
                        self._actions.save_score(
                            self.name, self.gamestate.score)
                        self.name = ""
                        self.gamestate.__init__()
                        self.__init__(self.gamestate,
                                      self._draw_display,
                                      self.events,
                                      self._clock)

