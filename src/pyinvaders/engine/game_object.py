from pathlib import Path

import pygame

from pyinvaders.engine import urls
from pyinvaders.game import constants


class GameObject(object):
    game_objects = list()

    def __init__(self, coordinates=(constants.WINDOW_WIDTH / 2, constants.WINDOW_HEIGHT / 2), visible=True):
        self.visible = visible
        self.x, self.y = coordinates
        GameObject.game_objects.append(self)
        self.image = None

    def load_image(self, image_url):
        self.image = pygame.image.load(str(Path(urls.graphics_dir, image_url).resolve()))

    def update(self, delta_time):
        pass

    def destroy(self):
        GameObject.game_objects.remove(self)

    def show(self, window):
        if self.visible:
            window.blit(self.image, (self.x, self.y))
