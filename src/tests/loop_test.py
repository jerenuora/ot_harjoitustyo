import unittest
import pygame

from loop import Loop
from gamestate import GameState

class MockEvent:
    def __init__(self, type, key):
        self.type = type
        self.key = key
    def unicode(self,key):
        return key.upper()
class MockEventQueue:
    def __init__(self, events):
        self._events = events

    def get_events(self):
        return self._events

class MockDrawDisplay:
    def draw_display(self):
        pass
    def draw_display_gameover(self,name):
        pass

class MockClock:
    def tick(self, fps):
        pass

    def get_ticks(self):
        return 0

class TestLoop(unittest.TestCase):

    def setUp(self):
        self.gamestate = GameState()

    def test_loop_starts_and_plays(self):
        events = [MockEvent(pygame.KEYDOWN, pygame.K_RETURN),
            MockEvent(pygame.KEYDOWN, pygame.K_SPACE),
            MockEvent(pygame.KEYDOWN, pygame.K_ESCAPE)
            ]
        loop = Loop(self.gamestate,MockDrawDisplay(),MockEventQueue(events),MockClock())
        loop.start()
        self.assertFalse(loop.pause)

    def test_loop_starts_and__game_ends(self):
        events = [
            MockEvent(pygame.KEYDOWN, pygame.K_RETURN),
            MockEvent(pygame.KEYDOWN, pygame.K_ESCAPE)
            ]

        loop = Loop(self.gamestate,MockDrawDisplay(),MockEventQueue(events),MockClock())
        loop.start()
        self.assertEqual(loop.name, "")
        