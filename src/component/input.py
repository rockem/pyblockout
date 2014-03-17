from pygame.constants import K_RIGHT, K_LEFT

__author__ = 'elisegal'


class UserInputComponent:
    PACK_SPEED = 250

    def __init__(self, input_handler):
        self.input_handler = input_handler
        self.sprite = None

    def update(self, elapsed_time):
        self.sprite.rect.x = int(self.sprite.rect.x + self.get_x_delta(self.PACK_SPEED * elapsed_time))

    def get_x_delta(self, velocity):
        if self.input_handler.key_down(K_RIGHT):
            return velocity
        elif self.input_handler.key_down(K_LEFT):
            return -velocity
        return 0
