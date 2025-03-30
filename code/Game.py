import pygame

from .Menu import Menu
from .Level import Level

from .Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.running: bool = True

    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                level = Level(self.window, "Level1")
                level_return = level.run()
            elif menu_return == MENU_OPTIONS[2]:
                pygame.quit()
                quit()
            else:
                pass