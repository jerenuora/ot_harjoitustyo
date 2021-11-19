import pygame
# from sprites.bottom import Bottom
from sprites.piece_long import Long_piece

class GameState:

    def __init__(self):
        
        self.all_sprites = pygame.sprite.Group()
        # # self.bottom = pygame.sprite.Group()
        self.pieces = pygame.sprite.Group()

        # # self.bottom.add(Bottom())
        self.pieces.add(Long_piece(100, 100))
        self.pieces.add(Long_piece(0, 0))
        self.pieces.add(Long_piece(134, 550))
        print(self.pieces)

        self.all_sprites.add(self.pieces)
        print(self.all_sprites)