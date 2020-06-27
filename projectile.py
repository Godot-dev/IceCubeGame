import random
import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super(Projectile, self).__init__()
        self.velocity = 5
        self.image = pygame.image.load("bowling-ball.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.direction = random.randint(1, 4)
        self.rect_init(self)

    def rect_init(self):
        if self.direction == 1:  # va en haut
            self.rect.y = 720
            self.rect.x = random.randint(0, 1080)
        elif self.direction == 2:  # va à droite
            self.rect.x = - self.rect.width
            self.rect.y = random.randint(0, 720 - self.rect.height)
        elif self.direction == 3:  # va en bas
            self.rect.y = - self.rect.y
            self.rect.x = random.randint(0, 1080)
        elif self.direction == 4:  # va à gauche
            self.rect.x = 1080
            self.rect.y = random.randint(0, 720 - self.rect.height)

    def move(self):
        if self.direction == 1:
            self.rect.y -= self.velocity
        elif self.direction == 2:
            self.rect.x += self.velocity
        elif self.direction == 3:
            self.rect.y += self.velocity
        elif self.direction == 4:
            self.rect.x -= self.velocity
