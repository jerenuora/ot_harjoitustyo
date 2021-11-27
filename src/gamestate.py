import pygame
from random import choice
from sprites.bottom import Bottom
from sprites.backround import Board
from sprites.piece_creator import creator

from sprites.block import Block


class GameState:
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        # self.bottom = pygame.sprite.Group()
        self.one_piece = Block(20, 300)
        print(self.one_piece.rect.left)
        self.pieces = creator("SHAPE_SQ", 540, 10)
        # self.pieces.add(self.one_piece)
        self.fallen = pygame.sprite.Group()
        self.backround = Board(0, 0)
        self.bottom = Bottom()
        # self.bottom.add(Bottom())
        # self.piece_L = pygame.sprite.Group()
        # self.piece_L.add(Block(375, 10))
        # self.piece_L.add(Block(405, 10))
        # self.piece_L.add(Block(405, 40))
        # self.piece_L.add(Block(405, 70))
        # self.pieces.add(self.piece_L)

        self.all_sprites.add(self.backround, self.bottom, self.pieces, self.fallen)
        print(self.all_sprites)

    def move(self, x_coord=0, y_coord=0):
        for piece in self.pieces:
            piece.rect.move_ip(x_coord, y_coord)

    def check_for_collision(self):
        fallen_list = [sprite for sprite in self.fallen]
        for piece in self.pieces:
            if piece.rect.collidelist(fallen_list) != -1:
                for piece in self.pieces: 
                    self.fallen.add(piece)
                    self.pieces.remove(piece)
                fallen_list = []
                self.spawn_new_piece()
                return True
                                    
            elif piece.rect.colliderect(self.bottom):
                for piece in self.pieces: 
                    self.fallen.add(piece)
                    self.pieces.remove(piece)
                fallen_list = []

                self.spawn_new_piece()
                return True
        return False
                    
    def spawn_new_piece(self):
        SHAPES = [
            "SHAPE_I",
            "SHAPE_L",
            "SHAPE_T",
            "SHAPE_SQ"
        ]

        self.pieces = creator(choice(SHAPES), 540, 10)
        self.all_sprites.add(self.pieces)


    # def make_like_a_snake():
        # This will make the piece move like a snake
        # if we for some reason need it
        #
        # prev_x,prev_y = None, None
        # for piece in self.pieces:
        #     if not prev_x:
        #         prev_x = piece.rect.x
        #         prev_y = piece.rect.y
        #         piece.rect.move_ip(x,y)
        #     else:
        #         a,b = piece.rect.x, piece.rect.y
        #         piece.rect.move_ip(prev_x-a,prev_y-b)
        #         prev_x, prev_y = a,b
