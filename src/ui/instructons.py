import pygame


class Instructions:
    def __init__(self, screen, width, height) -> None:
        self.screen = screen
        self.width = width
        self.height = height
        self.img = pygame.image.load('assets/images/Instructions.png')

    def render(self):
        bg = pygame.transform.scale(self.img, (self.width, self.height))
        self.screen.blit(bg, (0, 0))

    # def treat_input(self, key):
        # if key == pygame.K_RETURN:
            # return 