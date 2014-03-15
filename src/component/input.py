from pygame.constants import K_RIGHT, K_LEFT

__author__ = 'elisegal'


class UserInputComponent:
    PACK_SPEED = 250

    def __init__(self, input_handler):
        self.input_handler = input_handler

    def update(self, pack, elapsedTime):
        pack.rect.x = int(pack.rect.x + self.get_x_delta(self.PACK_SPEED * elapsedTime))

    def get_x_delta(self, velocity):
        if self.input_handler.key_down(K_RIGHT):
            return velocity
        elif self.input_handler.key_down(K_LEFT):
            return -velocity
        return 0
