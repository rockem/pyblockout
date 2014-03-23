__author__ = 'elisegal'


class Rect(object):

    def __init__(self, x, y, width, height):
        self._x, self._y = x, y
        self._width, self._height = width, height

    def set_x(self, value): self._x = value
    x = property(lambda self: self._x, set_x)

    def set_y(self, value): self._y = value
    y = property(lambda self: self._y, set_y)

    def set_width(self, value): self._width = value
    width = property(lambda self: self._width, set_width)

    def set_height(self, value): self._height = value
    height = property(lambda self: self._height, set_height)

    def set_pos(self, value): self._x, self._y = value
    pos = property(lambda self: (self._x, self._y), set_pos)

    def set_size(self, value): self._width, self._height = value
    size = property(lambda self: (self._width, self._height), set_size)

    def get_center(self):
        return self.x + self.width / 2, self.y + self.height / 2

    def set_center(self, center):
        x, y = center
        self.pos = (x - self.width/2, y - self.height/2)
    center = property(get_center, set_center)

    def get_top(self): return self.y + self.height
    def set_top(self, y): self.y = y - self.height
    top = property(get_top, set_top)

    def get_bottom(self): return self.y
    def set_bottom(self, y): self.y = y
    bottom = property(get_bottom, set_bottom)

    def get_left(self): return self.x
    def set_left(self, x): self.x = x
    left = property(get_left, set_left)

    def get_right(self): return self.x + self.width
    def set_right(self, x): self.x = x - self.width
    right = property(get_right, set_right)

    def clamp_ip(self, rect):
        if self._x < rect.x: self._x = rect.x
        if self._y < rect.y: self._y = rect.y
        if self._x + self._width > rect.x + rect.width: self._x = rect.x + rect.width - self._width
        if self._y + self._height > rect.y + rect.height: self._y = rect.y + rect.height - self._height
