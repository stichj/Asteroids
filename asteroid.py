from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
        
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position
        
        left_asteroid = Asteroid(x, y, new_radius)
        left_asteroid.velocity = pygame.Vector2(self.velocity).rotate(angle) * 1.2
        right_asteroid = Asteroid(x, y, new_radius)
        right_asteroid.velocity = pygame.Vector2(self.velocity).rotate(-angle) * 1.2