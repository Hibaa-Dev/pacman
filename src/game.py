from src.utils.global_data import VIRTUAL_H, VIRTUAL_W,  GameState
from src.utils import global_data
from src.ui.instructons import Instructions
from src.ui.menu import Main_menu
import pygame


class Game:
    def __init__(self):
        pygame.init()

        info = pygame.display.Info()
        self.current_w, self.current_h = (
            info.current_w, info.current_h
        )
        self.screen = pygame.display.set_mode((self.current_w, self.current_h), pygame.RESIZABLE)
        self.canvas = pygame.Surface((VIRTUAL_W, VIRTUAL_H))

        self.running = True
        self.main_menu = Main_menu(self.canvas)
        self.instructions = Instructions(self.canvas)

    def get_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            # ADDED — without this, self.current_w/current_h stay frozen at
            # launch-time values forever, so dragging the window to resize
            # it would make the letterbox math below stale/wrong.
            if event.type == pygame.VIDEORESIZE:
                self.current_w, self.current_h = event.w, event.h
            if event.type == pygame.KEYDOWN:
                if global_data.GAME_STATE == GameState.MENU:
                    action = self.main_menu.treat_input(event.key)
                    if action:
                        action.command()
                if global_data.GAME_STATE == GameState.INSTRUCTIONS:
                    self.instructions.treat_input(event.key)

    def render(self):
        self.canvas.fill((0, 0, 0))
        if global_data.GAME_STATE == GameState.MENU:
            self.main_menu.render()

        if global_data.GAME_STATE == GameState.INSTRUCTIONS:
            self.instructions.render()

        # CHANGED — was a non-uniform stretch to (current_w, current_h),
        # which distorts the aspect ratio on any window that isn't
        # exactly VIRTUAL_W:VIRTUAL_H. This now scales the canvas as one
        # rigid block, preserving its aspect ratio, and centers it with
        # black bars filling any leftover space (letterboxing).
        scale = min(self.current_w / VIRTUAL_W, self.current_h / VIRTUAL_H)
        scaled_w, scaled_h = int(VIRTUAL_W * scale), int(VIRTUAL_H * scale)
        self.scaled_canvas = pygame.transform.smoothscale(
            self.canvas, (scaled_w, scaled_h)
        )

        offset_x = (self.current_w - scaled_w) // 2
        offset_y = (self.current_h - scaled_h) // 2

        self.screen.fill((0, 0, 0))  # ADDED — paints the letterbox bars
        self.screen.blit(self.scaled_canvas, (offset_x, offset_y))

    def run(self):
        while self.running:
            self.get_input()
            self.render()

            pygame.display.flip()
        pygame.quit()