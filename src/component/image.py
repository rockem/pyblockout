__author__ = 'elisegal'


class PackRenderer:

    def __init__(self, game_factory):
        self.image = game_factory.load_image('pack.png')
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.sprite = None

    def update(self, elapsed_time):
        if not self.sprite.image:
            #midbottom = self.sprite.rect.midbottom
            self.sprite.image = self.image
            #self.sprite.rect.midbottom = midbottom


class BallRenderer:

    def __init__(self, game_factory):
        self.image = game_factory.load_image('ball.png')
        self.image.anchor_x = self.image.width / 2
        self.image.anchor_y = self.image.height / 2
        self.sprite = None

    def update(self, elapsed_time):
        if not self.sprite.image:
            self.sprite.image = self.image
            print "."  # Weirdest bug ever!
