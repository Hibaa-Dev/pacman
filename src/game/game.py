from src.input.input_manager import Input_manager
from src.render.menu_render import Main_menu
from .gameState import GameState
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

        self.state = GameState.MENU
        self.running = True
        self.menu = Main_menu(self.screen)
        self.input_manager = Input_manager(self.state, self.menu)

    def run(self):
        while self.running:
            action = self.input_manager.get_input()
            if action == 'QUIT':
                self.running = False
            if action == GameState.MENU:
                self.menu.render()

            pygame.display.flip()
        pygame.quit()