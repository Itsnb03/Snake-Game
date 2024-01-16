import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Block Game")

# Initialize block
block = pygame.Rect(WIDTH // 2 - BLOCK_SIZE // 2, HEIGHT - BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Move the block
    if keys[pygame.K_LEFT] and block.left > 0:
        block.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and block.right < WIDTH:
        block.move_ip(5, 0)

    # Draw background
    screen.fill(WHITE)

    # Draw the block
    pygame.draw.rect(screen, RED, block)

    # Update the display
    pygame.display.flip()
