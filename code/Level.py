import pygame

from .Const import COLOR_WHITE, COLOR_RED_DARK, WIN_WIDTH, WIN_HEIGHT, FONT_PIXEL, ENTITY_SPEED
from .Entity import Entity
from .EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity("level1bg"))
        self.timeout = 20000

    def run(self):
        pygame.mixer_music.load(f'./assets/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)
            self.window.fill((0, 0, 0))  # Limpa a tela com preto

            # Renderiza em ordem de velocidade (mais lento primeiro)
            for ent in sorted(self.entity_list, key=lambda x: ENTITY_SPEED[x.name]):
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

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

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple, name_font: str,
                   border_color=None):
        text_font = pygame.font.SysFont(name=name_font, size=text_size)

        # Renderiza o texto principal
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_pos)

        # Se a borda for ativada, desenha a borda ao redor
        if border_color:
            text_surf_border = text_font.render(text, True, border_color).convert_alpha()

            # Desenha a borda em torno do texto principal
            for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-3, -3), (-3, 3), (3, -3), (3, 3)]:
                self.window.blit(text_surf_border, text_rect.move(dx, dy))

        # Desenha o texto principal no centro
        self.window.blit(text_surf, text_rect)
