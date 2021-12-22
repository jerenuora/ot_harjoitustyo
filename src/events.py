"""
Event queue in its own class to make testing easier
"""

import pygame


class Events:
    """Gets events
    """

    def get_events(self):
        """Event getter

        Returns:
            pygame events
        """
        return pygame.event.get()
