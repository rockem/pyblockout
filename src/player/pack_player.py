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

    def dim(self, dimensions):
        self.size = dimensions
        self._packLoc = (self.viewSize[0] / 2 - dimensions[0] / 2, self.viewSize[1] - (dimensions[1] + 2))

    def update(self):
        if PlayerAction.MOVE_RIGHT in self.actionsProvider.actions() and \
                self._packLoc[0] < self.viewSize[0] - self.size[0] - self.PACK_SPEED:
            self._packLoc = (self._packLoc[0] + self.PACK_SPEED, self._packLoc[1])
        elif PlayerAction.MOVE_LEFT in self.actionsProvider.actions() and \
                self._packLoc[0] > self.PACK_SPEED:
            self._packLoc = (self._packLoc[0] - self.PACK_SPEED, self._packLoc[1])

    def set_location(self, location):
        self._packLoc = location