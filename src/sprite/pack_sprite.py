import os

import pygame
from pygame.constants import RLEACCEL

from enum import Enum


PlayerAction = Enum(["MOVE_RIGHT", "MOVE_LEFT"])


def load_image(name, color_key=None):
    fullname = os.path.join('image', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, RLEACCEL)
    return image, image.get_rect()


class PackSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('pack.png')
        self._control = None

    @property
    def control(self):
        return self._control

    @control.setter
    def control(self, value):
        self._control = value
        self._control.dim((self.rect.width, self.rect.height))

    def update(self, *args):
        self._control.update(*args)
        self.rect.topleft = self._control.location
