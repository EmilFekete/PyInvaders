import pygame.key

from pyinvaders.engine.game_controller import GameController


def main():
    game_controller = GameController()
    game_controller.run()


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
