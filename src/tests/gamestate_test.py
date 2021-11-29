import unittest
from gamestate import GameState
from sprites.piece_creator import creator

class TestGamestate(unittest.TestCase):
    def setUp(self):
        self.gamestate = GameState()

    def test_collision_fallen(self):
        a_piece = creator(self.gamestate.next_piece, 540,100)
        self.gamestate.move(y_coord=100)
        self.gamestate.fallen.add(a_piece)

        self.assertTrue(self.gamestate.check_for_collision())

    def test_collision_bottom(self):
        self.gamestate.move(y_coord=650)

        self.assertTrue(self.gamestate.check_for_collision())

    def test_no_collision(self):
        self.gamestate.move(y_coord=400)
        self.assertFalse(self.gamestate.check_for_collision())

    def test_a_piece_moves(self):

        gamepieces = self.gamestate.pieces.sprites()
        one_gamepiece = gamepieces[0]
        x, y = one_gamepiece.rect.x, one_gamepiece.rect.y

        self.gamestate.move(40, 70)

        self.assertEqual(
            (x+40, y+70), (one_gamepiece.rect.left, one_gamepiece.rect.top))

    def test_multiple_pieces_move(self):

        for piece in self.gamestate.pieces:
            x, y = piece.rect.left, piece.rect.top
            self.gamestate.move(120, -200)

            self.assertEqual(
                (x+120, y+-200), (piece.rect.left, piece.rect.top))
