from src.utils.global_data import VIRTUAL_H, VIRTUAL_W
import pygame


class Start:
    def __init__(self, canvas, clock):
        self.canvas = canvas
        self.clock = clock
        self.bg = pygame.image.load('assets/play_img/start.png')
        self.loading = pygame.image.load('assets/play_img/loading_bar.png')
        self.progess = 0

    def start(self):
        bg = pygame.transform.scale(self.bg, (VIRTUAL_W, VIRTUAL_H))
        self.canvas.blit(bg, (0, 0))