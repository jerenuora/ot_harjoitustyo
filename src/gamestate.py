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
    """Keeps track of all the sprites and their locations

    """

    def __init__(self):
        """Constructor, that creates the spritegroups that contain the gamepieces
        """
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
        """Moves the gamepiece

        Args:
            x_coord (int, optional): Amount of movement in the x-plane. Defaults to 0.
            y_coord (int, optional): Amount of movement in the y-plane. Defaults to 0.
            user (str, optional): To see wether the move-command is coming from human-user or
                                    the game-logig function. Defaults to "HUMAN".
        """
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
        """Making sure the gamepiece doesn't go over the right edge.

        Takes the maximum x-coordinate of the spritegroup and compares that to the border.

        Args:
            pieces (spritegroup): The gamepiece

        Returns:
            Bool: False if within bounds, True if outside
        """
        max_x = max([piece.rect.x for piece in pieces])
        if max_x > 763:
            return True
        return False

    def enforce_left_boundary(self, pieces):
        """Making sure the gamepiece doesn't go over the left edge.

        Takes the maximum x-coordinate of the spritegroup and compares that to the border.

        Args:
            pieces (spritegroup): The gamepiece

        Returns:
            Bool: False if within bounds, True if outside
        """
        if min([piece.rect.x for piece in pieces]) < 370:
            return True
        return False

    def save_prev_move(self, x_coord, y_coord):
        """Saves the previous direction the gampiece moved.

        Used to keep the pieces from clipping inside eachother.

        Args:
            x_coord (int): The x-coordinate of the previous move.
            y_coord (int): The y-coordinate of the previous move.
        """
        if y_coord == 32:
            self.prev_move = "DOWN"
        if x_coord == 32:
            self.prev_move = "RIGHT"
        if x_coord == -32:
            self.prev_move = "LEFT"

    def rotate(self):
        """Calculates the upper leftmost edge of the gamepiece spritegroup

        Deletes the previous gamepiece,
        and calls the rotator function to create a new, rotated one, in its place

        """
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
        """Checks if the gamepiece has collided with the bottom, or the old fallen pieces

        When a collision is detected, adds gamepiece to the fallen-pieces spritegroup,
        and calls a function to create a new gamepiece

        Returns:
            Bool: True if a collision happened, False if not
        """

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
        """Calls the function to pick a new shape for a gampiece,
        and a function to create a gamepiece, and adds it to the spritegroup to be rendered
        """
        self.pick_next()
        self.pieces = creator(self.next_piece, 540, 10)
        self.all_sprites.add(self.pieces)

    def pick_next(self):
        """Pick a new shape for gamepiece
        """
        self.next_piece = choice(SHAPES)

    def add_all_sprites(self):
        """Add all the different sprites and spritegroups to the group that is then rendered in Loop
        """
        self.all_sprites.empty()
        self.all_sprites.add(
            self.background,
            self.bottom,
            self.pieces,
            self.fallen
        )
