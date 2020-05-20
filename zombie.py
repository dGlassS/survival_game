import pygame
import random

class Zombie(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 70
        self.max_health = 70
        self.attack = 0.2
        self.velocity = 2
        self.image = pygame.image.load('assets/monster_1.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = 900 + random.randint(0, 300)
        self.rect.y = 470
        self.velocity = random.randint(1, 2)

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        bar_position = [self.rect.x - 1, self.rect.y - 17, self.health, 5]
        back_bar_position = [self.rect.x - 1, self.rect.y - 17, self.max_health, 5]
        pygame.draw.rect(surface, (30, 30, 30), back_bar_position)
        pygame.draw.rect(surface, (211, 13, 13), bar_position)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            self.game.hero.damage(self.attack)