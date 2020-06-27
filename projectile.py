import random
import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, game):
        super(Projectile, self).__init__()
        self.game = game
        self.velocity = random.randint(2, 4)
        self.direction = random.randint(0, 3)
        self.angle = 90 * self.direction
        self.image = pygame.image.load("assets/bowling-ball.png")
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect_init()

    def rect_init(self):
        if self.direction == 0:  # va en haut
            self.rect.y = 720
            self.rect.x = random.randint(0, 1080)
        elif self.direction == 1:  # va à gauche
            self.rect.x = 1080
            self.rect.y = random.randint(0, 720 - self.rect.height)
        elif self.direction == 2:  # va en bas
            self.rect.y = - self.rect.y
            self.rect.x = random.randint(0, 1080)
        elif self.direction == 3:  # va à droite
            self.rect.x = - self.rect.width
            self.rect.y = random.randint(0, 720 - self.rect.height)

    def move(self):
        if self.direction == 0:
            self.rect.y -= self.velocity
        elif self.direction == 1:
            self.rect.x -= self.velocity
        elif self.direction == 2:
            self.rect.y += self.velocity
        elif self.direction == 3:
            self.rect.x += self.velocity

        # On supprime le projectile s'il n'est plus sur la fenêtre

        if self.rect.x < - self.rect.width or self.rect.x > 1080 + self.rect.width or self.rect.y < 0 - self.rect.y or self.rect.y > 720 + self.rect.y:
            self.game.liste_projectiles.remove(self)
