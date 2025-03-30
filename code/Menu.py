import pygame

from .Const import WIN_WIDTH, WIN_HEIGHT, FONT_STRONG, FONT_PIXEL, COLOR_RED, COLOR_WHITE, MENU_OPTIONS, COLOR_RED_DARK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/background-menu.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (WIN_WIDTH, WIN_HEIGHT))  # Redimensiona a imagem
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        # Inserindo musica ao menu
        pygame.mixer.music.load("./assets/menu_music.mp3")
        pygame.mixer.music.play(-1)

        # Carregando conteúdo do menu
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            # Inserindo logo do jogo
            self.menu_text(150, "Dead", COLOR_RED, ((WIN_WIDTH / 2), 100), FONT_STRONG)
            self.menu_text(150, "City", COLOR_RED, ((WIN_WIDTH / 2), 210), FONT_STRONG)

            # Carregando opções do menu
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(80, MENU_OPTIONS[i], COLOR_RED_DARK, ((WIN_WIDTH / 2), 500 + 65 * i), FONT_PIXEL,
                                   COLOR_RED)
                else:
                    self.menu_text(80, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 500 + 65 * i), FONT_PIXEL)

            # Atualizando tela
            pygame.display.flip()

            # Verificando eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # Tecla para baixo
                        if menu_option + 1 == len(MENU_OPTIONS):
                            menu_option = 0
                        else:
                            menu_option += 1
                    if event.key == pygame.K_UP: # Tecla para cima
                        if menu_option - 1 < 0:
                            menu_option = 2
                        else:
                            menu_option -= 1
                    if event.key == pygame.K_RETURN: # Tecla enter
                        return MENU_OPTIONS[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, name_font: str,
                  border_color=None):
        text_font = pygame.font.SysFont(name=name_font, size=text_size)

        # Renderiza o texto principal
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)

        # Se a borda for ativada, desenha a borda ao redor
        if border_color:
            text_surf_border = text_font.render(text, True, border_color).convert_alpha()

            # Desenha a borda em torno do texto principal
            for dx, dy in [(-3, 0), (3, 0), (0, -3), (0, 3), (-3, -3), (-3, 3), (3, -3), (3, 3)]:
                self.window.blit(text_surf_border, text_rect.move(dx, dy))

        # Desenha o texto principal no centro
        self.window.blit(text_surf, text_rect)
