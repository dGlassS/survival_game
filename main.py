import pygame
import math
from game import Game
pygame.init()

pygame.display.set_caption("hero vs zombies")
screen = pygame.display.set_mode((1000, 720))

background = pygame.image.load('assets/bg.jpg')

# interface
# banner survival
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# button play
play_button = pygame.image.load('assets/button_play.png')
play_button = pygame.transform.scale(play_button, (150, 70))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 4)
play_button_rect.y = math.ceil(screen.get_height() / 11+450)

# button quit
quit_button = pygame.image.load('assets/button_quit.png')
quit_button = pygame.transform.scale(quit_button, (150, 70))
quit_button_rect = quit_button.get_rect()
quit_button_rect.x = math.ceil(screen.get_width() / 5+400)
quit_button_rect.y = math.ceil(screen.get_height() / 11+450)

# instruction de touche
instruction = pygame.image.load('assets/instruction.png')
instruction = pygame.transform.scale(instruction, (200, 120))
instruction_rect = quit_button.get_rect()
instruction_rect.x = 20
instruction_rect.y = 250

game = Game()

running = True
while running:
    screen.blit(background, (-200, -400))
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(quit_button, quit_button_rect)
        screen.blit(instruction, instruction_rect)
        screen.blit(banner, banner_rect)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Aucun problème !')
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_x:
                game.hero.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button_rect.collidepoint(event.pos):
                    running = False
                    pygame.quit()
                    print('Aucun problème !')