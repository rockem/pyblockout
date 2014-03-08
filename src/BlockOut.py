import pygame
from pygame.constants import QUIT, K_ESCAPE

from control.pack_control import PackControl

from src.input.pygame_input_handler import PyGameInputHandler
from src.sprite.pack_sprite import PackSprite


__author__ = 'eli.segal'


class CreateSprite:
    def __init__(self, sprite, view_rect):
        self.sprite = sprite()
        self.view_rect = view_rect
        self.control = None
        self.input_handler = None

    def controlled_by(self, control):
        self.control = control(self.view_rect)
        return self

    def with_input(self, input_handler):
        self.input_handler = input_handler
        return self

    def in_group(self, group):
        self.control.input_handler = self.input_handler
        self.sprite.control = self.control
        group.add(self.sprite)


class BlockOut:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("BlockOut")
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.background = self.create_background()
        self.input_handler = PyGameInputHandler()
        self.running = True
        self.elapsed_time = 0

        self.all_sprites = pygame.sprite.Group()
        self.create_sprite(PackSprite).controlled_by(PackControl).with_input(self.input_handler).in_group(self.all_sprites)

    def create_background(self):
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))
        return background

    def run(self):

        while self.running:
            self.elapsed_time = self.clock.tick(60)
            pygame.display.set_caption("BlockOut [FPS:%s]" % self.clock.get_fps())
            self.on_events()
            self.on_update()
            self.on_render()

    def on_events(self):
        self.input_handler.update(pygame.event.get())
        if self.should_quit():
            self.quit()

    def should_quit(self):
        return self.input_handler.input_type(QUIT) or self.input_handler.key_down(K_ESCAPE)

    def quit(self):
        self.running = False

    def on_update(self):
        self.all_sprites.update(self.elapsed_time / 1000.0)

    def on_render(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def create_sprite(self, sprite):
        return CreateSprite(sprite, self.screen.get_rect())