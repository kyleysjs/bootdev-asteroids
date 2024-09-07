import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_ast1 = Asteroid(
            self.position.x, self.position.y, self.radius / random.uniform(1.8, 2.2)
        )
        new_ast2 = Asteroid(
            self.position.x, self.position.y, self.radius / random.uniform(1.8, 2.2)
        )
        new_ast1.velocity = self.velocity.rotate(angle)
        new_ast1.velocity = new_ast1.velocity * 1.2
        new_ast2.velocity = self.velocity.rotate(-angle)
        new_ast2.velocity = new_ast2.velocity * 1.2
