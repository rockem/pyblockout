import pyglet
from pyglet.sprite import Sprite

BALL_IMAGE = 'ball.png'
PACK_IMAGE = 'pack.png'
RED_BLOCK_IMAGE = 'red_block.png'
WHITE_BLOCK_IMAGE = 'white_block.png'


class SpriteFactory:

    def __init__(self):
        self._batch = pyglet.graphics.Batch()

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

    def create_red_block(self):
        return self.create_simple_sprite(RED_BLOCK_IMAGE)

    def create_white_block(self):
        return self.create_simple_sprite(WHITE_BLOCK_IMAGE)

    def create_win_message(self):
        return self.create_simple_sprite('win_message.png')

    def draw(self):
        self._batch.draw()