from rect import Rect

__author__ = 'elisegal'


class GameObject(object):
    x_velocity = 0
    y_velocity = 0
    _components = []
    _new_position = (0, 0)

    def set_components(self, value):
        self._components = value
        for c in self._components:
            c.game_object = self

    components = property(lambda self: self._components, set_components)

    def update(self, elapsed_time):
        for c in self.components:
            c.update(elapsed_time)

    x = property(
        lambda self: self._get_x(),
        lambda self, x: self._set_x(x)
    )

    def _get_x(self):
        return 0

    def _set_x(self, value):
        pass

    y = property(
        lambda self: self._get_y(),
        lambda self, y: self._set_y(y)
    )

    def _get_y(self):
        return 0

    def _set_y(self, value):
        pass

    def _set_position(self, value):
        self.x = value[0]
        self.y = value[1]

    def _get_position(self):
        return self.x, self.y

    position = property(_get_position, _set_position)

    def get_new_rect(self):
        r = self.get_rect()
        r.center = self._new_position
        return r

    def get_rect(self):
        pass


class SpriteGameObject(GameObject):

    def __init__(self, sprite):
        self._sprite = sprite

    def get_rect(self):
        r = Rect(0, 0, self._sprite.width, self._sprite.height)
        r.center = (self.x, self.y)
        return r

    def _get_x(self):
        return self._sprite.x

    def _set_x(self, value):
        self._sprite.x = value

    def _get_y(self):
        return self._sprite.y

    def _set_y(self, value):
        self._sprite.y = value


