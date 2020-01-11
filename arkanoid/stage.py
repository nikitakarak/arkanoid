import pygame
from collections import defaultdict, namedtuple


NextStage = namedtuple('NextStage', ('name', 'params'))


# TODO Не должны создаваться экземпляры класса.
class Stage:
    '''
    Базовый класс этапа игры
    
    Класс содержит только общий набор методов и реализацию метода для получения событий мыши и клавиатуры.
    '''
    def __init__(self):
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []


    def show(self, params=None):
        pass


    def hide(self):
        pass


    # Возвращает None или объект типа NextStage.
    def update(self):
        pass


    def draw(self, surface):
        pass


    # TODO Метод не должен перекрыватся в наследниках.
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            for handler in self.keydown_handlers[event.key]:
                handler(event.key)
        elif event.type == pygame.KEYUP:
            for handler in self.keyup_handlers[event.key]:
                handler(event.key)
        elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            for handler in self.mouse_handlers:
                handler(event.type, event.pos)
