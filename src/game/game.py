import pygame


class Game:
    def __init__(self):
        pygame.init()

        # Screen configuration
        info = pygame.display.Info()
        self.current_w, self.current_h = (
            info.current_w, info.current_h
        )
        self.screen = pygame.display.set_mode((self.current_w, self.current_h))

    def run(self):
        running = True
        while running:
            get_input()
            game_rules()
            render()
            pygame.display.flip()
        pygame.quit()