import os
import pygame


dirname = os.path.dirname(__file__)


def img_loader(filename):
    """Loads the images for the spites

    Args:
        filename (str): Name of the image file

    Returns:
        pygame.image: pygame image
    """

    return pygame.image.load(
        os.path.join(dirname, "..", "assets", filename)
    )
