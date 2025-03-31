from .Background import Background
from .Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from .Enemy import Enemy
from .Player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "level1bg":
                bg_layers = []
                # Cria 2 backgrounds para cada uma das 6 camadas
                for i in range(1, 7):
                    layer_name = f'level1bg{i}'
                    bg_layers.append(Background(layer_name, (0, 0)))
                return bg_layers
            case "player":
                return Player("player", (100, WIN_HEIGHT - 150))
            case "enemy1":
                return Enemy("enemy1", (WIN_WIDTH + 100, WIN_HEIGHT - 150))
            case "enemy2":
                return Enemy("enemy2", (WIN_WIDTH + 100, WIN_HEIGHT - 150))
