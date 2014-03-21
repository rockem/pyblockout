import pyglet
from BlockOut import BlockOut
from game.pyglet_game import GameFactory, PygletInputHandler


class PygletMain(pyglet.window.Window):

    def __init__(self):
        super(PygletMain, self).__init__(800, 600)
        key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(key_handler)
        self.blockout = BlockOut(GameFactory(self), PygletInputHandler(key_handler))

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
