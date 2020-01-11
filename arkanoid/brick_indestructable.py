import pygame
from arkanoid.brick import Brick


class IndestructibleBrick(Brick):
    def hit(self):
        pass

    @property
    def is_destroyed(self):
        return False
