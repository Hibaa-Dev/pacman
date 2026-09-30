from src.game.gameState import GameState
from .menu_input import Menu_input
import pygame


class Input_manager:
    def __init__(self, state, menu) -> None:
        self.state = state
        self.menu_input = Menu_input(menu)

    def get_input(self) -> str | None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'QUIT'
            if self.state == GameState.MENU:
                action = self.menu_input.handle_event(event)
                return action
                    
        return None

