from .Background import Background
from .Const import WIN_WIDTH, ENTITY_SPEED

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
                    bg_layers.append(Background(layer_name, (WIN_WIDTH, 0)))
                return bg_layers