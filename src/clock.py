"""
For keeping track of time
"""
import pygame

class Clock:
    """
    A clock
    """
    def __init__(self):
        """Set up clock
        """
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Tick the clock

        Args:
            fps (int): number of frames to be ticked
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Get number of ticks passed

        Returns:
             (int): Ticks
        """
        return pygame.time.get_ticks()
