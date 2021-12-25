"""
To perform actions called upon by loop
"""
from database.database_actions import put_scores


class Actions:
    """
    A class for performing gamepiece actions when called upon by the loop
    """

    def __init__(self, gamestate):
        """Constructor, inject gamestate passed from loop

        Args:
            gamestate (class): The gamestate class
        """
        self._gamestate = gamestate
        self.timer = 0

    def drop_piece(self, level,clock):
        """
        Countdown to dropping a gamepiece

        Args:
            clock (pygame.time.Clock()): A clock to keep track of advanced loop time
        """
        curr_time = clock.get_ticks()
        if curr_time - self.timer > level:
            self.timer = curr_time

            self.drop_once()

    def drop_to_bottom(self):
        """
        Drop a gamepiece until a collision occurs
        """
        while not self._gamestate.check_for_collision(y_coord=32):
            self._gamestate.move(y_coord=32)

    def drop_once(self):
        """
        Drop a gamepiece for one block length, if no collision occurs
        """
        counter = 0
        while not self._gamestate.check_for_collision(y_coord=32) and counter < 1:
            self._gamestate.move(y_coord=32)
            counter += 1

    def left_once(self):
        """
        Move a gamepiece left for one block length, if no collision occurs
        """

        if not self._gamestate.check_for_collision_sideways(x_coord=-32):
            self._gamestate.move(x_coord=-32)

    def right_once(self):
        """
        Move a gamepiece right for one block length, if no collision occurs
        """

        if not self._gamestate.check_for_collision_sideways(x_coord=32):
            self._gamestate.move(x_coord=32)

    def rotate(self):
        """
        Rotate a gamepiece
        """
        self._gamestate.rotate()

    def save_score(self, name, score):
        """
        Call the database function to save the highscore

        Args:
            name (str): Name (initials) of the player
            score (int): Score
        """
        put_scores(name, score)
