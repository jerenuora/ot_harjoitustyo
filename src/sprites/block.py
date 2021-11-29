import pygame
from img_loader import img_loader


class Block(pygame.sprite.Sprite):

    def __init__(self, x_coord=0, y_coord=0, shape="", orientation="RIGHT"):
        super().__init__()
        self.image = img_loader("x_block copy.png")
        self.rect = self.image.get_rect()
        self.type = shape
        self.orientation = orientation
        self.rect.x = x_coord
        self.rect.y = y_coord
