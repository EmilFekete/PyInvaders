from enum import Enum, unique

from pyinvaders.engine.game_object import GameObject


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
