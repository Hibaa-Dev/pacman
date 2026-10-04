import pygame

pygame.init()
screen = pygame.display.set_mode((400, 200))
clock = pygame.time.Clock()

# Progress bar settings
bar_rect = pygame.Rect(50, 80, 300, 40)
frame_color = (100, 100, 100)
bar_color = (0, 255, 0)

progress = 0.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Simulate loading
    progress += 0.01
    if progress > 1.0:
        progress = 1.0

    # Calculate current width based on progress
    current_width = int(bar_rect.width * progress)
    
    # Draw frame (outer rectangle)
    pygame.draw.rect(screen, frame_color, bar_rect)
    
    # Draw progress (inner rectangle, clipped to frame)
    # Use clip argument to ensure it doesn't overflow the border
    pygame.draw.rect(screen, bar_color, bar_rect.clip(50, 80, current_width, 40))
    
    pygame.display.flip()
    clock.tick(60)