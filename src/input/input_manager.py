import pygame


class Input_manager:
    def __init__(self, running: bool) -> None:
        self.running = running 

    def get_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('test')
                self.running = False
            elif event == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
