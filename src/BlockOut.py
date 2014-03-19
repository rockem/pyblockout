from pygame.constants import QUIT, K_ESCAPE
import pyglet
from component.image import PackRenderer, BallRenderer

from component.input import UserInputComponent
from component.move import ClampComponent, BallMoveComponent
from rect import Rect
from sprite.sprite_object import SpriteObject


__author__ = 'eli.segal'


class SpriteCreator:

    def components(self, components):
        self.components = components
        return self

    def groups(self, groups):
        self.groups = groups
        return self

    def renderer(self, renderer):
        self.renderer = renderer
        return self

    def create_at(self, x, y):
        sprite = self.__create_sprite()
        sprite.x, sprite.y = x, y
        #or p in rect_properties:
        #    setattr(sprite.rect, p, rect_properties[p])
        return sprite

    def __create_sprite(self):
        sprite = SpriteObject(self.renderer, self.groups)
        sprite.components = self.components
        return sprite

    def create(self):
        return self.__create_sprite()


class BlockOut:
    def __init__(self, screen, input_handler):
        self.screen = screen
        self.input_handler = input_handler
        self.background = self.create_background()
        self.running = True
        self.createAllSprites()

    def create_background(self):
        return pyglet.resource.image('background.png')

    def createAllSprites(self):

        #self.all_sprites = pygame.sprite.Group()
        self.all_sprites = pyglet.graphics.Batch()
        self.pack = SpriteCreator().renderer(PackRenderer()) \
            .groups(self.all_sprites) \
            .components([UserInputComponent(self.input_handler), ClampComponent(self.screenRect())]) \
            .create_at(self.screen.width / 2, 20)

        self.ball = SpriteCreator().renderer(BallRenderer()) \
            .groups(self.all_sprites) \
            .components([BallMoveComponent(self.pack)]) \
            .create()

    def screenRect(self):
        return Rect(0, 0, self.screen.get_size()[0], self.screen.get_size()[1])

    def on_events(self, events):
        self.input_handler.update(events)
        if self.should_quit():
            self.quit()

    def should_quit(self):
        return self.input_handler.input_type(QUIT) or self.input_handler.key_down(K_ESCAPE)

    def quit(self):
        self.running = False

    def on_update(self, elapsed_time):
        #self.all_sprites.update(elapsed_time / 1000.0)
        self.pack.update(elapsed_time)
        self.ball.update(elapsed_time)

    def on_render(self):
        #self.screen.blit(self.background, (0, 0))
        #self.all_sprites.draw(self.screen)
        # pygame.display.update()
        self.background.blit(0, 0)
        self.all_sprites.draw()
