import pygame
from sprite_operations.json_loader import load_shapes
from sprites.block import Block


SHAPES = load_shapes()


def creator(shape, spot_x, spot_y, direction="DOWN"):
    piece = pygame.sprite.Group()
    for i in range(0, 8, 2):
        x_coord = SHAPES[shape][direction][i] + spot_x
        y_coord = SHAPES[shape][direction][i+1] + spot_y
        piece.add(Block(x_coord, y_coord, shape))
    return piece
