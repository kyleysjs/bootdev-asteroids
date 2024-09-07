import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes will override
        pass

    def update(self, dt):
        # sub-classes will override
        pass

    def collisions(self, circle_shape_obj):
        distance = self.position.distance_to(circle_shape_obj.position)
        if distance <= (self.radius + circle_shape_obj.radius):
            return True
        return False
