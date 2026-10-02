from src.ui.button import Button
from src.utils.global_data import VIRTUAL_H, VIRTUAL_W, GameState
from src.utils import global_data
import pygame


class Main_menu:

    def __init__(self, canvas) -> None:

        PANEL_LEFT = 410
        PANEL_RIGHT = 1560
        self.PANEL_CENTER_X = (PANEL_LEFT + PANEL_RIGHT) // 2
        self.canvas = canvas
        self.background = pygame.image.load('assets/images/menu.jpg').convert()
        self.current_w, self.current_h = VIRTUAL_W, VIRTUAL_H
        self.focused_button_index: int = 0
        self.start_game = False
        self.buttons = []
        self.set_menu()

    def set_menu(self):
        button_w = int(self.current_w * 0.11)
        x = self.PANEL_CENTER_X - button_w // 2
        first_y = int(self.current_h * 0.35)
        gap = int(self.current_h * 0.015)

        specs = [
            (lambda: self._play, 'assets/images/start.jpg', "play", 'assets/images/hover_start.png'),
            (lambda: self._show_instructions(), 'assets/images/Instr.jpg', "instructions", 'assets/images/hover_instru.png'),
            (lambda: exit(0), 'assets/images/Exit.jpg', 'exit', 'assets/images/hover_exit.png'),
        ]
        current_y = first_y
        for cmd, normal, id, hovered in specs:
            btn = Button(cmd, self.canvas, normal, x, current_y, id, hovered)
            btn.set_size(button_w)
            btn.y = current_y
            self.buttons.append(btn)
            current_y += btn.height + gap

        if self.buttons:
            self.buttons[0].set_focus()

    def render(self):
        bg = pygame.transform.scale(self.background, (VIRTUAL_W, VIRTUAL_H))
        self.canvas.blit(bg, (0, 0))
        for button in self.buttons:
            button.render()

    def _play(self):
        global_data.GAME_STATE = GameState.PLAY

    def _show_instructions(self):
        global_data.GAME_STATE = GameState.INSTRUCTIONS

    def treat_input(self, key: int):
        if key == pygame.K_w or key == pygame.K_UP:
            self.buttons[self.focused_button_index].remove_focus()
            self.focused_button_index = (self.focused_button_index - 1) % len(self.buttons)
            self.buttons[self.focused_button_index].set_focus()

        if key == pygame.K_s or key == pygame.K_DOWN:
            self.buttons[self.focused_button_index].remove_focus()
            self.focused_button_index = (self.focused_button_index + 1) % len(self.buttons)
            self.buttons[self.focused_button_index].set_focus()

        if key == pygame.K_RETURN:
            return self.buttons[self.focused_button_index]
