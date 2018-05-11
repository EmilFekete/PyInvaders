from enum import Enum, unique

from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants


def get_images_of_enemy_type(enemy_type):
    if enemy_type == EnemyType.SMALL:
        return constants.ENEMY_SMALL
    elif enemy_type == EnemyType.MEDIUM:
        return constants.ENEMY_MEDIUM
    elif enemy_type == EnemyType.LARGE:
        return constants.ENEMY_LARGE
    elif enemy_type == EnemyType.SPECIAL:
        return constants.ENEMY_SPECIAL
    else:
        return constants.ENEMY_SMALL


@unique
class EnemyType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    SPECIAL = 4


class Enemy(GameObject):
    def __init__(self, enemy_type=EnemyType.SMALL):
        super(Enemy, self).__init__()
        self.enemy_type = enemy_type
        self.sprite = get_images_of_enemy_type(self.enemy_type)
        self.set_image_url(self.sprite)
