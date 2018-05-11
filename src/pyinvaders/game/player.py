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
        self.stop_watch = StopWatch()

    def update(self, delta_time):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        elif pressed_keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        elif pressed_keys[pygame.K_SPACE]:
            self._shoot()

    def _shoot(self):
        if self.missile_clock.get_time() >= constants.PLAYER_FIRE_RATE:
            PlayerMissile((self.x, self.y))
            self.missile_clock.tick()
