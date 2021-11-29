from random import choice
import pygame
from sprites.bottom import Bottom
from sprites.backround import Board
from sprite_operations.piece_creator import creator
from sprite_operations.piece_rotator import rotator


SHAPES = [
    "SHAPE_I",
    "SHAPE_L",
    "SHAPE_T",
    "SHAPE_SQ"
]


class GameState:
    def __init__(self):
        self.pick_next()
        self.all_sprites = pygame.sprite.Group()
        self.pieces = creator(self.next_piece, 540, 10)
        self.fallen = pygame.sprite.Group()
        self.backround = Board(0, 0)
        self.bottom = pygame.sprite.Group()
        self.bottom.add(Bottom())

        self.all_sprites.add(
            self.backround,
            self.bottom,
            self.pieces,
            self.fallen
        )

    def move(self, x_coord=0, y_coord=0):
        for piece in self.pieces:
            piece.rect.move_ip(x_coord, y_coord)

    def rotate(self):
        min_x, min_y = 10000, 10000
        count = 0
        orientation = ""
        for piece in self.pieces:
            if piece.rect.x < min_x:
                min_x = piece.rect.x
            if piece.rect.y < min_y:
                min_y = piece.rect.y
            count += 1
            orientation = piece.orientation
        new = rotator(self.next_piece, min_x, min_y, orientation)
        self.pieces.empty()
        self.pieces.add(new)
        self.all_sprites.add(self.pieces)
        self.pieces = new
        self.all_sprites.add(self.pieces)

    def check_for_collision(self):

        if pygame.sprite.groupcollide(self.pieces, self.fallen, False, False):
            self.move(x_coord=0, y_coord=-32)
            self.fallen.add(self.pieces)
            self.spawn_new_piece()
            return True

        if pygame.sprite.groupcollide(self.pieces, self.bottom, False, False):
            self.fallen.add(self.pieces)
            self.spawn_new_piece()
            return True
        return False

    def spawn_new_piece(self):
        self.pick_next()
        self.pieces = creator(self.next_piece, 540, 10)
        self.all_sprites.add(self.pieces)

    def pick_next(self):
        self.next_piece = choice(SHAPES)
