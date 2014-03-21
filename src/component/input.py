from game.key import RIGHT, LEFT

__author__ = 'elisegal'


class UserInputComponent:
    PACK_SPEED = 250

    def __init__(self, input_handler):
        self.input_handler = input_handler
        self.sprite = None

    def update(self, elapsed_time):
        self.sprite.x = int(self.sprite.x + self.get_x_delta(self.PACK_SPEED * elapsed_time))

    def get_x_delta(self, velocity):
        if self.input_handler.key_down(RIGHT):
            return velocity
        elif self.input_handler.key_down(LEFT):
            return -velocity
        return 0
