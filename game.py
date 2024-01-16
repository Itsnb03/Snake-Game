import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zombie Shooter")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size - 10
player_speed = 5

# Bullet
bullet_size = 10
bullet_speed = 10
bullets = []

# Zombie
zombie_size = 50
zombie_speed = 3
zombies = []

# Clock
clock = pygame.time.Clock()

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Functions
def draw_player(x, y):
    pygame.draw.rect(display, white, [x, y, player_size, player_size])

def draw_bullet(x, y):
    pygame.draw.rect(display, white, [x, y, bullet_size, bullet_size])

def draw_zombie(x, y):
    pygame.draw.rect(display, red, [x, y, zombie_size, zombie_size])

def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    display.blit(score_text, [10, 10])

# Game Loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append([player_x + player_size // 2 - bullet_size // 2, player_y])

    # Move bullets
    bullets = [[x, y - bullet_speed] for x, y in bullets if y > 0]

    # Spawn zombies
    if random.randrange(0, 100) < 2:
        zombie_x = random.randrange(0, width - zombie_size)
        zombie_y = -zombie_size
        zombies.append([zombie_x, zombie_y])

    # Move zombies
    zombies = [[x, y + zombie_speed] for x, y in zombies if y < height]

    # Check for collision with zombies
    for bullet in bullets:
        for zombie in zombies:
            if (
                zombie[0] < bullet[0] < zombie[0] + zombie_size
                and zombie[1] < bullet[1] < zombie[1] + zombie_size
            ):
                zombies.remove(zombie)
                bullets.remove(bullet)
                score += 10

    # Check for collision with player
    for zombie in zombies:
        if (
            player_x < zombie[0] < player_x + player_size
            and player_y < zombie[1] < player_y + player_size
        ):
            game_over = True

    # Draw everything
    display.fill(black)
    draw_player(player_x, player_y)
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])
    for zombie in zombies:
        draw_zombie(zombie[0], zombie[1])
    show_score(score)

    # Update the display
    pygame.display.update()

    # Control the frame rate
    clock.tick(30)

# Quit the game
pygame.quit()
sys.exit()