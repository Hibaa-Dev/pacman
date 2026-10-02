from src.utils.global_data import VIRTUAL_H, VIRTUAL_W,  GameState
from src.utils import global_data
from src.ui.instructons import Instructions
from src.ui.menu import Main_menu
import pygame


class Game:
    def __init__(self):
        pygame.init()

        info = pygame.display.Info()
        self.current_w, self.current_h = (
            info.current_w, info.current_h
        )
        self.screen = pygame.display.set_mode((self.current_w, self.current_h), pygame.RESIZABLE)
        self.canvas = pygame.Surface((VIRTUAL_W, VIRTUAL_H))

        self.running = True
        self.main_menu = Main_menu(self.canvas)
        self.instructions = Instructions(self.canvas)

    def get_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if global_data.GAME_STATE == GameState.MENU:
                    action = self.main_menu.treat_input(event.key)
                    if action:
                        action.command()
                if global_data.GAME_STATE == GameState.INSTRUCTIONS:
                    self.instructions.treat_input(event.key)

    def render(self):
        self.canvas.fill((0, 0, 0))
        if global_data.GAME_STATE == GameState.MENU:
            self.main_menu.render()

        if global_data.GAME_STATE == GameState.INSTRUCTIONS:
            self.instructions.render()

        self.scaled_canvas = pygame.transform.scale(
            self.canvas, (self.current_w, self.current_h)
        )
        self.screen.blit(self.scaled_canvas, (0, 0))

    def run(self):
        while self.running:
            self.get_input()
            self.render()
   
            pygame.display.flip()
        pygame.quit()
