from typing import Callable
import pygame


class Button:
    def __init__(self, command: Callable, screen, normal,
                 x, y, hovered = None):
        self.command = command
        self.screen = screen
        self.normal = normal
        self.hovered = hovered
        self.x: int = x
        self.y: int = y
        self.focus = False

    def render(self):
        if self.focus and self.hovered:
            img = pygame.image.load(self.hovered)
        else:
            img = pygame.image.load(self.normal)

        button = pygame.transform.scale(img, (600, 170))
        self.screen.blit(button, (self.x, self.y))

    def set_focus(self):
        self.focus = True

    def remove_focus(self):
        self.focus = False
