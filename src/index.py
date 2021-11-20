import pygame
from gamestate import GameState
from img_loader import img_loader
from loop import Loop
def main():


    display_x = 1145
    display_y = 800
    display = pygame.display.set_mode((display_x,display_y))

    pygame.display.set_caption("TETRIS")

    display.fill((255,255,255))


    game_state = GameState()
    pygame.init()
    loop = Loop(game_state,display)
    game_state.all_sprites.draw(display)
    pygame.draw.line(display, (0,135,255), (341,10),(341,781),width=5)
    pygame.draw.line(display, (0,135,255), (794,10),(794,781),width=5)
    pygame.draw.line(display, (0,135,255), (341,10),(794,10),width=5)
    pygame.draw.line(display, (0,135,255), (341,781),(794,781),width=5)
    loop.start()
    #pygame.display.update()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if events.type == pygame.KEYDOWN:

                if events.key == pygame.K_ESCAPE:
                        exit()

if __name__ == "__main__":

    main()


   