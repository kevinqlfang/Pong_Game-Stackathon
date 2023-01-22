import pygame

# Define some colors
WHITE = (255, 255, 255)
PURPLE = (206, 202, 255)

# create Ball class
class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)

    def bounce(self):
        if self.y <= 0 or self.y >= 600:
            self.speed_y *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.radius)
        
    def reset(self):
        self.x = 640
        self.y = 360
        self.speed_x *= -1
        self.speed_y *= -1