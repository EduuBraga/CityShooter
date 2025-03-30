import pygame

from .Menu import Menu

from .Const import WIN_WIDTH, WIN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.running: bool = True

    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu.run()
            pass