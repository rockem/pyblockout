__author__ = 'elisegal'


class ClampComponent:

    def __init__(self, area_rect):
        self.rect = area_rect
        self.sprite = None

    def update(self, elapsed_time):
        self.sprite.rect.clamp_ip(self.rect)


class BallMoveComponent:

    def __init__(self, pack):
        self.pack = pack
        self.sprite = None

    def update(self, elapsed_time):
        topleft = self.pack.rect.topleft
        self.sprite.rect.midbottom = (topleft[0] + self.pack.rect.width / 2, topleft[1])

