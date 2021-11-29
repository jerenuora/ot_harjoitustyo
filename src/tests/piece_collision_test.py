import unittest
from gamestate import GameState
from sprites.piece_creator import creator

class TestGamePieceCollision(unittest.TestCase):
    def setUp(self):
        self.gamestate = GameState()
        # self.gamestate.pieces.empty()

    def test_collision_fallen(self):
        # self.gamestate.spawn_new_piece()
        a_piece = creator(self.gamestate.next_piece, 540,100)
        self.gamestate.move(y_coord=100)
        self.gamestate.fallen.add(a_piece)

        self.assertTrue(self.gamestate.check_for_collision())

    def test_collision_bottom(self):
        # self.gamestate.spawn_new_piece()
        self.gamestate.move(y_coord=650)

        self.assertTrue(self.gamestate.check_for_collision())

    def test_no_collision(self):
        # self.gamestate.spawn_new_piece()
        self.gamestate.move(y_coord=400)
        self.assertFalse(self.gamestate.check_for_collision())