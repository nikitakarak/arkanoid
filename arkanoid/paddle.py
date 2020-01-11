import pygame
from arkanoid.config import DIR_RESOURCES_IMAGES


class Paddle(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()

        self.screen_rect = screen_rect

        self.image = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'paddle_01.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_left = False
        self.moving_right = False
        self.speed = 5


    def update(self):
        if self.moving_left:
            self.rect.x -= self.speed
            if self.rect.left < self.screen_rect.left:
                self.rect.left = self.screen_rect.left
        elif self.moving_right:
            self.rect.x += self.speed
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right


    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right
