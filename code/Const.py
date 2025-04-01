import pygame

WIN_WIDTH = 1280
WIN_HEIGHT = 720

FONT_STRONG = "Sigmar One Regular"
FONT_PIXEL = "Jersey 15 Regular"

COLOR_RED = (247, 55, 79)
COLOR_WHITE = (244, 244, 244)
COLOR_RED_DARK = (82, 37, 70)
COLOR_YELLOW = (255, 235, 0)

MENU_OPTIONS = ["NEW GAME", "SCORE", "EXIT"]

PLAYER_SHOT_DELAY = 15

ENTITY_SPEED = {
    'player': 3,
    'enemy1': 5,
    'enemy2': 3,
    'playerShoot': 5
}

ENTITY_HEALTH = {
    'level1bg1': 999,
    'level1bg2': 999,
    'level1bg3': 999,
    'level1bg4': 999,
    'level1bg5': 999,
    'level1bg6': 999,
    'player': 300,
    'enemy1': 80,
    'enemy2': 100,
    'playerShoot': 1
}

ENTITY_DAMAGE = {
    'level1bg1': 0,
    'level1bg2': 0,
    'level1bg3': 0,
    'level1bg4': 0,
    'level1bg5': 0,
    'level1bg6': 0,
    'player': 1,
    'enemy1': 20,
    'enemy2': 20,
    'playerShoot': 30
}

EVENT_ENEMY = pygame.USEREVENT + 1
SPAWN_TIME = 3000
