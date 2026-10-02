from src.utils.global_data import GameState
from src.utils import global_data
import pygame


class Instructions:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.img = pygame.image.load('assets/images/Instructions.png')
        self.canvas_w, self.canvas_h = self.canvas.get_size()
        self.img_w, self.img_h = self.img.get_size()

    def render(self):
        x = (self.canvas_w - self.img_w) // 2
        self.canvas.blit(self.img, (x, 0))

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU
