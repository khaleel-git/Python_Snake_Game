import pygame
import time
import random


# Initialize pygame
pygame.init()

# Set screen size
width = 600
height = 600

# Set colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# Create screen
screen = pygame.display.set_mode((width, height))

# Set title
pygame.display.set_caption("Snake Game")

# Set snake block size
block_size = 10

# Set font for displaying score
font_style = pygame.font.SysFont(None, 50)

# your score
def Your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    screen.blit(value, [0, 0])

# Initial snake position
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/2, height/2])

def gameLoop():
    game_over = False
    game_close = False

    x1 = 300
    y1 = 300

    x1_change = 0
    y1_change = 0

    # Create clock
    clock = pygame.time.Clock()

    # Create snake
    snake_block = 10
    snake_speed = 30

    # Set food position
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(snake_block - 1)
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
                game_close = False
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

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, white, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(screen, white, [x1, y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_block += 10

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()

