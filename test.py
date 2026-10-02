import pygame

pygame.init()
screen = pygame.display.set_mode((2800, 3000))
bg_image = pygame.image.load("assets/images/Instructions.png").convert()
bg_height = bg_image.get_height()

# Two positions: one at the bottom, one above it
bg_y1 = 0
bg_y2 = bg_height
scroll_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update positions
    bg_y1 -= scroll_speed
    bg_y2 -= scroll_speed

    # Reset when images move off bottom
    if bg_y1 <= -screen.get_height():
        bg_y1 = bg_height
    if bg_y2 <= -screen.get_height():
        bg_y2 = bg_height

    # Draw
    screen.fill((0, 0, 0))
    screen.blit(bg_image, (0, bg_y1))
    screen.blit(bg_image, (0, bg_y2))
    pygame.display.flip()

pygame.quit()
