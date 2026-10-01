from typing import Callable
import pygame


class Button:
    def __init__(self, command: Callable, screen, normal,
                 x, y, id, hovered = None) -> None:
        self.id = id
        self.command = command
        self.screen = screen
        self.x: int = x
        self.y: int = y
        self.focus = False

        self.normal_img = pygame.image.load(normal).convert_alpha()
        self.hovered_img = pygame.image.load(hovered).convert_alpha() if hovered else None

        self.width, self.height = self.normal_img.get_size()

    def set_size(self, target_width: int) -> None:
 
        ratio = self.normal_img.get_height() / self.normal_img.get_width()
        self.width = target_width
        self.height = int(target_width * ratio)
        self.normal_img = pygame.transform.smoothscale(
            self.normal_img, (self.width, self.height))

        if self.hovered_img:
            self.hovered_img = pygame.transform.smoothscale(
                self.hovered_img, (self.width, self.height))

    def render(self) -> None:
        img = self.hovered_img if (self.focus and self.hovered_img) else self.normal_img
        # print(f"button {self.id}, is focused == {self.focus}")
        # img = self.hovered_img if self.focus == True else self.normal_img
        self.screen.blit(img, (self.x, self.y))

    def set_focus(self) -> None:
        self.focus = True

    def remove_focus(self) -> None:
        self.focus = False
