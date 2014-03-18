import pygame
from BlockOut import BlockOut


class PyGameMain:

    def __init__(self):
        self.blockout = BlockOut(self.create_pygame_screen())
        self.clock = pygame.time.Clock()

    def create_pygame_screen(self):
        pygame.init()
        pygame.display.set_caption("BlockOut")
        screen = pygame.display.set_mode((640, 480))
        pygame.mouse.set_visible(False)
        return screen

    def run(self):
        while self.blockout.running:
            elapsed_time = self.clock.tick(60)
            pygame.display.set_caption("BlockOut [FPS:%s]" % self.clock.get_fps())
            self.blockout.on_events(pygame.event.get())
            self.blockout.on_update(elapsed_time)
            self.blockout.on_render()


if __name__ == '__main__':
    PyGameMain().run()