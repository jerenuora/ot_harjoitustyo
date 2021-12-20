from random import choice
import pygame

from sprites.block import Block
from sprites.bottom import Bottom
from sprites.background import Board
from sprites.buttons import Button
from sprite_operations.operations import creator, rotator


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
        self.button = Button(play=True)
        self.bottom = Bottom()
        self.spawn_new_piece()
        self.score = 0

    def move(self, x_coord=0, y_coord=0):
        """Moves the gamepiece

        Args:
            x_coord (int, optional): Amount of movement in the x-plane. Defaults to 0.
            y_coord (int, optional): Amount of movement in the y-plane. Defaults to 0.
        """
        if not self.enforce_right_boundary(self.pieces) and x_coord >= 0:
            for piece in self.pieces:
                piece.rect.move_ip(x_coord, y_coord)
        elif not self.enforce_left_boundary(self.pieces) and x_coord <= 0:
            for piece in self.pieces:
                piece.rect.move_ip(x_coord, y_coord)

    def enforce_right_boundary(self, pieces):
        """Making sure the gamepiece doesn't go over the right edge.

        Takes the maximum x-coordinate of the spritegroup and compares that to the border.

        Args:
            pieces (spritegroup): The gamepiece

        Returns:
            Bool: False if within bounds, True if outside
        """
        if max([piece.rect.x for piece in pieces]) > 763:
            return True
        return False

    def enforce_left_boundary(self, pieces):
        """Making sure the gamepiece doesn't go over the left edge.

        Takes the minimum x-coordinate of the spritegroup and compares that to the border.

        Args:
            pieces (spritegroup): The gamepiece

        Returns:
            Bool: False if within bounds, True if outside
        """
        if min([piece.rect.x for piece in pieces]) < 370:
            return True
        return False

    def rotate(self):
        """Calculates the upper leftmost edge of the gamepiece spritegroup

        Deletes the previous gamepiece,
        and calls the rotator function to create a new, rotated one, in its place

        """
        min_x, min_y = float('inf'), float('inf')
        orientation = ""
        for piece in self.pieces:
            if piece.rect.x < min_x:
                min_x = piece.rect.x
            if piece.rect.y < min_y:
                min_y = piece.rect.y
            orientation = piece.orientation
        rotated_piece = rotator(self.next_piece, min_x, min_y, orientation)
        if self.enforce_rotation_ability(rotated_piece):
            self.pieces.empty()
            self.pieces.add(rotated_piece)
            self.add_all_sprites()

    def enforce_rotation_ability(self, rotated_piece):
        """

        Args:
            rotated_piece ([type]): [description]

        Returns:
            Bool: True if piece can be rotated, False if not
        """
        left = min([piece.rect.x for piece in rotated_piece])
        right = max([piece.rect.x for piece in rotated_piece])
        if left > 338 and right < 796 and not self.check_fallen_collision():
            return True
        return False

    def check_for_collision(self, x_coord=0, y_coord=0):
        """Checks if the gamepiece has collided with the bottom, or the old fallen pieces

        When a collision is detected, adds gamepiece to the fallen-pieces spritegroup,
        and calls a function to create a new gamepiece

        Returns:
            Bool: True if a collision happened, False if not
        """
        if self.check_fallen_collision():
            for piece in self.pieces:
                piece.rect.move_ip(-x_coord, -y_coord)
            self.fallen.add(self.pieces)
            self.add_all_sprites()
            self.spawn_new_piece()
            return True

        if pygame.sprite.spritecollideany(self.bottom,self.pieces):

            self.fallen.add(self.pieces)
            self.add_all_sprites()
            self.spawn_new_piece()
            return True
        return False

    def check_for_collision_sideways(self, x_coord=0, y_coord=0):
        """Checks if the gamepiece has collided with the old fallen pieces sideways

        When a collision is detected, the gamepiece is moved backwards one step

        Returns:
            Bool: True if a collision happened, False if not
        """
        for piece in self.pieces:
            piece.rect.move_ip(x_coord, y_coord)
        if self.check_fallen_collision():
            for piece in self.pieces:
                piece.rect.move_ip(-x_coord, -y_coord)
            return True
        for piece in self.pieces:
            piece.rect.move_ip(-x_coord, -y_coord)

        return False

    def check_for_full_row(self):
        """Check to see if a row is full of fallen gamepieces, and if so, delete the row
        """
        table = {}
        sum_of_x_coordinates_for_full_row = 7784
        rows = [(piece.rect.x, piece.rect.y) for piece in self.fallen]
        for row in rows:
            if row[1] in table:
                table[row[1]] += row[0]
            else:
                table[row[1]] = row[0]
        for y_coord, x_coord in table.items():
            if x_coord == sum_of_x_coordinates_for_full_row:
                for piece in self.fallen:
                    if piece.rect.y == y_coord:
                        piece.kill()
                    elif piece.rect.y < y_coord:
                        piece.rect.move_ip(0, 32)
                self.score += 1
    def check_for_top_reach(self):
        """Check if the gamepiece collides with the already fallen gamepieces at the spawn site

        Returns:
            Bool: True if collision has happened, False if not
        """
        if self.check_fallen_collision():
            return True
        return False

    def check_fallen_collision(self):
        """Check if the gamepiece has collided with the already fallen gamepieces

        Returns:
            Bool: True if collision has happened, False if not
        """
        if pygame.sprite.groupcollide(self.pieces, self.fallen, False, False):
            return True
        return False

    def spawn_new_piece(self):
        """Calls the function to pick a new shape for a gampiece,
        and a function to create a gamepiece, and adds it to the spritegroup to be rendered
        """
        self.pick_next()
        self.pieces = creator(self.next_piece, 540, 10)
        self.add_all_sprites()

    def pick_next(self):
        """Pick a new shape for gamepiece
        """
        self.next_piece = choice(SHAPES)

    def change_button(self):
        """Change the play button from "PLAY" to "PAUSE" and back"""
        self.button = Button(play=not self.button.play)
        self.add_all_sprites()

    def add_all_sprites(self):
        """Add all the different sprites and spritegroups to the group that is then rendered in Loop
        """
        self.all_sprites.empty()
        self.all_sprites.add(
            self.background,
            self.button,
            self.bottom,
            self.fallen,
            self.pieces,

        )
