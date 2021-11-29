import unittest
from gamestate import GameState


class TestGamePieceMovement(unittest.TestCase):
    def setUp(self):
        self.gamestate = GameState()
        # self.display = pygame.display.set_mode((1145,800))

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
