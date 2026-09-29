from src.input.input_manager import Input_manager
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

        self.running = True
        self.input_manager = Input_manager(self.running)

    def run(self):
        while self.running:
            self.input_manager.get_input()
            # game_rules()
            # render()
            # pygame.display.flip()

        pygame.quit()