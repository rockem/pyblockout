from key import RIGHT, LEFT

__author__ = 'elisegal'


class GameComponent:

    sprite = None


class UserInputComponent(GameComponent):
    PACK_SPEED = 250

    def __init__(self, input_handler):
        self.input_handler = input_handler

    def update(self, elapsed_time):
        self.sprite.x = int(self.sprite.x + self.get_x_delta(self.PACK_SPEED * elapsed_time))

    def get_x_delta(self, velocity):
        if self.input_handler.key_down(RIGHT):
            return velocity
        elif self.input_handler.key_down(LEFT):
            return -velocity
        return 0


class ClampComponent(GameComponent):
    def __init__(self, area_rect):
        self.rect = area_rect

    def update(self, elapsed_time):
        sprite_rect = self.sprite.get_rect()
        sprite_rect.clamp_ip(self.rect)
        self.sprite.position = sprite_rect.center


class BallMoveComponent(GameComponent):
    BALL_VELOCITY = 300

    def __init__(self, pack, play_rect):
        self._pack = pack
        self.play_rect = play_rect
        self.init()

    def init(self):
        self._play_state = False
        self._x_dir = 1
        self._y_dir = 1

    def update(self, elapsed_time):
        if self.hit_bottom():
            self.init()
        if not self._play_state:
            self.keep_ball_on_pack()
        else:
            self.update_direction()
            self.sprite.x += self._x_dir * self.BALL_VELOCITY * elapsed_time
            self.sprite.y += self._y_dir * self.BALL_VELOCITY * elapsed_time

    def hit_bottom(self):
        return self.play_rect.bottom == self.sprite.get_rect().bottom

    def keep_ball_on_pack(self):
        self.sprite.x = self._pack.x
        self.sprite.y = self._pack.y + self._pack.height / 2 + self.sprite.height / 2

    def update_direction(self):
        if self.play_rect.right == self.sprite.get_rect().right or \
                        self.play_rect.x == self.sprite.get_rect().left:
            self._x_dir *= -1
        if self.play_rect.top == self.sprite.get_rect().top:
            self._y_dir *= -1

    def play(self):
        self._play_state = True

    def stay(self):
        self._play_state = False
