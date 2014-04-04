import pyglet

from blockout import BlockOut
from pyglet_game import GameFactory, PygletInputHandler


class LayoutProvider(object):

    def current_layout(self):
        # return ((1, 1, 1, 2, 0, 2, 0, 0),
        #         (0, 1, 0, 0, 2, 0, 0, 2),
        #         (0, 1, 0, 2, 0, 2, 0, 2),
        #         (0, 1, 0, 2, 0, 2, 0, 0),
        #         (0, 1, 0, 2, 0, 2, 0, 0),
        #         (1, 1, 1, 0, 2, 0, 0, 0))
        return ((1, 1, 1, 1, 1, 1, 1),
                (1, 1, 1, 1, 1, 1, 1),
                (1, 1, 2, 2, 2, 1, 1),
                (1, 1, 2, 2, 2, 1, 1),
                (1, 1, 1, 1, 1, 1, 1),
                (1, 1, 1, 1, 1, 1, 1))



class PygletMain(pyglet.window.Window):

    def __init__(self):
        super(PygletMain, self).__init__(800, 600)
        key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(key_handler)
        self.set_mouse_visible(False)
        self.layout_provider = LayoutProvider()
        self.blockout = BlockOut(GameFactory(self), PygletInputHandler(key_handler), self.layout_provider)


    def run(self):
        pyglet.clock.schedule_interval(self.update, 1/120.0)
        pyglet.app.run()

    def update(self, elapsed_time):
        self.blockout.on_update(elapsed_time)

    def on_draw(self):
        self.blockout.on_render()


if __name__ == '__main__':
    pyglet.resource.path = ['../image']
    pyglet.resource.reindex()
    PygletMain().run()
