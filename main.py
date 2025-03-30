import pygame

pygame.init()
window = pygame.display.set_mode((600, 400))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
