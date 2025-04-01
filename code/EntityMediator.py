from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.PlayerShot import PlayerShot


class EntityMediator:
    @staticmethod
    def __verify_collission_window(ent):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.right >= WIN_WIDTH:
                ent.health = 0


    @staticmethod
    def verify_collision(entity_list):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]

            EntityMediator.__verify_collission_window(test_entity)

    @staticmethod
    def verify_health(entity_list):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)