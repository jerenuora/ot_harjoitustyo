import pygame
from sprite_operations.json_loader import load_shapes
from sprites.block import Block

SHAPES = load_shapes()


def rotator(shape, spot_x, spot_y, orientation):
    """Take the location and oriantetion of a gamepiece and return a new one, rotated

    Args:
        shape (str): The shape of the gamepiece, to get its instructions from the json
        spot_x (int): x-coordinates
        spot_y (int): y-coordinates
        orientation (str): The old orientation of the gamepiece

    Returns:
        spritegroup: The new gamepiece
    """

    piece = pygame.sprite.Group()
    for i in range(0, 8, 2):
        if orientation == "UP":
            new_or = "RIGHT"
        elif orientation == "RIGHT":
            new_or = "DOWN"
        elif orientation == "DOWN":
            new_or = "LEFT"
        elif orientation == "LEFT":
            new_or = "UP"

        x_coord = SHAPES[shape][new_or][i] + spot_x
        y_coord = SHAPES[shape][new_or][i+1] + spot_y
        piece.add(Block(x_coord, y_coord, orientation=new_or))
    return piece
