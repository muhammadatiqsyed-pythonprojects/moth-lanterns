import pygame

import settings


class LANTERNS:
    def __init__(self):
        # TOP LANTERN
        self.top_rect = pygame.FRect(
            0, 0, settings.TOP_LANTERN_WIDTH, settings.TOP_LANTERN_HEIGHT
        )
        self.rect.center = (settings.TOP_LANTERN_START_X, settings.TOP_LANTERN_START_Y)
        # BOTTOM LENTERN
        self.top_rect = pygame.FRect(
            0, 0, settings.BOTTOM_LANTERN_WIDTH, settings.BOTTOM_LANTERN_HEIGHT
        )
        self.rect.center = (
            settings.BOTTOM_LANTERN_START_X,
            settings.BOTTOM_LANTERN_START_Y,
        )

    def update(self):
        pass

    def draw(self):
        pass
