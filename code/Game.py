import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 400))
        self.running: bool = True

    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         running = False