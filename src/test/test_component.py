import mox
from nose.tools import assert_less, assert_true, assert_false, assert_greater, assert_equals, assert_not_equal
from component import BallPhysicsComponent, BlockCollisionComponent, SoundOnCollisionComponent
from game import GameObject
from rect import Rect
from sound import SoundFactory

__author__ = 'elisegal'


class StubGameObject(GameObject):

    def __init__(self, x, y):
        super(StubGameObject, self).__init__()
        self._x, self._y = x, y
        self.width, self.height = 10, 10

    def get_rect(self):
        return Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)


class AbstractTestBallPhysicsComponent(object):

    OBJECT_POS = (50, 50)
    PLAY_RECT = Rect(0, 0, 100, 100)

    def setup(self):
        self.game_object = StubGameObject(self.OBJECT_POS[0], self.OBJECT_POS[1])
        self.pack = StubGameObject(70, 70)
        self.move_comp = BallPhysicsComponent(self.pack, self.PLAY_RECT)
        self.move_comp.game_object = self.game_object

    def assert_ball_on_pack(self):
        assert self.game_object.x == self.pack.x
        assert self.game_object.y == self.pack.get_rect().top + self.game_object.height / 2

    def update(self):
        self.move_comp.update(1)


class TestBallPhysicsComponent_Play(AbstractTestBallPhysicsComponent):

    def setup(self):
        super(TestBallPhysicsComponent_Play, self).setup()
        self.move_comp.play()

    def test_should_move_ball(self):
        self.update()
        assert_not_equal(self.game_object.x_velocity, 0)
        assert_not_equal(self.game_object.y_velocity, 0)

    def test_should_change_horizontal_direction(self):
        self.game_object.x = self.PLAY_RECT.right - self.game_object.width / 2
        self.update()
        assert self.game_object.x_velocity < 0
        self.game_object.x = self.game_object.width / 2
        self.update()
        assert self.game_object.x_velocity > 0

    def test_should_change_vertical_direction(self):
        self.game_object.y = self.PLAY_RECT.top - self.game_object.height / 2
        self.update()
        assert self.game_object.y_velocity < 0

    def test_should_stay_when_ball_hit_bottom_of_play_rect(self):
        self.game_object.y = self.PLAY_RECT.bottom + self.game_object.height / 2
        self.update()
        self.assert_ball_on_pack()

    def test_should_change_vertical_dir_on_collision(self):
        self.game_object.y_velocity = 1
        self.game_object.handle_collision_with(StubGameObject(self.game_object.x, self.game_object.get_rect().top + 5))
        self.update()
        assert self.game_object.y_velocity < 0

    def test_should_change_horizontal_dir_on_collision(self):
        self.game_object.x_velocity = 1
        self.game_object.handle_collision_with(StubGameObject(self.game_object.get_rect().right + 5, self.game_object.y))
        self.update()
        assert self.game_object.x_velocity < 0

    def test_should_revert_dir_on_collision(self):
        self.game_object.x_velocity = 1
        self.game_object.y_velocity = 1
        self.game_object.handle_collision_with(
            StubGameObject(self.game_object.get_rect().right + 5, self.game_object.get_rect().bottom - 5))
        self.update()
        assert_less(self.game_object.x_velocity, 0)
        assert_equals(self.game_object.y_velocity, 1)


class TestBallPhysicsComponent_Stay(AbstractTestBallPhysicsComponent):

    def test_should_set_position_above_pack(self):
        self.update()
        self.assert_ball_on_pack()


class TestBlockCollisionComponent(object):

    def test_should_be_dead_when_collides(self):
        component = BlockCollisionComponent()
        component.game_object = StubGameObject(0, 0)
        component.on_collision_with(None)
        assert_false(component.game_object.alive)


class TestSoundOnCollisionComponent(object):

    SOUND_NAME = "popov"

    def test_should_play_on_collision(self):
        mocker = mox.Mox()
        sound_factory = mocker.CreateMock(SoundFactory)
        component = SoundOnCollisionComponent(self.SOUND_NAME, sound_factory)
        sound_factory.play_efx(self.SOUND_NAME)
        mocker.ReplayAll()
        component.on_collision_with(None)
        mocker.VerifyAll()
