import pygame

from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants
from pyinvaders.game.player_missile import PlayerMissile


class Player(GameObject):
    def __init__(self, coordinates):
        super(Player, self).__init__(coordinates)
        self.player_image = constants.PLAYER
        self.speed = constants.PLAYER_SPEED
        self.set_image_url(self.player_image)
        self.time_since_last_shot = 0.8;


    def update(self, delta_time):
        pressed_keys = pygame.key.get_pressed()
        self.time_since_last_shot += delta_time;
        if pressed_keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        elif pressed_keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        if pressed_keys[pygame.K_SPACE] and self.time_since_last_shot > 0.8:
            self._shoot()

    def _shoot(self):
        self.time_since_last_shot = 0;
        PlayerMissile((self.x + constants.PLAYER_MUZZLE_OFFSET_PX[0], self.y))
