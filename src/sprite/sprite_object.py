import pygame
import pyglet

__author__ = 'elisegal'


class SpriteObject(pyglet.sprite.Sprite):

    _components = []

    def __init__(self, renderer, group):
        pyglet.sprite.Sprite.__init__(self, renderer.image, batch=group)
        self.renderer = renderer
        #self.rect = pygame.Rect(0, 0, 0, 0)
        self._image = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.rect.size = self.image.get_rect().size

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
