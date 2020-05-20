import pygame
from projectile import Projectile

class Hero(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 7
        self.image = pygame.image.load('assets/hero.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 470
        self.all_projectiles = pygame.sprite.Group()

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_health_bar_hero(self, surface):
        bar_position = [self.rect.x - 1, self.rect.y - 17, self.health, 5]
        back_bar_position = [self.rect.x - 1, self.rect.y - 17, self.max_health, 5]
        pygame.draw.rect(surface, (30, 30, 30), back_bar_position)
        pygame.draw.rect(surface, (39, 169, 7), bar_position)

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_zombies):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity