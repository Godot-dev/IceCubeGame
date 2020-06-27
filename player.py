import pygame

pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.health = 2
        self.max_health = 2
        self.velocity = 4
        self.image = pygame.image.load('assets/ice-cream.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 360

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

