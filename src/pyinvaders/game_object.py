class GameObject(object):
    game_objects = list()

    def __init__(self):
        self.visible = True
        self.x = 50
        self.y = 50
        GameObject.game_objects.append(self)
