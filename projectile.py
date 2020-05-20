import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, hero):
        super().__init__()
        self.hero = hero
        self.velocity = 8
        self.player = hero
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = hero.rect.x + 57
        self.rect.y = hero.rect.y + -3

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        if self.rect.x > 1000:
            self.remove()

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies):
            self.remove()
            zombie.damage(self.hero.attack)