import pygame
from player import Player
from projectile import Projectile


class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.liste_projectiles = pygame.sprite.Group()

    def launch_projectile(self):
        self.liste_projectiles.add(Projectile())
