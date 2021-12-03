import sys
import pygame
from gamestate import GameState
from loop import Loop


def main():

    display_x = 1145
    display_y = 800
    display = pygame.display.set_mode((display_x, display_y))
    pygame.display.set_caption("TETRIS")
    game_state = GameState(display)
    pygame.init()
    loop = Loop(game_state, display)
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
