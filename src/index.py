"""
To set up pygame, gamestate, database and loop
"""
import sys
import pygame
from gamestate import GameState
from loop import Loop
from database.database_init import database_init
from ui.draw_display import DrawDisplay
from events import Events
from clock import Clock
def main():
    """
    Main function to set up pygame, a display area and to call the gameplay loop
    """

    display_x = 1145
    display_y = 800
    display = pygame.display.set_mode((display_x, display_y))
    pygame.display.set_caption("TETRIS")
    gamestate = GameState()
    pygame.init()
    database_init()
    draw_display = DrawDisplay(gamestate,display)
    events = Events()
    loop = Loop(gamestate,draw_display,Events(),Clock())
    loop.start()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_ESCAPE:
                    sys.exit()


if __name__ == "__main__":

    main()
