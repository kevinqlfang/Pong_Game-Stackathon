import pygame

# Define some colors
WHITE = (255, 255, 255)
PURPLE = (206, 202, 255)

# create Score class
class Score:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.left_score = 0
        self.right_score = 0

    def draw(self, screen):
        font = pygame.font.Font(None, 30)
        left_score_text = font.render("Left: " + str(self.left_score), 1, (255, 255, 255))
        right_score_text = font.render("Right: " + str(self.right_score), 1, (255, 255, 255))
        screen.blit(left_score_text, (self.x, self.y))
        screen.blit(right_score_text, (self.x + 100, self.y))

    def add_point(self, side):
        if side == "left":
            self.left_score += 1
        elif side == "right":
            self.right_score += 1