import pygame
from img_loader import img_loader




class Block(pygame.sprite.Sprite):

    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = img_loader("x_block copy.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y