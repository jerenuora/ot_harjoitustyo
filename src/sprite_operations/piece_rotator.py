import pygame
import json
from sprites.block import Block

with open('assets/shapefile_directions.json') as f:
    SHAPES = json.load(f)

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
