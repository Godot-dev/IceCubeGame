import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Maël chut")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('assets/bg.jpg')
game = Game()

running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(game.player.image, game.player.rect)
    game.launch_projectile()
    for projectile in game.liste_projectiles:
        projectile.move()

    if game.check_collision(game.player, game.liste_projectiles):
        game.player.health -= 1
        if game.player.health == 0:
            running = False

    game.liste_projectiles.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
