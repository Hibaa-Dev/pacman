from src.utils.global_data import GameState
from src.utils import global_data
import pygame


class Instructions:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.img = pygame.image.load('assets/images/Instructions.png')
        self.canvas_w, self.canvas_h = self.canvas.get_size()
        self.img_w, self.img_h = self.img.get_size()
        self.scroll_y = 0

    def render(self):
        y0 = 0
        y1 = self.img_h
        scroll_speed = 3

        y0 =- scroll_speed
        y1 =- scroll_speed

        if y0 <= -self.canvas_h:
            y0 = self.img_h
        if y1 <= -self.canvas_h:
            y1 = self.img_h

        x = (self.canvas_w - self.img_w) // 2
        self.canvas.blit(self.img, (x, y0))
        self.canvas.blit(self.img, (x, y1))

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU
