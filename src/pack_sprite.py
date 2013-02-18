import os
import pygame
from pygame.constants import RLEACCEL, K_RIGHT, KEYDOWN
from src.enum import Enum

PlayerAction = Enum(["MOVE_RIGHT", "MOVE_LEFT"])

def load_image(name, colorkey=None):
    fullname = os.path.join('image', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()


class PackSprite(pygame.sprite.Sprite):

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('pack.png')
        self.player = player
        self.player.dim((self.rect.width, self.rect.height))

    def update(self):
        self.player.update()
        self.rect.topleft = self.player.get_location()
