import subprocess
import pyglet

from blockout import BlockOut
from pyglet_game import GameFactory, PygletInputHandler
from rect import Rect
from sound import PygletSoundFactory
from sprite import SpriteFactory


class LayoutProvider(object):
    LOVE1 = ((1, 1, 1),
             (0, 1, 0),
             (0, 1, 0),
             (0, 1, 0),
             (0, 1, 0),
             (1, 1, 1))

    LOVE2 = ((2, 2, 2, 0, 2, 2, 2),
             (2, 0, 0, 2, 0, 0, 2),
             (0, 2, 0, 0, 0, 2, 0),
             (0, 2, 0, 0, 0, 2, 0),
             (0, 0, 2, 0, 2, 0, 0),
             (0, 0, 0, 2, 0, 0, 0))

    LOVE3 = ((1, 0, 0, 0, 1),
             (1, 0, 0, 0, 1),
             (1, 0, 0, 0, 1),
             (1, 0, 0, 0, 1),
             (1, 0, 0, 0, 1),
             (0, 1, 1, 1, 0))

    SCREEN1 = ((1, 1, 1, 1, 1, 1, 1),
               (1, 0, 0, 0, 0, 0, 1),
               (1, 0, 2, 0, 2, 0, 1),
               (1, 0, 2, 0, 2, 0, 1),
               (1, 0, 0, 0, 0, 0, 1),
               (1, 1, 1, 1, 1, 1, 1))

    SCREEN2 = ((1, 1, 1, 1, 1, 1, 1),
               (1, 1, 1, 1, 1, 1, 1),
               (1, 1, 2, 2, 2, 1, 1),
               (1, 1, 2, 2, 2, 1, 1),
               (1, 1, 1, 1, 1, 1, 1),
               (1, 1, 1, 1, 1, 1, 1))

    LAYOUTS = [LOVE1, LOVE2, LOVE3]

    def __init__(self):
        self.current_layout = 0

    def get_next_layout(self):
        self.current_layout += 1
        return self.LAYOUTS[self.current_layout - 1]

    def current_is_last(self):
        return self.current_layout == len(self.LAYOUTS)


class PygletMain(pyglet.window.Window):
    SCREEN_SIZE = (800, 600)

    def __init__(self):
        super(PygletMain, self).__init__(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1])
        self.key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(self.key_handler)
        self.set_mouse_visible(False)
        self.blockout = self.create_blockout()

    def create_blockout(self):
        blockout = BlockOut()
        blockout.screen_rect = Rect(0, 0, self.SCREEN_SIZE[0], self.SCREEN_SIZE[1])
        blockout.input_handler = PygletInputHandler(self.key_handler)
        blockout.layout_provider = LayoutProvider()
        blockout.sound_factory = PygletSoundFactory()
        blockout.sprite_factory = SpriteFactory()
        blockout.game_factory = GameFactory()
        return blockout

    def run(self):
        self.blockout.init()
        self.player = subprocess.Popen(["afplay", "sillylovesongs.mp3"])
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
        pyglet.app.run()

    def update(self, elapsed_time):
        self.blockout.on_update(elapsed_time)

    def on_draw(self):
        self.blockout.on_render()

    def on_close(self):
        self.player.terminate()
        super(PygletMain, self).on_close()


if __name__ == '__main__':
    pyglet.resource.path = ['../image', '../sound']
    pyglet.resource.reindex()
    PygletMain().run()
