import pygame
from img_loader import img_loader


class Bottom(pygame.sprite.Sprite):

    def __init__(self, x_coord=340, y_coord=730):
        super().__init__()
        self.image = img_loader("bottom.png")
        self.rect = self.image.get_rect()

        self.rect.x = x_coord
        self.rect.y = y_coord
