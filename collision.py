import pygame, sys
from score import Score

# Define some colors
WHITE = (255, 255, 255)
PURPLE = (206, 202, 255)

# create Collision class
class Collision:
    def check_paddle_collision(self, ball, paddle):
        if pygame.Rect.colliderect(ball.rect, paddle.rect):
            ball.speed_x *= -1
            
            # Check if ball is sticking to paddle
            if abs(ball.x - (paddle.x + paddle.width/2)) < ball.radius:
                ball.speed_x = 0
                ball.speed_y = 0
                ball.x = paddle.x + paddle.width/2
                ball.y = paddle.y + paddle.height/2

    def check_wall_collision(self, ball, score, win_score):
        # if ball.y - ball.radius <= 0 or ball.y + ball.radius >= 720:
        #     ball.speed_y *= -1
        # if ball.x - ball.radius <= 0 or ball.x + ball.radius >= 1280:
        #     ball.reset()
        if ball.y - ball.radius <= 0 or ball.y + ball.radius >= 720:
            ball.speed_y *= -1
        if ball.x - ball.radius <= 0:
            score.add_point("right")
            if score.right_score >= win_score:
                print("Right player wins!")
                pygame.quit()
                sys.exit()
            ball.reset()
        elif ball.x + ball.radius >= 1280:
            score.add_point("left")
            if score.left_score >= win_score:
                print("Left player wins!")
                pygame.quit()
                sys.exit()
            ball.reset()