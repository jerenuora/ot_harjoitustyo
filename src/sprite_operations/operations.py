"""To create a gamepice, and to rotate one
"""
import pygame
from sprite_operations.json_loader import load_shapes
from sprites.block import Block


SHAPES = load_shapes()


def creator(shape, spot_x, spot_y, direction="DOWN"):
    """
    Create new gamepiece given the shape, x,y coordinates and the directional instruction

    Args:
        shape (str): The shape of the gamepiece, to get its instructions from the json
        spot_x (int): x-coordinates
        spot_y (int): y-coordinates
        direction (str, optional): The  orientation of the gamepiece. Defaults to "DOWN".

    Returns:
        spritegroup: The new gamepiece
    """
    piece = pygame.sprite.Group()
    for i in range(0, 8, 2):
        x_coord = SHAPES[shape][direction][i] + spot_x
        y_coord = SHAPES[shape][direction][i+1] + spot_y
        piece.add(Block(x_coord, y_coord, shape))
    return piece


def rotator(shape, spot_x, spot_y, orientation):
    """
    Take the location and oriantetion of a gamepiece and return a new one, rotated

    Args:
        shape (str): The shape of the gamepiece, to get its instructions from the json
        spot_x (int): x-coordinates
        spot_y (int): y-coordinates
        orientation (str): The old orientation of the gamepiece,
                           for the new one to be picked from the list

    Returns:
        spritegroup: The new gamepiece
    """

    piece = pygame.sprite.Group()
    orientation_rotation = ["UP","RIGHT","DOWN","LEFT"]
    or_n = orientation_rotation.index(orientation)
    if or_n == len(orientation_rotation)-1:
        or_n = -1
    new_or = orientation_rotation[or_n+1]

    for i in range(0, 8, 2):

        x_coord = SHAPES[shape][new_or][i] + spot_x
        y_coord = SHAPES[shape][new_or][i+1] + spot_y
        piece.add(Block(x_coord, y_coord, orientation=new_or))
    return piece
