import pygame
from sprite_operations.img_loader import img_loader


class Button(pygame.sprite.Sprite):
    """A class to greate a play button

    """
    def __init__(self, x_coord=20, y_coord=20, play=True):
        """Set up the bottom piece

        Args:
            x_coord (int, optional): x-coordinate. Defaults to 20.
            y_coord (int, optional): y-coordinate. Defaults to 20.
        """
        self.play = play
        if play:
            button = "play"
        if not play:
            button = "pause"
        super().__init__()
        self.image = img_loader(button + ".png")
        self.rect = self.image.get_rect()

        self.rect.x = x_coord
        self.rect.y = y_coord
