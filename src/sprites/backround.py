import pygame
from img_loader import img_loader


class Board(pygame.sprite.Sprite):

    def __init__(self, x_coord=0, y_coord=0):
        super().__init__()
        self.image = img_loader("board.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
