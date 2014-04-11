import pyglet

from blockout import BlockOut
from pyglet_game import GameFactory, PygletInputHandler
from sound import PygletSoundFactory


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

    LAYOUTS = [SCREEN1, SCREEN2]

    def __init__(self):
        self.current_layout = 0

    def get_next_layout(self):
        self.current_layout += 1
        return self.LAYOUTS[self.current_layout - 1]

    def current_is_last(self):
        return self.current_layout == len(self.LAYOUTS)


class PygletMain(pyglet.window.Window):
    def __init__(self):
        super(PygletMain, self).__init__(800, 600)
        key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(key_handler)
        self.set_mouse_visible(False)
        self.layout_provider = LayoutProvider()
        self.blockout = BlockOut(GameFactory(self), PygletInputHandler(key_handler), self.layout_provider)
        self.sound_factory = PygletSoundFactory()

    def run(self):
        self.sound_factory.play_background()
        pyglet.clock.schedule_interval(self.update, 1 / 120.0)
        pyglet.app.run()

    def update(self, elapsed_time):
        self.blockout.on_update(elapsed_time)

    def on_draw(self):
        self.blockout.on_render()


if __name__ == '__main__':
    pyglet.resource.path = ['../image', '../sound']
    pyglet.resource.reindex()
    PygletMain().run()
