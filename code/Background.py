import pygame

from .Entity import Entity
from .Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass