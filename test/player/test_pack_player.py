import mox
from pygame.constants import K_RIGHT, K_LEFT
from pygame.rect import Rect

from src.sprite.pack_sprite import PlayerAction
from src.control.pack_control import PackControl


class StubInputHandler:
    def update(self, events):
        pass

    def add_event(self, type, value=None):
        pass

    def key_down(self, key):
        pass

    def input_type(self, type):
        pass


class TestPackPlayer:
    PACK_HEIGHT = 5
    PACK_WIDTH = 16
    SCREEN_HEIGHT = 100
    SCREEN_WIDTH = 100

    def setup(self):
        self.packPlayer = PackControl(Rect(0, 0, self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.packPlayer.dim((self.PACK_WIDTH, self.PACK_HEIGHT))
        self.mocker = mox.Mox()
        self.input_handler = self.mocker.CreateMock(StubInputHandler)
        self.packPlayer.input_handler = self.input_handler

    def test_should_be_in_the_center(self):
        assert self.packPlayer.location[0] == self.SCREEN_WIDTH / 2 - self.PACK_WIDTH / 2

    def test_should_move_to_the_right(self):
        self.setInputTo(K_RIGHT)
        oldLoc = self.packPlayer.location
        self.packPlayer.update(0.1)
        assert self.packPlayer.location[0] > oldLoc[0]

    def setInputTo(self, inout):
        self.input_handler.key_down(inout).MultipleTimes().AndReturn(True)
        self.input_handler.key_down(mox.Not(mox.IsA(input))).MultipleTimes().AndReturn(False)
        self.mocker.ReplayAll()

    def test_should_not_pass_the_right_edge_of_the_screen(self):
        self.setInputTo(K_RIGHT)
        oldLoc = (self.SCREEN_WIDTH - self.PACK_WIDTH,
                  self.packPlayer.location[1])
        self.packPlayer.location = oldLoc
        self.packPlayer.update(0.1)
        assert self.packPlayer.location == oldLoc

    def test_should_move_to_the_left(self):
        self.setInputTo(K_LEFT)
        oldLoc = self.packPlayer.location
        self.packPlayer.update(0.1)
        assert self.packPlayer.location[0] < oldLoc[0]

    def test_should_not_pass_the_left_edge_of_the_screen(self):
        self.setInputTo(K_LEFT)
        oldLoc = (0, self.packPlayer.location[1])
        self.packPlayer.location = oldLoc
        self.packPlayer.update(0.1)
        assert self.packPlayer.location == oldLoc