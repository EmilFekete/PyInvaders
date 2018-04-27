import os

import pygame

from pyinvaders.game import constants
from pyinvaders.engine.game_object import GameObject


class Player(GameObject):
    def __init__(self):
        self.player_image = constants.PLAYER
        super(Player, self).__init__()
        self.speed = constants.PLAYER_SPEED
        self.set_image_url(self.player_image)
