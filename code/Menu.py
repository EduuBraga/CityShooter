import pygame

from .Const import WIN_WIDTH, WIN_HEIGHT, FONT_STRONG, FONT_PIXEL, COLOR_RED, COLOR_WHITE, MENU_OPTIONS

class Menu:
    def __init__(self, window):
        self.window = window
        self.image = pygame.image.load("./assets/background-menu.png")
        self.image = pygame.transform.scale(self.image, (WIN_WIDTH, WIN_HEIGHT))  # Redimensiona a imagem
        self.rect = self.image.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer.music.load("./assets/menu_music.mp3")
        pygame.mixer.music.play(-1)

        while True:
            self.window.blit(source=self.image, dest=self.rect)
            self.menu_text(150, "Dead", COLOR_RED, ((WIN_WIDTH / 2), 100), FONT_STRONG)
            self.menu_text(150, "City", COLOR_RED, ((WIN_WIDTH / 2), 210), FONT_STRONG)

            for i in range(len(MENU_OPTIONS)):
                self.menu_text(80, MENU_OPTIONS[i], COLOR_WHITE, ((WIN_WIDTH / 2), 500 + 65 * i), FONT_PIXEL)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple, name_font: str):
        text_font = pygame.font.SysFont(name=name_font, size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)