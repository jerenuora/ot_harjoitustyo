import pygame
from sprite_operations.img_loader import img_loader


class Bottom(pygame.sprite.Sprite):
    """A class to greate the bottom floor of the game area

    """
    def __init__(self, x_coord=340, y_coord=730):
        """Set up the bottom piece

        Args:
            x_coord (int, optional): x-coordinate. Defaults to 340.
            y_coord (int, optional): y-coordinate. Defaults to 730.
        """
        super().__init__()
        self.image = img_loader("bottom.png")
        self.rect = self.image.get_rect()

        self.rect.x = x_coord
        self.rect.y = y_coord
