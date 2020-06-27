import pygame
import random
from player import Player
from projectile import Projectile


class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.liste_projectiles = pygame.sprite.Group()

    def launch_projectile(self):  # crée un projectile une fois sur 10 afin de diminuer la fréquence
        if random.randint(1, 30) == 1:
            self.liste_projectiles.add(Projectile(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, True, pygame.sprite.collide_mask)
