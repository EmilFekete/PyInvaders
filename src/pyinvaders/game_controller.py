import pygame
import pygame.draw
import pygame.display
import pygame.key
import pygame.time

from src.pyinvaders import constants
from src.pyinvaders.game_object import GameObject
from src.pyinvaders.player import Player


class GameController(object):
    def __init__(self):
        self.win = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.player = Player()

    def run(self):
        while self.is_running:
            self.clock.tick(constants.FPS_CAP)
            delta_time = self.clock.get_time() / 1000.0
            self.update(delta_time)
            self.show()

    def show(self):
        pygame.display.update()
        self.win.fill(constants.BLACK)
        for go in GameObject.game_objects:
            pygame.draw.rect(self.win, constants.RED, (go.x, go.y, 50, 100))


    def update(self, delta_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            self.player.x -= self.player.velocity*delta_time
        elif pressed_keys[pygame.K_RIGHT]:
            self.player.x += self.player.velocity*delta_time


    def initialize(self):
        pass


