import pygame
from pygame_util import load_image

__author__ = 'elisegal'


class PackImageComponent:

    def __init__(self):
        self.image, self.rect = load_image('pack.png')
        self.sprite = None

    def update(self, elapsed_time):
        if not self.sprite.image:
            midbottom = self.sprite.rect.midbottom
            self.sprite.image = self.image
            self.sprite.rect.midbottom = midbottom


class BallImageComponent:

    def __init__(self):
        self.image = self.createBallImage()
        self.sprite = None

    def createBallImage(self):
        img = pygame.Surface((16, 16))
        pygame.draw.circle(img, (255, 255, 255), (8, 8), 8, 0)
        img = img.convert()
        return img

    def update(self, elapsed_time):
        if not self.sprite.image:
            self.sprite.image = self.image
            print "."  # Weirdest bug ever!
