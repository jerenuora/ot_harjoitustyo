from random import choice
import pygame
from sprites.bottom import Bottom
from sprites.background import Board
from sprite_operations.piece_creator import creator
from sprite_operations.piece_rotator import rotator


SHAPES = [
    "SHAPE_I",
    "SHAPE_L",
    "SHAPE_T",
    "SHAPE_O",
    "SHAPE_J",
    "SHAPE_S",
    "SHAPE_Z"
]


class GameState:
    """A class that keeps track of the state of the gamepieces and handles manipulating them
    """
    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.pieces = pygame.sprite.Group()
        self.fallen = pygame.sprite.Group()
        self.background = Board()
        self.bottom = pygame.sprite.Group()
        self.bottom.add(Bottom())
        self.add_all_sprites()
        self.spawn_new_piece()
        self.prev_move = ""

    def move(self, x_coord=0, y_coord=0, user="HUMAN"):
        if not self.enforce_right_boundary(self.pieces) and x_coord >= 0:
            for piece in self.pieces:
                piece.rect.move_ip(x_coord, y_coord)
            if user == "HUMAN":
                self.save_prev_move(x_coord, y_coord)
        elif not self.enforce_left_boundary(self.pieces) and x_coord <= 0:
            for piece in self.pieces:
                piece.rect.move_ip(x_coord, y_coord)
            if user == "HUMAN":
                self.save_prev_move(x_coord, y_coord)

    def enforce_right_boundary(self, pieces):
        max_x = max([piece.rect.x for piece in pieces])
        if max_x > 763:
            return True
        return False

    def enforce_left_boundary(self, pieces):
        if min([piece.rect.x for piece in pieces]) < 370:
            return True
        return False

    def save_prev_move(self, x_coord, y_coord):
        if y_coord == 32:
            self.prev_move = "DOWN"
        if x_coord == 32:
            self.prev_move = "RIGHT"
        if x_coord == -32:
            self.prev_move = "LEFT"

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
        self.pieces.empty()
        self.pieces.add(rotator(self.next_piece, min_x, min_y, orientation))
        self.add_all_sprites()

    def check_for_collision(self):

        if pygame.sprite.groupcollide(self.pieces, self.fallen, False, False):
            if self.prev_move == "DOWN":
                self.move(x_coord=0, y_coord=-32)
                self.fallen.add(self.pieces)
                self.spawn_new_piece()

            if self.prev_move == "LEFT":
                self.move(x_coord=32, user="SYSTEM")
            if self.prev_move == "RIGHT":
                self.move(x_coord=-32, user="SYSTEM")
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

    def add_all_sprites(self):
        self.all_sprites.empty()
        self.all_sprites.add(
            self.background,
            self.bottom,
            self.pieces,
            self.fallen
        )
