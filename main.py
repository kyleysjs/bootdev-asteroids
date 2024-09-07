import pygame
from constants import *
from player import Player
from shoot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pclock = pygame.time.Clock()
    dt = 1

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    afield = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    ass_field = AsteroidField()
    myplayer = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for each in updateable:
            each.update(dt)
        for each in drawable:
            each.draw(screen)
        for each in asteroids:
            if myplayer.collisions(each):
                print("Game over!")
                sys.exit()
            for curr_shot in shots:
                if each.collisions(curr_shot):
                    curr_shot.kill()
                    each.split()
        pygame.display.flip()
        dt = pclock.tick(60) / 1000


if __name__ == "__main__":
    main()
