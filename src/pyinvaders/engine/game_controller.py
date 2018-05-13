import pygame
import pygame.display
import pygame.draw
import pygame.key
import pygame.time

from pyinvaders.engine.colors import Colors
from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants
from pyinvaders.game.world_config import world_config


class GameController(object):
    def __init__(self):
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()


    def run(self):
        world_config()
        time_elapsed_since_last_show = 0.0
        while self.is_running:
            self.clock.tick()
            delta_time = self.clock.get_time() / 1000.0
            self._update(delta_time)
            if time_elapsed_since_last_show > 0.016666:
                self._show()
                time_elapsed_since_last_show -= 0.016666


    def _show(self):
        self.window.fill(Colors.WHITE.value)
        for game_object in GameObject.game_objects:
            game_object.show(self.window)
            pygame.display.update()


    def _update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        for game_object in GameObject.game_objects:
            game_object.update(delta_time)
