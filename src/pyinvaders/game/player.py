import pygame

from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants


class Player(GameObject):
    def __init__(self, coordinates):
        super(Player, self).__init__(coordinates)
        self.player_image = constants.PLAYER
        self.speed = constants.PLAYER_SPEED
        self.set_image_url(self.player_image)

    def update(self, delta_time):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        elif pressed_keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
