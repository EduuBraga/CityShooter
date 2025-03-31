import pygame

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.rect = self.surf.get_rect(center=position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH