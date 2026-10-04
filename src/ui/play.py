from src.utils.global_data import GameState, VIRTUAL_H, VIRTUAL_W
from src.utils import global_data
from .start import Start
import pygame


class Play:
    def __init__(self, canvas, clock):
        self.canvas = canvas
        self.clock = clock
        self.start = Start(self.canvas, self.clock)

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU
 
    def render(self):
        self.start.start()
