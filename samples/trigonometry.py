'''
Описание расчёта угла отскока шарика с помощью тригонометрических функций
http://thepythongamebook.com/en:pygame:step017
'''


import pygame
import random
import math


def write(surface, position, color, message):
    myfont = pygame.font.SysFont("None", 25)
    mytext = myfont.render(message, True, color)
    mytext = mytext.convert_alpha()
    screen.blit(mytext, position)


def get_position(position, direction, speed):
    direction_radians = math.radians(direction)
    return [
        position[0] + speed * math.cos(direction_radians),
        position[1] + speed * math.sin(direction_radians)
    ]


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Тест отскока шарика от стенок')
    screen = pygame.display.set_mode((800, 600))
    area = screen.get_rect()

    ball_direction = 90
    ball_speed = 200
    ball_radius = 15
    ball_center = area.center

    clock = pygame.time.Clock()

    running = True
    while running:
        time = clock.tick() / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ball_center = get_position(ball_center, ball_direction, ball_speed * time)

        if (ball_center[1] - ball_radius) <= area.top:
            ball_center[1] = area.top + ball_radius + 1
            ball_direction = (360 - ball_direction + random.randint(-2, +2)) % 360

        if (ball_center[1] + ball_radius) >= area.bottom:
            ball_center[1] = area.bottom - ball_radius - 1
            ball_direction = (360 - ball_direction + random.randint(-10, +10)) % 360

        if (ball_center[0] - ball_radius) <= area.left:
            ball_center[0] = area.left + ball_radius + 1
            ball_direction = (180 - ball_direction + random.randint(-2, +2)) % 360

        if (ball_center[0] + ball_radius) >= area.right:
            ball_center[0] = area.right - ball_radius - 1
            ball_direction = (180 - ball_direction + random.randint(-2, +2)) % 360

        screen.fill(pygame.Color('white'))
        pygame.draw.circle(screen, pygame.Color('red'), (int(ball_center[0]), int(ball_center[1])), ball_radius)
        write(screen, (0, 0), pygame.Color('gray'), f'Направление [{ball_direction}°]')
        pygame.display.update()

    pygame.quit()
