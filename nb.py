import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Snake and Apple
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)

# Functions
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [width / 6, height / 3])

# Game Loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1, y1 = width / 2, height / 2

    # Change in position
    x1_change, y1_change = 0, 0

    # Snake body
    snake_list = []
    length_of_snake = 3  # Change snake length from 1 to 3

    # Initial position of the apple
    apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            display.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Check if snake hits the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        display.fill(white)
        pygame.draw.rect(display, red, [apple_x, apple_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if snake collides with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        # Update the display
        pygame.display.update()

        # Check if snake eats the apple
        if x1 == apple_x and y1 == apple_y:
            apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Control the snake's speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()