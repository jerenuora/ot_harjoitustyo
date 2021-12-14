import unittest
import pygame
from gamestate import GameState
from sprite_operations.actions import Actions
from sprite_operations.piece_creator import creator
from sprites.block import Block


class TestActions(unittest.TestCase):
    def setUp(self):
        self.gamestate = GameState()
        self.actions = Actions(self.gamestate)


    def test_left_once(self):
        gamepieces = self.gamestate.pieces.sprites()

        for y_coord in range(20,700,32):
            self.gamestate.fallen.add(Block(400,y_coord))

        for i in range(20):
            self.actions.left_once()
        
        self.assertGreater(            
            (min([piece.rect.x for piece in gamepieces])),(400))

    def test_right_once(self):
        gamepieces = self.gamestate.pieces.sprites()

        for y_coord in range(20,700,32):
            self.gamestate.fallen.add(Block(700,y_coord))

        for i in range(20):
            self.actions.right_once()
        
        self.assertLess(  
            (max([piece.rect.x for piece in gamepieces])),(700))

    def test_drop_once(self):
        gamepieces = self.gamestate.pieces.sprites()
        positions = [piece.rect.y for piece in gamepieces]

        for i in range(5):
            self.actions.drop_once()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            [y + (5*32) for y in positions], new_positions)

    def test_drop_once_collision(self):
        gamepieces = self.gamestate.pieces.sprites()

        for i in range(50):
            self.actions.drop_once()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            714, max(new_positions))

    def test_drop_to_bottom(self):
        gamepieces = self.gamestate.pieces.sprites()

        self.actions.drop_to_bottom()
        
        new_positions = [piece.rect.y for piece in gamepieces]
        
        self.assertEqual(
            714, max(new_positions))

