import mox
from pack_sprite import PlayerAction

from src.action_provider import ActionsProvider
from src.player.pack_player import PackPlayer


class TestPackPlayer:
    PACK_HEIGHT = 5
    PACK_WIDTH = 16
    SCREEN_HEIGHT = 100
    SCREEN_WIDTH = 100

    def setup_method(self, method):
        self.packPlayer = PackPlayer((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.packPlayer.dim((self.PACK_WIDTH, self.PACK_HEIGHT))
        self.mocker = mox.Mox()
        self.actionsProvider = self.mocker.CreateMock(ActionsProvider)
        self.packPlayer.actionsProvider = self.actionsProvider

    def test_should_be_in_the_center(self):
        assert self.packPlayer.get_location()[0] == 100 / 2 - 16 / 2

    def test_should_move_to_the_right(self):
        self.setActionsTo([PlayerAction.MOVE_RIGHT])
        oldLoc = self.packPlayer.get_location()
        self.packPlayer.update()
        assert self.packPlayer.get_location()[0] > oldLoc[0]

    def setActionsTo(self, actions):
        self.actionsProvider.actions().MultipleTimes().AndReturn(actions)
        self.mocker.ReplayAll()

    def test_should_not_pass_the_right_edge_of_the_screen(self):
        self.setActionsTo([PlayerAction.MOVE_RIGHT])
        oldLoc = (self.SCREEN_WIDTH - self.PACK_WIDTH,
                  self.packPlayer.get_location()[1])
        self.packPlayer.set_location(oldLoc)
        self.packPlayer.update()
        assert self.packPlayer.get_location() == oldLoc

    def test_should_move_to_the_left(self):
        self.setActionsTo([PlayerAction.MOVE_LEFT])
        oldLoc = self.packPlayer.get_location()
        self.packPlayer.update()
        assert self.packPlayer.get_location()[0] < oldLoc[0]

    def test_should_not_pass_the_left_edge_of_the_screen(self):
        self.setActionsTo([PlayerAction.MOVE_LEFT])
        oldLoc = (0, self.packPlayer.get_location()[1])
        self.packPlayer.set_location(oldLoc)
        self.packPlayer.update()
        assert self.packPlayer.get_location() == oldLoc