import pygame
from sprites.block import Block


SHAPES = {
    "SHAPE_I": [0, 0, 0, 32, 0, 64, 0, 96],
    "SHAPE_L": [0, 0, 0, 32, 0, 64, 32, 64],
    "SHAPE_T": [0, 0, 0, 32, 0, 64, 32, 32],
    "SHAPE_O": [0, 0, 0, 32, 32, 0, 32, 32],
    "SHAPE_J": [0, 0, 32, 0, 0, 32, 0, 64],
    "SHAPE_S": [32, 0, 32, 32,  0, 32, 0, 64],
    "SHAPE_Z": [32, 0, 32, 32,  0, 32, 0, 64]
    }


def creator(shape, spot_x, spot_y):
    piece = pygame.sprite.Group()
    for i in range(0, 8, 2):
        x_coord = SHAPES[shape][i] + spot_x
        y_coord = SHAPES[shape][i+1] + spot_y
        piece.add(Block(x_coord, y_coord,shape))
    return piece
