from pygame.constants import K_RIGHT, KEYDOWN, KEYUP, K_LEFT
from pack_sprite import PlayerAction


class ActionsProvider:

    def actions(self):
        pass


class UserActionsProvider(ActionsProvider):

    KEY_TO_ACTION_MAP = {
        K_RIGHT: PlayerAction.MOVE_RIGHT,
        K_LEFT: PlayerAction.MOVE_LEFT,
    }

    _actions = []

    def actions(self):
        return self._actions

    def reset(self):
        self._actions = []

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key in self.KEY_TO_ACTION_MAP:
                self._actions.append(self.KEY_TO_ACTION_MAP[event.key])
        elif event.type == KEYUP:
            if event.key in self.KEY_TO_ACTION_MAP:
                self._actions.remove(self.KEY_TO_ACTION_MAP[event.key])

