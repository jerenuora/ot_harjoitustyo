import pygame
from sprites.block import Block



class Piece_L():

    def __init__(self, x=0, y=0):
        self.piece_L = pygame.sprite.Group()
        self.piece_L.add(Block(375, 10))
        self.piece_L.add(Block(405, 10))
        self.piece_L.add(Block(405, 40))
        self.piece_L.add(Block(405, 70))
