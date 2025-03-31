import pygame
from .Entity import Entity
from .Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        # Redimensiona mantendo a proporção original (1920x1080 -> 1280x720)
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))
        self.rect = self.surf.get_rect(topleft=position)

    def move(self):
        pass
        # self.rect.x -= ENTITY_SPEED[self.name]
        #
        # # Quando o background sair completamente da tela
        # if self.rect.right <= 0:
        #     self.rect.left = WIN_WIDTH  # Reposiciona à direita