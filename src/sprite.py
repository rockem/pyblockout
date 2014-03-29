import pyglet
from pyglet.sprite import Sprite

BALL_IMAGE = 'ball.png'
PACK_IMAGE = 'pack.png'


class SpriteFactory:

    def __init__(self, batch):
        self._batch = batch

    def create_ball_sprite(self):
        return self.create_simple_sprite(BALL_IMAGE)

    def create_simple_sprite(self, img):
        return Sprite(self.load_image(img), batch=self._batch)

    def load_image(self, img_name):
        image = pyglet.resource.image(img_name)
        image.anchor_x = image.width / 2
        image.anchor_y = image.height / 2
        return image

    def create_pack_sprite(self):
        return self.create_simple_sprite(PACK_IMAGE)