import pygame
from sprite_operations.img_loader import img_loader


class Board(pygame.sprite.Sprite):
    """A class to create the background of the game area

    """

    def __init__(self, x_coord=0, y_coord=0):
        """Set up the background

        Args:
            x_coord (int, optional): Upper left corner x-coordinate. Defaults to 0.
            y_coord (int, optional): Upper left corner y-coordinate. Defaults to 0.
        """
        super().__init__()
        self.image = img_loader("board.png")
        self.rect = self.image.get_rect()
        self.rect.x = x_coord
        self.rect.y = y_coord
