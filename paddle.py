import pygame

# Define some colors
WHITE = (255, 255, 255)
PURPLE = (206, 202, 255)

# create Paddle class
class Paddle:
    def __init__(self, x, y, width, height, screen_height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 5
        self.screen_height = screen_height

    def move(self, direction):
        if direction == "up":
            if self.y - self.speed >= 0: # check if paddle is going out of bounds
                self.y -= self.speed
        elif direction == "down":
            if self.y + self.height + self.speed <= self.screen_height: # check if paddle is going out of bounds
                self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)