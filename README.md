# Python_Snake_Game
Library needed: pip install pygame

# Some basic functions:

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

# Initial snake position!
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/2, height/2])


![Game_python](https://user-images.githubusercontent.com/48614035/215202490-425a2e94-23a2-4fa6-a8a5-de1ec58f6084.PNG)
