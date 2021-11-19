import pygame
from gamestate import GameState

def main():

    # AN UNSTRUCTURED MESS FOR SURE, BUT JUST TO GET STARTED ## 
    
    display_x = 600
    display_y = 700
    display = pygame.display.set_mode((display_x,display_y))

    pygame.display.set_caption("TETRIS")

    display.fill((0,34,249))
    pygame.draw.rect(display, (46,155,86), (100,20,400,660))
    pygame.draw.rect(display, (46,155,86), (10,10,80,50))
    # pygame.display.flip()
    # print("Tetris")

    game_state = GameState()
    pygame.init()

    game_state.all_sprites.draw(display)
    pygame.display.update()

    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if events.type == pygame.KEYDOWN:

                if events.key == pygame.K_ESCAPE:
                        exit()

if __name__ == "__main__":

    main()