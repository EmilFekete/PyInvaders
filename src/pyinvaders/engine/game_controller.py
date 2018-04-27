import pygame
import pygame.draw
import pygame.display
import pygame.key
import pygame.time

from pyinvaders.game import constants
from pyinvaders.engine.game_object import GameObject
from pyinvaders.engine.graphic_handler import GraphicHandler
from pyinvaders.game.player import Player


class GameController(object):
    def __init__(self):
        self.window = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.graphic_handler = GraphicHandler(self.window)

    def run(self):
        while self.is_running:
            self.clock.tick(constants.FPS_CAP)
            delta_time = self.clock.get_time() / 1000.0
            self.update(delta_time)
            self.show()

    def show(self):
        self.graphic_handler.reset()
        for game_object in GameObject.game_objects:
            if game_object.visible:
                self.graphic_handler.handle_graphic(game_object.image_url, (game_object.x, game_object.y))
        pygame.display.update()

    def update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.player.x -= self.player.speed * delta_time
        elif pressed_keys[pygame.K_RIGHT]:
            self.player.x += self.player.speed * delta_time


