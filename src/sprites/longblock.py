import pygame
from sprites.block import Block



class Longblock(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.first = Block(0,0)
        self.second = Block(30,0)
        self.third = Block(60,0)
        self.fourth = Block(90,0)