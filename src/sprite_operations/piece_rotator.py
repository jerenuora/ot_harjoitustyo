import pygame
from sprites.block import Block

SHAPES = {
    "SHAPE_I": {
        "RIGHT": [64, -64, 64, -32, 64, 0, 64, 32],
        "DOWN": [-64, 64,  -32, 64, 0, 64, 32, 64],
        "LEFT": [64, -64, 64, -32, 64, 0, 64, 32],
        "UP": [-64, 64,  -32, 64, 0, 64, 32, 64]
    },
    "SHAPE_L": {
        "RIGHT": [32, 0, 32, 32, 32, 64, 64, 64],
        "DOWN": [-32, 32,  0, 32, 32, 32, -32, 64],
        "LEFT": [0, -32, 32, -32, 32, 0, 32, 32],
        "UP": [0, 32, 32, 32, 64, 0, 64, 32]
    },
    "SHAPE_T": {
        "RIGHT": [32, 0, 32, 32, 32, 64, 64, 32],
        "DOWN": [-32, 32, 0, 32, 0, 64, 32, 32],
        "LEFT": [32, -32, 32, 0, 32, 32, 0, 0],
        "UP": [32, 0, 0, 32, 32, 32, 64, 32]
    },
    "SHAPE_SQ": {
        "RIGHT": [0, 0, 0, 32, 32, 0, 32, 32],
        "DOWN": [0, 0, 0, 32, 32, 0, 32, 32],
        "LEFT": [0, 0, 0, 32, 32, 0, 32, 32],
        "UP": [0, 0, 0, 32, 32, 0, 32, 32]
    },
    "SHAPE_J": {
        "RIGHT": [32, 0, 64, 0, 32, 32, 32, 64],
        "DOWN": [-32, 32,  0, 32, 32, 32, 32, 64],
        "LEFT": [0, 32, 32, -32, 32, 0, 32, 32],
        "UP": [0, 0, 0, 32, 32, 32, 64, 32]
    },
    "SHAPE_S": {
        "RIGHT": [32, -32, 32, 0, 64, 0,   64, 32],
        "DOWN": [-32, 64, 0, 32, 0, 64, 32, 32],
        "LEFT":  [32, -32, 32, 0, 64, 0, 64, 32],
        "UP": [-32, 64, 0, 32, 0, 64, 32, 32]
    },
    "SHAPE_Z": {
        "RIGHT": [64, -32, 32, 0, 64, 0, 32, 32],
        "DOWN": [-32, 32, 0, 32, 0, 64, 32, 64],
        "LEFT":  [64, -32, 32, 0, 64, 0, 32, 32],
        "UP": [-32, 32, 0, 32, 0, 64, 32, 64]
    },
}

def rotator(shape, spot_x, spot_y, orientation):
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
