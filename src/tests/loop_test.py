import unittest
import pygame
from gamestate import GameState
from loop import Loop
from sprite_operations.piece_creator import creator
from sprites.block import Block

display_x = 0
display_y = 0
display = pygame.display.set_mode((display_x, display_y))
pygame.display.set_caption("TETRIS")
pygame.init()

class TestLoop(unittest.TestCase):
    def setUp(self):
        self.gamestate = GameState()
        self.loop = Loop(self.gamestate,display)











    def test_left_once(self):
        gamepieces = self.gamestate.pieces.sprites()

        for y_coord in range(20,700,32):
            self.gamestate.fallen.add(Block(400,y_coord))

        for i in range(20):
            self.loop.left_once()
        
        self.assertGreater(            
            (min([piece.rect.x for piece in gamepieces])),(400))

    def test_right_once(self):
        gamepieces = self.gamestate.pieces.sprites()

        for y_coord in range(20,700,32):
            self.gamestate.fallen.add(Block(700,y_coord))

        for i in range(20):
            self.loop.right_once()
        
        self.assertLess(  
            (max([piece.rect.x for piece in gamepieces])),(700))

    def test_drop_once(self):
        gamepieces = self.gamestate.pieces.sprites()
        positions = [piece.rect.y for piece in gamepieces]

        for i in range(5):
            self.loop.drop_once()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            [y + (5*32) for y in positions], new_positions)

    def test_drop_once_collision(self):
        gamepieces = self.gamestate.pieces.sprites()

        for i in range(50):
            self.loop.drop_once()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            714, max(new_positions))

    def test_drop_to_bottom(self):
        gamepieces = self.gamestate.pieces.sprites()

        self.loop.drop_to_bottom()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            714, max(new_positions))
