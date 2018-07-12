import pygame
import pygame.display
import pygame.draw
import pygame.key
import pygame.time

from pyinvaders.engine.colors import Colors
from pyinvaders.engine.game_object import GameObject
from pyinvaders.game import constants
from pyinvaders.game.world_config import setup_world


class GameController(object):
    TIME_BETWEEN_FRAMES_IN_SECONDS = 0.016666
    MILLISECONDS_IN_A_SECOND = 1000.0

    def __init__(self):
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self._time_elapsed_since_previous_frame = 0.0
        self.delta_time = 0.0

    def run(self):
        setup_world()
        while self.is_running:
            self._update()

    def _update(self):
        self._calculate_delta_time()
        self._update_game_state()
        if self._should_update_display():
            self._update_display()

    def _calculate_delta_time(self):
        self.clock.tick()
        self.delta_time = self.clock.get_time() / GameController.MILLISECONDS_IN_A_SECOND
        self._time_elapsed_since_previous_frame += self.delta_time

    def _should_update_display(self):
        return self._time_elapsed_since_previous_frame > GameController.TIME_BETWEEN_FRAMES_IN_SECONDS

    def _update_display(self):
        self.window.fill(Colors.WHITE.value)
        for game_object in GameObject.game_objects:
            game_object.show(self.window)
            pygame.display.update()
        self._time_elapsed_since_previous_frame -= GameController.TIME_BETWEEN_FRAMES_IN_SECONDS

    def _update_game_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
        for game_object in GameObject.game_objects:
            game_object.update(self.delta_time)
