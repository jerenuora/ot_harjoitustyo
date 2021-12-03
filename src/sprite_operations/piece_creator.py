import pygame
import json
from sprites.block import Block


with open('assets/shapefile_directions.json') as f:
    SHAPES = json.load(f)

def creator(shape, spot_x, spot_y, direction="RIGHT"):
    piece = pygame.sprite.Group()
    for i in range(0, 8, 2):
        x_coord = SHAPES[shape][direction][i] + spot_x
        y_coord = SHAPES[shape][direction][i+1] + spot_y
        piece.add(Block(x_coord, y_coord,shape))
    return piece
