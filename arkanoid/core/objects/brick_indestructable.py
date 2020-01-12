import pygame
from .brick import Brick


class IndestructibleBrick(Brick):
    def hit(self):
        pass

    @property
    def is_destroyed(self):
        return False
