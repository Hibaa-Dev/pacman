from src.utils.global_data import GameState
from src.utils import global_data
import pygame


class Instructions:
    def __init__(self, canvas, clock) -> None:
        self.canvas = canvas
        self.clock = clock
        self.img = pygame.image.load('assets/images/Instructions.png')
        self.canvas_w, self.canvas_h = self.canvas.get_size()
        self.img_w, self.img_h = self.img.get_size()
        self.header_height: int = 570
        self.scroll_y: float = 0.0
        self.scroll_speed: int = 15
        self.paused: bool = False

    def render(self):
        dt = self.clock.tick(60) / 100
        x = (self.canvas_w - self.img_w) // 2

        # Header Erea
        header = pygame.Rect(0, 0, self.img_w, self.header_height)
        self.canvas.blit(self.img, (x, 0), header)

        # Scrolling area
        if not self.paused:
            self.scroll_y -= self.scroll_speed * dt
        if self.scroll_y <= -self.img_h:
            self.scroll_y += self.img_h

        scroll_area = pygame.Rect(
            0, self.header_height,
            self.img_w,
            self.img_h - self.header_height
        )
        self.canvas.set_clip(scroll_area)
        self.canvas.blit(self.img, (x, self.scroll_y + (self.img_h - self.header_height)))
        self.canvas.blit(self.img, (x, self.scroll_y))
        self.canvas.set_clip(None)

    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            self.scroll_y = 0.0
            self.paused = False
            global_data.GAME_STATE = GameState.MENU
        if key == pygame.K_SPACE:
            self.paused = not self.paused
