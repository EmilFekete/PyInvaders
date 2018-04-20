import pygame
import pygame.draw
import pygame.display
import pygame.key

from pyinvaders import constants


class GameController(object):
    def __init__(self):
        self.win = pygame.display.set_mode(constants.WINDOW_SIZE)
        pygame.display.set_caption(constants.TITLE)
        self.is_running = True
        self.clock = pygame.time.Clock()

    def run(self):
        x = 50
        y = 50
        while self.is_running:
            self.clock.tick(constants.FPS_CAP)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False

            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_LEFT]:
                x = x - 1
            elif pressed_keys[pygame.K_RIGHT]:
                x = x + 1
            self.win.fill(constants.BLACK)
            pygame.draw.rect(self.win, constants.RED, (x, y, 50, 100))
            pygame.display.update()

    def initialize(self):
        pass


