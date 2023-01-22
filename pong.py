import pygame, sys
from paddle import Paddle
from ball import Ball
from collision import Collision
from score import Score


# define some colors / width and height
PURPLE = (206, 202, 255)
WHITE = (255, 255, 255)
WIDTH = 1280
HEIGHT = 720

# initialize pygame
pygame.init()
# pygame.font.init()

# set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# create the paddles
left_paddle = Paddle(50, 200, 20, 100, HEIGHT)
right_paddle = Paddle(1210, 200, 20, 100, HEIGHT)

# create the ball
ball = Ball(400, 300, 10, 5, 5)

# create the collision detector
collision = Collision()

# create the score
score = Score(WIDTH // 2 - 80, 20)

# loop until the user clicks the close button.
clock = pygame.time.Clock()

# variables
done = False
win_score = 1
win_message = None
wim_message_rect = None

# main loop
while True:
    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if close button is pressed
            done = True # flag that we are done so we exit this loop
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        right_paddle.move("up")
    if keys[pygame.K_DOWN]:
        right_paddle.move("down")
    if keys[pygame.K_w]:
        left_paddle.move("up")
    if keys[pygame.K_s]:
        left_paddle.move("down")

    # Game logic
    if not done:
        # background color
        screen.fill(PURPLE)

        # draw objects
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)
        score.draw(screen)

        # collision detection
        collision.check_paddle_collision(ball, left_paddle)
        collision.check_paddle_collision(ball, right_paddle)
        ball.move()
        collision.check_wall_collision(ball, score, win_score)

        # # check for collision with left or right wall
        if ball.x - ball.radius <= 0:
            score.add_point("right")
            if score.right_score >= win_score:
                win_message = font.render("Right player wins!", 1, (255, 255, 255))
                win_message_rect = win_message.get_rect()
                win_message_rect.center = (WIDTH // 2, HEIGHT // 2)
                screen.blit(win_message, win_message_rect)
                pygame.display.update()
                done = True
            else:
                score.draw(screen)
                ball.reset()

        elif ball.x + ball.radius >= 1280:
            score.add_point("left")
            if score.left_score >= win_score:
                win_message = font.render("Left player wins!", 1, (255, 255, 255))
                win_message_rect = win_message.get_rect()
                win_message_rect.center = (WIDTH // 2, HEIGHT // 2)
                screen.blit(win_message, win_message_rect)
                pygame.display.update()
                done = True
            else:
                score.draw(screen)
                ball.reset()

        # update the screen
        # pygame.display.flip()
        pygame.display.update()

        # limit to 60 frames per second
        clock.tick(60)
        
# quit
pygame.quit()
