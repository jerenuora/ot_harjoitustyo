import os
import pygame

dirname = os.path.dirname(__file__)


def img_loader( filename):

    return pygame.image.load(
        os.path.join(dirname, "assets", filename)
    )
