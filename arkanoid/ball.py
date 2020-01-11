import pygame
import math, random
from arkanoid.config import DIR_RESOURCES_IMAGES


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()

        self.speed = 5.0

        self.image = pygame.image.load(
            DIR_RESOURCES_IMAGES + r'ball_01.png').convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
 
        self.screen_rect = screen_rect

        # Начальное положение шарика.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        # Направление движения шарика в градусах.
        self.direction = 0


    @property
    def is_dead(self):
        return self.rect.top >= self.screen_rect.bottom


    def bounce_horizontal(self, offset=0):
        if self.is_dead:
            return

        self.direction = (180 - self.direction) % 360
        self.direction -= offset


    def bounce_vertical(self):
        if self.is_dead:
            return

        self.direction = (360 - self.direction) % 360


    def update(self):
        if self.is_dead:
            return

        direction_radians = math.radians(self.direction)
        self.rect.x += self.speed * math.sin(direction_radians)
        self.rect.y -= self.speed * math.cos(direction_radians)

        # Do we bounce off the top of the screen?
        if self.rect.y <= self.screen_rect.top:
            self.rect.y = self.screen_rect.top
            self.bounce_horizontal()

        # Do we bounce off the left of the screen?
        if self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left
            self.bounce_vertical()

        # Do we bounce of the right side of the screen?
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.bounce_vertical()
