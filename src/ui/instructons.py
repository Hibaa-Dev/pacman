from src.utils.global_data import GameState
from src.utils import global_data
import pygame

#  old code 
# class Instructions:
#     def __init__(self, canvas) -> None:
#         self.canvas = canvas
#         self.img = pygame.image.load('assets/images/Instructions.png')
#         self.canvas_w, self.canvas_h = self.canvas.get_size()
#         self.img_w, self.img_h = self.img.get_size()
#         self.scroll_y = 0

#     def render(self):
#         y0 = 0
#         y1 = self.img_h
#         scroll_speed = 3

#         y0 =- scroll_speed
#         y1 =- scroll_speed

#         if y0 <= -self.canvas_h:
#             y0 = self.img_h
#         if y1 <= -self.canvas_h:
#             y1 = self.img_h

#         x = (self.canvas_w - self.img_w) // 2
#         self.canvas.blit(self.img, (x, y0))
#         self.canvas.blit(self.img, (x, y1))


class Instructions:
    def __init__(self, canvas) -> None:
        self.canvas = canvas
        self.img = pygame.image.load('assets/images/Instructions.png')
        self.canvas_w, self.canvas_h = self.canvas.get_size()
        self.img_w, self.img_h = self.img.get_size()
        self.scroll_y = 0.0          # CHANGED — this now actually gets used
        self.scroll_speed = 3        # CHANGED — moved out of render(), no longer reset every frame

    def render(self):
        # CHANGED — advance persistent state instead of recomputing from scratch
        self.scroll_y -= self.scroll_speed

        # Wrap back to the start once the image has fully scrolled past.
        if self.scroll_y <= -self.img_h: # -3 < -100 ===> -102 <= -100
            self.scroll_y += self.img_h

        x = (self.canvas_w - self.img_w) // 2

        # Draw two copies stacked vertically so there's no gap while wrapping.
        self.canvas.blit(self.img, (x, self.scroll_y + self.img_h))
        self.canvas.blit(self.img, (x, self.scroll_y))


    def treat_input(self, key):
        if key == pygame.K_ESCAPE:
            global_data.GAME_STATE = GameState.MENU
