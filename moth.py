import pygame

import settings


class Moth:
    def __init__(self):
        self.rect = pygame.FRect(0, 0, settings.MOTH_WIDTH, settings.MOTH_HEIGHT)
        self.rect.center = (settings.MOTH_START_X, settings.MOTH_START_Y)

    def update(self):
        pass

    def draw(self):
        pass
