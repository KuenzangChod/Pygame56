import pygame
import random

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the window
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avoid the blocks")

# Set up the player
player_width = 50
player_height = 50
player_x = 375
player_y = 525
player_speed = 0

# Set up the obstacles
obstacle_list = []
for i in range(10):
    obstacle_x = random.randrange(0, 750)
    obstacle_y = random.randrange(0, 500)
    obstacle_width = 50
    obstacle_height = 50
    obstacle_list.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])

# Set up the font
font = pygame.font.SysFont('Calibri', 25, True, False)

# Set up the score
score = 0

# Set up the game loop
done = False
clock = pygame.time.Clock()

while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed = -5
            elif event.key == pygame.K_RIGHT:
                player_speed = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_speed = 0

    # Update the player's position
    player_x += player_speed

    # Check for collisions with the obstacles
    for obstacle in obstacle_list:
        if player_x + player_width > obstacle[0] and player_x < obstacle[0] + obstacle[2] and player_y + player_height > obstacle[1] and player_y < obstacle[1] + obstacle[3]:
            player_x = 375
            player_y = 525
            score = 0
            obstacle_list.clear()
            for i in range(10):
                obstacle_x = random.randrange(0, 750)
                obstacle_y = random.randrange(0, 500)
                obstacle_width = 50
                obstacle_height = 50
                obstacle_list.append([obstacle_x, obstacle_y, obstacle_width, obstacle_height])

    # Update the obstacles' position
    for obstacle in obstacle_list:
        obstacle[1] += 5
        if obstacle[1] > 600:
            obstacle[0] = random.randrange(0, 750)
            obstacle[1] = random.randrange(-500, 0)

    # Update the score
    score += 1

    # Draw on the screen
    screen.fill(BLACK)

    for obstacle in obstacle_list:
        pygame.draw.rect(screen, WHITE, [obstacle[0], obstacle[1], obstacle[2], obstacle[3]])

    pygame.draw.rect(screen, WHITE, [player_x, player_y, player_width, player_height])

    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])

    pygame.display.flip()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()