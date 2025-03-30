from .Background import Background
from .Const import WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case "level1bg":
                bg_list = []
                for i in range(6):
                    bg_list.append(Background(f'level1bg{i + 1}', (0, 0)))
                    bg_list.append(Background(f'level1bg{i + 1}', (WIN_WIDTH, 0)))
                return bg_list

