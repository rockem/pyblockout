__author__ = 'elisegal'


class ClampComponent:

    def __init__(self, area_rect):
        self.rect = area_rect

    def update(self, sprite, elapsedTime):
        sprite.rect.clamp_ip(self.rect)


class BallMoveComponent:

    def __init__(self, pack):
        self.pack = pack

    def update(self, sprite, elapsedTime):
        topleft = self.pack.rect.topleft
        sprite.rect.midbottom = (topleft[0] + self.pack.rect.width / 2, topleft[1])

