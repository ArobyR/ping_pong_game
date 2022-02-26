import pygame

pygame.init()
pygame.font.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

my_font = pygame.font.SysFont('C059', 32)
pygame.display.set_caption('Ping Pong Game')

sound = pygame.mixer.Sound('./resources/sounds/paddle.wav')

done = False
BACKGROUND_COLOR = (0, 160, 84)
WHITE_COLOR = (255, 255, 255)

player_width = 15
player_height = 90

# Coordinate and velocity
player1_x_coord = 50
player1_y_coord = 255
player1_y_speed = 0

player2_x_coord = 850 - player_width
player2_y_coord = 300 - 45
player2_y_speed = 0

velocity = 0

# Ball coordinate
ball_x = 400
ball_y = 300
ball_speed_x = 3
ball_speed_y = 3

# counters of the players
counter_1 = 0
counter_2 = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    key = pygame.key.get_pressed()
    if key[pygame.K_w] and player1_y_coord > 0:
        player1_y_coord -= 3
    if key[pygame.K_s] and player1_y_coord < 505:
        player1_y_coord += 3
    if key[pygame.K_UP] and player2_y_coord > 0:
        player2_y_coord -= 3
    if key[pygame.K_DOWN] and player2_y_coord < 505:
        player2_y_coord += 3

    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1

    # Counters
    player1_counter = my_font.render(
        f'Player A: {counter_1}', False, WHITE_COLOR)
    player2_counter = my_font.render(
        f'Player B: {counter_2}', False, WHITE_COLOR)

    if ball_x > 900:
        counter_1 += 1
    if ball_x < 0:
        counter_2 += 1

    # Check if the ball go out of the right side
    if ball_x > SCREEN_WIDTH or ball_x < 0:
        ball_x = SCREEN_WIDTH / 2
        ball_y = SCREEN_HEIGHT / 2

        # If go out of the window, invest direction
        ball_speed_x *= -1
        ball_speed_y *= -1

    # Ball mov.
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    screen.fill(BACKGROUND_COLOR)

    screen.blit(player1_counter, (250, 5))
    screen.blit(player2_counter, (490, 5))

    player1 = pygame.draw.rect(
        screen, WHITE_COLOR, (player1_x_coord, player1_y_coord, player_width, player_height))

    player2 = pygame.draw.rect(
        screen, WHITE_COLOR, (player2_x_coord, player2_y_coord, player_width, player_height))

    ball = pygame.draw.circle(screen, WHITE_COLOR, (ball_x, ball_y), 10)

    pygame.draw.line(screen, WHITE_COLOR,
                     (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT), 3)

    # Collisions
    if ball.colliderect(player1) or ball.colliderect(player2):
        sound.play()
        ball_speed_x *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.font.quit()
pygame.quit()
