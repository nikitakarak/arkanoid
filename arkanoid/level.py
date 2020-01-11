import pygame
from arkanoid.config import DIR_RESOURCES_LEVELS
from arkanoid.brick import Brick
from arkanoid.brick_normal import NormalBrick
from arkanoid.brick_indestructable import IndestructibleBrick


_BRICK_SIZE = (44, 22)
_BRICK_OFFSET = (1, 1)


class Level(pygame.sprite.Group):
    def __init__(self, screen_rect):
        super().__init__()
        self.screen_rect = screen_rect
        self.level_number = -1
        self.level_description = ''
        self.indestructible_brick_count = 0


    @staticmethod
    def _get_level_filename(level_number):
        return DIR_RESOURCES_LEVELS + f'{level_number:0>3}.dat'


    def _load(self, level_number):
        self.empty()

        self.level_number = level_number
        self.level_description = ''
        self.indestructible_brick_count = 0

        level_data = ()
        with open(self._get_level_filename(level_number), 'rt') as f:
            level_data = f.readlines()

        if len(level_data) >= 1:
            self.level_description = level_data[0]

            if len(level_data) >= 2:
                base_x, y = map(int, level_data[1].split(','))

                base_x += self.screen_rect.left
                y += self.screen_rect.top

                for row in range(2, len(level_data)):
                    x = base_x
                    for brick_data in level_data[row].split():
                        brick_type_id, brick_color_id = brick_data.split(':')

                        brick = None
                        if brick_type_id == '1':
                            brick = NormalBrick((x, y), brick_color_id)
                        elif brick_type_id == '2':
                            brick = IndestructibleBrick((x, y), brick_color_id)
                            self.indestructible_brick_count += 1

                        if brick:
                            if x + brick.rect.width > self.screen_rect.right:
                                break

                            self.add(brick)
                            x += brick.rect.width
                        else:
                            x += _BRICK_SIZE[0]

                        x += _BRICK_OFFSET[0]

                    y += _BRICK_SIZE[1] + _BRICK_OFFSET[1]


    def load_first(self):
        return self._load(1)


    def load_next(self):
        if self.level_number == -1:
            return self.load_first()

        return self._load(self.level_number + 1)
