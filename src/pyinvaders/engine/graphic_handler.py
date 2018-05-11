import pygame

from pyinvaders.engine.colors import Colors


class GraphicHandler(object):
    def __init__(self, window):
        self.window = window

    def reset(self):
        self.window.fill(Colors.WHITE.value)

    def handle_graphic(self, image_url, coordinates):
        image = pygame.image.load(image_url)
        self.window.blit(image, coordinates)
