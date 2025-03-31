import pygame

WIN_WIDTH = 1280
WIN_HEIGHT = 720

FONT_STRONG = "Sigmar One Regular"
FONT_PIXEL = "Jersey 15 Regular"

COLOR_RED = (247, 55, 79)
COLOR_WHITE = (244, 244, 244)
COLOR_RED_DARK = (82, 37, 70)

MENU_OPTIONS = ["NEW GAME", "SCORE", "EXIT"]

ENTITY_SPEED = {
    'player': 3,
    'enemy1': 5,
    'enemy2': 2
}

EVENT_ENEMY = pygame.USEREVENT + 1
SPAWN_TIME = 3000
