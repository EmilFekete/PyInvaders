from pathlib import Path

from pyinvaders.engine import urls
from pyinvaders.game import constants


class GameObject(object):
    game_objects = list()

    def __init__(self, visible=True, x=constants.WINDOW_WIDTH / 2, y=constants.WINDOW_HEIGHT / 2):
        self.image_url = None
        self.visible = visible
        self.x = x
        self.y = y
        GameObject.game_objects.append(self)
        self.image = None

    def set_image_url(self, image_url):
        self.image_url = str(Path(urls.graphics_dir, image_url).resolve())
