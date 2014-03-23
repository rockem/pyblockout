__author__ = 'elisegal'


class PackRenderer:

    def __init__(self, game_factory):
        self.image = game_factory.load_image('pack.png')
        self.sprite = None

    def update(self, elapsed_time):
        pass


class BallRenderer:

    def __init__(self, game_factory):
        self.image = game_factory.load_image('ball.png')
        self.sprite = None

    def update(self, elapsed_time):
        pass
