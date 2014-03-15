import pygame

__author__ = 'elisegal'


class SpriteObject(pygame.sprite.Sprite):

    components = []

    def __init__(self, *groups):
        pygame.sprite.Sprite.__init__(self, *groups)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self._image = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        self.rect.size = self.image.get_rect().size

    def update(self, *args):
        for c in self.components:
            c.update(self, *args)

    def location(self, location):
        self.rect.topleft = location