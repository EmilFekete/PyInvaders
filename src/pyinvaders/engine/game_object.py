from pathlib import Path

from pyinvaders.engine import urls
from pyinvaders.game import constants


class GameObject(object):
    game_objects = list()

    def __init__(self, coordinates=(constants.WINDOW_WIDTH / 2, constants.WINDOW_HEIGHT / 2), visible=True):
        self.image_url = None
        self.visible = visible
        self.x, self.y = coordinates
        GameObject.game_objects.append(self)
        self.image = None

    def set_image_url(self, image_url):
        self.image_url = str(Path(urls.graphics_dir, image_url).resolve())

    def update(self):
        pass
