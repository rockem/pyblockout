import pygame
from rect import Rect

__author__ = 'elisegal'


class ClampComponent:

    def __init__(self, area_rect):
        self.rect = area_rect
        self.sprite = None

    def update(self, elapsed_time):
        sprite_rect = Rect(0, 0, self.sprite.width, self.sprite.height)
        sprite_rect.center = (self.sprite.x, self.sprite.y)
        sprite_rect.clamp_ip(self.rect)
        self.sprite.position = sprite_rect.center


class BallMoveComponent:

    def __init__(self, pack):
        self.pack = pack
        self.sprite = None

    def update(self, elapsed_time):
        self.sprite.x = self.pack.x
        self.sprite.y = self.pack.y + self.pack.height / 2 + self.sprite.height / 2

