import pygame
import pyglet
from BlockOut import BlockOut
from input.pygame_input_handler import PyGameInputHandler, PygletInputHandler


class PyGameMain:

    def __init__(self):
        self.blockout = BlockOut(self.create_pyglet_window())
        self.blockout.input_handler = PyGameInputHandler()
        self.clock = pygame.time.Clock()

    def create_pygame_screen(self):
        pygame.init()
        pygame.display.set_caption("BlockOut")
        screen = pygame.display.set_mode((640, 480))
        pygame.mouse.set_visible(False)
        return screen

    def create_pyglet_window(self):
        window = pyglet.window.Window(800, 600, caption="BlockOut")
        #pygame.mouse.set_visible(False)
        return window

    def run(self):
        while self.blockout.running:
            elapsed_time = self.clock.tick(60)
            pygame.display.set_caption("BlockOut [FPS:%s]" % self.clock.get_fps())
            self.blockout.on_events(pygame.event.get())
            self.blockout.on_update(elapsed_time)
            self.blockout.on_render()


class PygletMain(pyglet.window.Window):

    def __init__(self):
        super(PygletMain, self).__init__(800, 600)
        #self.window = pyglet.window.Window(800, 600, caption="BlockOut")
        key_handler = pyglet.window.key.KeyStateHandler()
        self.push_handlers(key_handler)
        self.blockout = BlockOut(self, PygletInputHandler(key_handler))

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
