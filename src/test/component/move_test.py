from component import BallMoveComponent
from rect import Rect

__author__ = 'elisegal'


class StubSprite(object):

    def __init__(self, x, y):
        self._x, self._y = x, y
        self._width, self._height = 10, 10

    def set_x(self, value):
        self._x = value
    x = property(lambda self: self._x, set_x)

    def set_y(self, value): self._y = value
    y = property(lambda self: self._y, set_y)

    def set_width(self, value): self._width = value
    width = property(lambda self: self._width, set_width)

    def set_height(self, value): self._height = value
    height = property(lambda self: self._height, set_height)

    def set_pos(self, pos):
        self._x = pos[0]
        self._Y = pos[1]

    def get_pos(self):
        return self._x, self._y

    position = property(get_pos, set_pos)

    def get_rect(self):
        return Rect(self.x - self.width / 2, self.y - self.height / 2, self.width, self.height)


class TestBallMoveComponent:

    SPRITE_POS = (50, 50)
    PLAY_RECT = Rect(0, 0, 100, 100)

    def setup(self):
        self.sprite = StubSprite(self.SPRITE_POS[0], self.SPRITE_POS[1])
        self.move_comp = BallMoveComponent(StubSprite(70, 70), self.PLAY_RECT)
        self.move_comp.sprite = self.sprite
        self.move_comp.play()


class TestBallMoveComponent_Play:

    SPRITE_POS = (50, 50)
    PLAY_RECT = Rect(0, 0, 100, 100)

    def setup(self):
        self.sprite = StubSprite(self.SPRITE_POS[0], self.SPRITE_POS[1])
        self.pack = StubSprite(70, 70)
        self.move_comp = BallMoveComponent(self.pack, self.PLAY_RECT)
        self.move_comp.sprite = self.sprite

    def test_should_set_position_above_pack(self):
        self.update()
        assert self.sprite.x == self.pack.x
        assert self.sprite.y == self.pack.get_rect().top + self.sprite.height / 2

    def update(self):
        self.move_comp.update(1)

    def test_should_move_ball(self):
        old_pos = self.sprite.position
        self.update()
        assert self.sprite.position != old_pos

    def test_should_change_horizontal_direction(self):
        self.move_comp.play()
        old_x = self.sprite.x
        self.sprite.x = self.PLAY_RECT.right - self.sprite.width / 2
        self.update()
        assert self.sprite.get_rect().right < self.PLAY_RECT.right
        self.sprite.x = self.sprite.width / 2
        self.update()
        assert self.sprite.get_rect().left > 0

    def test_should_change_vertical_direction(self):
        self.move_comp.play()
        self.sprite.y = self.PLAY_RECT.top - self.sprite.height / 2
        self.update()
        assert self.sprite.get_rect().top < self.PLAY_RECT.top



