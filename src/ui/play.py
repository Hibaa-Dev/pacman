from src.utils.global_data import GameState, VIRTUAL_H, VIRTUAL_W
from src.utils import global_data
import pygame


class Play:
    def __init__(self, canvas, clock):
        self.canvas = canvas
        self.clock = clock
        self.start_bg = pygame.image.load('assets/play_img/start.jpg')

    def start(self):
        bg = pygame.transform.scale(self.start_bg, (VIRTUAL_W, VIRTUAL_H))
        self.canvas.blit(bg, (0, 0))

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU

    def render(self):
        self.start()
