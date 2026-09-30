import pygame


class Menu_input:

    def __init__(self, menu) -> None:
        self.menu = menu
        self.focused_button_index = 0

    def handle_event(self, event) -> str | None:

        if event.type != pygame.KEYDOWN:
            return None

        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self._move_up()

        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self._move_down()

        elif event.key == pygame.K_RETURN:
            return self._select_button()

        return None

    def _move_up(self) -> None:
        if self.focused_button_index == 0:
            return

        self.menu.buttons[
            self.focused_button_index
        ].remove_focus()

        self.focused_button_index -= 1

        self.menu.buttons[
            self.focused_button_index
        ].set_focus()

    def _move_down(self) -> None:
        if self.focused_button_index == len(self.menu.buttons) - 1:
            return

        self.menu.buttons[
            self.focused_button_index
        ].remove_focus()

        self.focused_button_index += 1

        self.menu.buttons[
            self.focused_button_index
        ].set_focus()

    def _select_button(self) -> str:
        actions = [
            "PLAY",
            "INSTRUCTIONS",
            "EXIT"
        ]
        return actions[self.focused_button_index]