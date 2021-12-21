"""
A single block of gamepiece sprite
"""
import pygame
from sprite_operations.img_loader import img_loader


class Block(pygame.sprite.Sprite):
    """
    Class for a single block of gamepiece. Many of these together form a whole gamepice
    """

    def __init__(self, x_coord=0, y_coord=0, shape="", orientation="DOWN"):
        super().__init__()
        self.image = img_loader("x_block.png")
        self.rect = self.image.get_rect()
        self.type = shape
        self.orientation = orientation
        self.rect.x = x_coord
        self.rect.y = y_coord
