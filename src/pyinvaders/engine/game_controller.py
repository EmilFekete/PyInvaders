import pygame
import pygame.display
import pygame.draw
import pygame.key
import pygame.time

from pyinvaders.engine.game_object import GameObject
from pyinvaders.engine.graphic_handler import GraphicHandler
from pyinvaders.game import constants
from pyinvaders.game.world_config import world_config


class GameController(object):
    def __init__(self):
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.graphic_handler = GraphicHandler(self.window)

    def run(self):
        world_config()
        while self.is_running:
            self.clock.tick(constants.FPS_CAP)
            delta_time = self.clock.get_time() / 1000.0
            self._update(delta_time)
            self._show()

    def _show(self):
        self.graphic_handler.reset()
        for game_object in GameObject.game_objects:
            if game_object.visible:
                self.graphic_handler.handle_graphic(game_object.image_url, (game_object.x, game_object.y))
        pygame.display.update()

    def _update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        for game_object in GameObject.game_objects:
            game_object.update(delta_time)
