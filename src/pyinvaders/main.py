import pygame
import pygame.draw
import pygame.display
import pygame.key
from pyinvaders.game_controller import GameController


def main():
    game_controller = GameController()
    game_controller.run()

if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
