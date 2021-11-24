import pygame
from img_loader import img_loader




class Block(pygame.sprite.Sprite):

    def __init__(self, X=0, Y=0):
        super().__init__()
        self.image = img_loader("x_block copy.png")
        self.rect = self.image.get_rect()

        self.rect.x = X
        self.rect.y = Y