from src.utils.global_data import GameState
from src.utils import global_data
import pygame


class Instructions:
    def __init__(self, canvas, width, height) -> None:
        self.canvas = canvas
        self.width = width
        self.height = height
        self.canvas_seize = self.canvas.get_seize()
        self.img_w, self.img_h = 
        self.img = pygame.image.load('assets/images/Instructions.png')

    def render(self):

        bg = pygame.transform.scale(self.img, (self.width, 3144))
        self.canvas.blit(bg, (0, 0))

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU