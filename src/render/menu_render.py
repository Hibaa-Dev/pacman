from src.ui.button import Button
from typing import List
import pygame


class Main_menu:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.background = pygame.image.load('assets/images/menu.jpg')
        self.current_w, self.current_h = screen.get_size()
        self.buttons: List[Button] = []
        self.focused_button_index: int = 0
        self.set_menu()

    def set_menu(self) -> None:

        x = self.current_w // 2 - 400
        y = int (self.current_h * (280 / 1080) + 250)

        self.buttons = [
            Button(lambda: 'PLAY', self.screen,
                    'assets/images/start.jpg', x, y, 'assets/images/hover_start.png'),
            Button(lambda: 'INSTRUCTIONS', self.screen,
                    'assets/images/Instr.jpg', x, y, 'assets/images/hover_instru.png'),
            Button(lambda: 'EXIT', self.screen,
                    'assets/images/Exit.jpg', x, y, 'assets/images/hover_exit.png')
        ]

        if self.buttons:
            self.buttons[0].set_focus()

        for button in self.buttons:
            button.y = y
            y += 200

    def render(self) -> None:
        bg = pygame.transform.scale(self.background, (self.current_w, self.current_h))
        self.screen.blit(bg, (0, 0))
        for button in self.buttons:
            button.render()
