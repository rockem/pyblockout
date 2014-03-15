import pygame
from pygame_util import load_image

__author__ = 'elisegal'


class PackImageComponent:

    def __init__(self):
        self.image, self.rect = load_image('pack.png')

    def update(self, sprite_object, *args):
        if not sprite_object.image:
            midbottom = sprite_object.rect.midbottom
            sprite_object.image = self.image
            # sprite_object.rect.size = self.rect.size
            sprite_object.rect.midbottom = midbottom


class BallImageComponent:

    def __init__(self):
        self.image = self.createBallImage()
        self.rect = self.image.get_rect()

    def createBallImage(self):
        img = pygame.Surface((16, 16))
        pygame.draw.circle(img, (255, 255, 255), (8, 8), 8, 0)
        img = img.convert()
        return img

    def update(self, sprite_object, *args):
        if not sprite_object.image:
            sprite_object.image = self.image


