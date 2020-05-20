import pygame
from hero import Hero
from zombie import Zombie


class Game:
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.hero = Hero(self)
        self.all_players.add(self.hero)
        self.all_zombies = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_zombie()
        self.spawn_zombie()
        self.spawn_zombie()

    def game_over(self):
        self.all_zombies = pygame.sprite.Group()
        self.hero.health = self.hero.max_health
        self.is_playing = False

    def update(self, screen):
        screen.blit(self.hero.image, self.hero.rect)
        self.hero.update_health_bar_hero(screen)

        for projectile in self.hero.all_projectiles:
            projectile.move()
        for zombie in self.all_zombies:
            zombie.forward()
            zombie.update_health_bar(screen)

        self.hero.all_projectiles.draw(screen)
        self.all_zombies.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.hero.rect.x < 900:
            self.hero.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.hero.rect.x > 5:
            self.hero.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_zombie(self):
        zombie = Zombie(self)
        self.all_zombies.add(zombie)