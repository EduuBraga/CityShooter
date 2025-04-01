import pygame

from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (10, 10))
        self.rect = self.surf.get_rect(center=position)

    def move(self):
        self.rect.centerx += ENTITY_SPEED[self.name]
