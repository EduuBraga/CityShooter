import random

import pygame

from .Const import COLOR_WHITE, WIN_HEIGHT, FONT_PIXEL, EVENT_ENEMY, SPAWN_TIME
from .Entity import Entity
from .EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.timeout = 20000
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("level1bg"))
        self.entity_list.append(EntityFactory.get_entity("player"))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela com preto

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('enemy1', 'enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

            self.level_text(
                28,
                f'{self.name} - Timeout: {self.timeout / 1000:.1f}s',
                COLOR_WHITE,
                (120, 25),
                FONT_PIXEL
            )
            self.level_text(
                28,
                f'FPS: {clock.get_fps():.0f}',
                COLOR_WHITE,
                (50, WIN_HEIGHT - 25),
                FONT_PIXEL
            )

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, name_font: str):
        text_font = pygame.font.SysFont(name=name_font, size=text_size)

        # Renderiza o texto principal
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)

        # Desenha o texto principal no centro
        self.window.blit(text_surf, text_rect)
