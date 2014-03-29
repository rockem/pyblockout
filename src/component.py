from key import RIGHT, LEFT

__author__ = 'elisegal'


class GameComponent:
    game_object = None


class SimpleMoveComponent(GameComponent):
    def update(self, elapsed_time):
        self.game_object.x += self.game_object.x_velocity * elapsed_time
        self.game_object.y += self.game_object.y_velocity * elapsed_time


class UserInputComponent(GameComponent):
    PACK_SPEED = 250

    def __init__(self, input_handler):
        self.input_handler = input_handler

    def update(self, elapsed_time):
        self.game_object.x_velocity = self._get_x_velocity()

    def _get_x_velocity(self):
        if self.input_handler.key_down(RIGHT):
            return self.PACK_SPEED
        elif self.input_handler.key_down(LEFT):
            return -self.PACK_SPEED
        return 0


class ClampComponent(GameComponent):
    def __init__(self, area_rect):
        self.rect = area_rect

    def update(self, elapsed_time):
        sprite_rect = self.game_object.get_rect()
        sprite_rect.clamp_ip(self.rect)
        self.game_object.position = sprite_rect.center


class BallPhysicsComponent(GameComponent):
    BALL_VELOCITY = 300

    def __init__(self, pack, play_rect):
        self._pack = pack
        self.play_rect = play_rect
        self._play_state = False
        self.game_object.on_collision += self.on_collision_with

    def on_collision_with(self, other_object):
        pass

    def update(self, elapsed_time):
        if self.hit_bottom():
            self.stay()
        if not self._play_state:
            self.keep_ball_on_pack()
        else:
            self.update_direction()

    def hit_bottom(self):
        return self.play_rect.bottom == self.game_object.get_rect().bottom

    def stay(self):
        self._set_play_state(False)

    def _set_play_state(self, state):
        self._play_state = state
        velocity = 0
        if state:
            velocity = self.BALL_VELOCITY
        self.game_object.x_velocity = velocity
        self.game_object.y_velocity = velocity

    def keep_ball_on_pack(self):
        self.game_object.x = self._pack.x
        self.game_object.y = self._pack.get_rect().top + self.game_object.get_rect().width / 2

    def update_direction(self):
        if self.play_rect.right == self.game_object.get_rect().right \
                or self.play_rect.x == self.game_object.get_rect().left:
            self.game_object.x_velocity *= -1
        if self.play_rect.top == self.game_object.get_rect().top:
            self.game_object.y_velocity *= -1

    def play(self):
        self._set_play_state(True)


