from pygame.constants import K_RIGHT, K_LEFT


class PackControl(object):
    PACK_SPEED = 250

    location = (0, 0)
    input_handler = None

    def __init__(self, view_rect):
        self.view_rect = view_rect

    def dim(self, dimensions):
        self.size = dimensions
        self.location = (self.view_rect.width / 2 - dimensions[0] / 2, self.view_rect.height - (dimensions[1] + 2))

    def update(self, elapsedTime):
        newXLoc = int(self.location[0] + self.get_x_delta(elapsedTime))
        if self.packXPositionInRange(newXLoc):
            self.location = (newXLoc, self.location[1])

    def packXPositionInRange(self, newXLoc):
        return self.view_rect.width - self.size[0] >= newXLoc >= 0

    def get_x_delta(self, elapsedTime):
        delta_x = 0
        if self.input_handler.key_down(K_RIGHT):
            delta_x = self.PACK_SPEED * elapsedTime
        elif self.input_handler.key_down(K_LEFT):
            delta_x = -self.PACK_SPEED * elapsedTime
        return delta_x
