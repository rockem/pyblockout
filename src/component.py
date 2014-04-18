from key import RIGHT, LEFT

__author__ = 'elisegal'


class GameComponent(object):

    _game_object = None

    game_object = property(
        lambda self: self._get_game_object(),
        lambda self, go: self._set_game_object(go)
    )

    def _get_game_object(self):
        return self._game_object

    def _set_game_object(self, go):
        self._game_object = go

    def update(self, elapsed_time):
        pass


class SimpleMoveComponent(GameComponent):
    def update(self, elapsed_time):
        self.game_object.x += self.game_object.x_velocity * elapsed_time
        self.game_object.y += self.game_object.y_velocity * elapsed_time


class UserInputComponent(GameComponent):
    PACK_SPEED = 300

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
    BALL_VELOCITY = 280

    def __init__(self, pack, play_rect):
        self._pack = pack
        self.play_rect = play_rect
        self._play_state = False

    def _set_game_object(self, go):
        super(BallPhysicsComponent, self)._set_game_object(go)
        self.game_object.on_collision += self.on_collision_with
        self.game_object.active = False

    def on_collision_with(self, other_object):
        if self.is_top_bottom_collision(other_object):
            self.handle_top_bottom_collision(other_object)
        elif self.is_right_left_collision(other_object):
            self.handle_left_right_collision(other_object)
        else:
            self.handle_corners_collision(other_object)

    def is_top_bottom_collision(self, other_object):
        return other_object.get_rect().left <= self.game_object.x <= other_object.get_rect().right

    def minus(self, number):
        return -abs(self.game_object.y_velocity)

    def handle_top_bottom_collision(self, other_object):
        abs_y_velocity = abs(self.game_object.y_velocity)
        if other_object.y > self.game_object.y:
            self.game_object.y_velocity = -abs_y_velocity
        else:
            self.game_object.y_velocity = abs_y_velocity

    def is_right_left_collision(self, other_object):
        return other_object.get_rect().top >= self.game_object.y >= other_object.get_rect().bottom

    def handle_left_right_collision(self, other_object):
        abs_x_velocity = abs(self.game_object.x_velocity)
        if other_object.x > self.game_object.x:
            self.game_object.x_velocity = -abs_x_velocity
        else:
            self.game_object.x_velocity = abs_x_velocity

    def handle_corners_collision(self, other_object):
        abs_x_velocity = abs(self.game_object.x_velocity)
        abs_y_velocity = abs(self.game_object.y_velocity)
        if other_object.x > self.game_object.x:
            self.game_object.x_velocity = -abs_x_velocity
        else:
            self.game_object.x_velocity = abs_x_velocity
        if other_object.y > self.game_object.y:
            self.game_object.y_velocity = -abs_y_velocity
        else:
            self.game_object.y_velocity = abs_y_velocity

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
        if self._play_state != state:
            self.game_object.active = state
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


class BlockCollisionComponent(GameComponent):

    def _set_game_object(self, go):
        super(BlockCollisionComponent, self)._set_game_object(go)
        go.on_collision += self.on_collision_with

    def on_collision_with(self, other_object):
        self.game_object.alive = False


class SoundOnCollisionComponent(GameComponent):

    def __init__(self, sound_name, sound_factory):
        self.sound_name = sound_name
        self.sound_factory = sound_factory

    def _set_game_object(self, go):
        super(SoundOnCollisionComponent, self)._set_game_object(go)
        go.on_collision += self.on_collision_with

    def on_collision_with(self, other_object):
        self.sound_factory.play_efx(self.sound_name)