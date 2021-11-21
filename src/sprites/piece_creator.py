import pygame
from sprites.block import Block


SHAPES = {"SHAPE_I": [0,0,0,32,0,64,0,96]}

def creator(shape,spot_x,spot_y):
    piece = pygame.sprite.Group()
    for i in range(0,8,2):
        x = SHAPES[shape][i] + spot_x
        y = SHAPES[shape][i+1] + spot_y
        piece.add(Block(x,y))
    return piece