import pygame

class Loop:
    def __init__(self, gamestate, display):
        self._gamestate = gamestate
        self._display = display
        self._clock = pygame.time.Clock()
        self._timer = 0

    def start(self):
        while True:
            if self._eventhandler() == False:
                break
            
            self._renderer()

            self._clock.tick(6)

    def _eventhandler(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._gamestate.move(x=-33)
                if event.key == pygame.K_RIGHT:
                    self._gamestate.move(x=33)
                if event.key == pygame.K_UP:
                    self._gamestate.move(y=-33)
                if event.key == pygame.K_DOWN:
                    self._gamestate.move(y=33)
                if event.key == pygame.K_ESCAPE:
                        return False
            elif event.type == pygame.QUIT:
                return False

    def _renderer(self):
        self._gamestate.all_sprites.draw(self._display)
        self.progress_time()
        pygame.display.update()

    def progress_time(self):
        print(str(self._clock))
        
        self._timer += self._clock.get_time()
        if self._timer > 600:
            self._gamestate.move(y=33)
            self._timer = 0
