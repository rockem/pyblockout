import pyglet

import key
from rect import Rect


__author__ = 'elisegal'


class SpriteObject(pyglet.sprite.Sprite):

    _components = []

    def __init__(self, renderer, group):
        pyglet.sprite.Sprite.__init__(self, renderer.image, batch=group)
        self.renderer = renderer
        self._image = None

    def set_components(self, value):
        self._components = value
        for c in self._components:
            c.sprite = self

    def get_components(self):
        return self._components

    components = property(get_components, set_components)

    def update(self, *args):
        for c in self.components:
            c.update(*args)

    def get_rect(self):
        r = Rect(0, 0, self.width, self.height)
        r.center = (self.x, self.y)
        return r


class GameFactory:

    def load_image(self, img_name):
        return pyglet.resource.image(img_name)


class PygletInputHandler:

    pygletKeyDict = {
        key.LEFT: pyglet.window.key.LEFT,
        key.RIGHT: pyglet.window.key.RIGHT,
        key.SPACE: pyglet.window.key.SPACE
    }

    def __init__(self, key_handler):
        self.key_handler = key_handler

    def key_down(self, k):
        return self.key_handler[self.pygletKeyDict[k]]

    def input_type(self, type):
        pass
