from pack_sprite import PlayerAction
from action_provider import ActionsProvider


class DummyActionsProvider(ActionsProvider):
    def actions(self):
        return []


class PackPlayer(object):
    PACK_SPEED = 2

    actionsProvider = DummyActionsProvider()

    def __init__(self, viewSize):
        self.viewSize = viewSize
        self._packLoc = (0, 0)

    def get_location(self):
        return self._packLoc

    def set_location(self, location):
        self._packLoc = location

    def dim(self, dimensions):
        self.size = dimensions
        self._packLoc = (self.viewSize[0] / 2 - dimensions[0] / 2, self.viewSize[1] - (dimensions[1] + 2))

    def update(self):
        newXLoc = self._packLoc[0] + self.get_x_delta()
        if self.packXPositionInRange(newXLoc):
            self._packLoc = (newXLoc, self._packLoc[1])

    def packXPositionInRange(self, newXLoc):
        return self.viewSize[0] - self.size[0] >= newXLoc >= 0

    def get_x_delta(self):
        deltaX = 0
        if PlayerAction.MOVE_RIGHT in self.actionsProvider.actions():
            deltaX = self.PACK_SPEED
        elif PlayerAction.MOVE_LEFT in self.actionsProvider.actions():
            deltaX = -self.PACK_SPEED
        return deltaX
