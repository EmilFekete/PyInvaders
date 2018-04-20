from src.pyinvaders.game_object import GameObject


class Player(GameObject):
    def __init__(self):
        super(Player,self).__init__()
        self.velocity = 50