from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants


class PlayerMissile(GameObject):
    def __init__(self, coordinates):
        super(PlayerMissile, self).__init__(coordinates)
        self.missile_image = constants.PLAYER_MISSILE
        self.load_image(self.missile_image)

    def update(self, delta_time):
        self.y -= constants.MISSILE_SPEED * delta_time
        if self.y <= 0:
            self.destroy()