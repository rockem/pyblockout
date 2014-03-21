from component.image import PackRenderer, BallRenderer

from component.input import UserInputComponent
from component.move import ClampComponent, BallMoveComponent
from rect import Rect


__author__ = 'eli.segal'


class SpriteCreator:

    def __init__(self, game_factory):
        self._game_factory = game_factory

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
        return sprite

    def __create_sprite(self):
        sprite = self._game_factory.create_sprite_object(self.renderer, self.groups)
        sprite.components = self.components
        return sprite

    def create(self):
        return self.__create_sprite()


class BlockOut:
    def __init__(self, game_factory, input_handler):
        self.game_factory = game_factory
        self.input_handler = input_handler
        self.background = self.create_background()
        self.running = True
        self.createAllSprites()

    def create_background(self):
        return self.game_factory.load_image('background.png')

    def createAllSprites(self):

        self.all_sprites = self.game_factory.create_batch()
        self.pack = SpriteCreator(self.game_factory).renderer(PackRenderer(self.game_factory)) \
            .groups(self.all_sprites) \
            .components([UserInputComponent(self.input_handler), ClampComponent(self.screenRect())]) \
            .create_at(self.screenRect().width / 2, 20)

        self.ball = SpriteCreator(self.game_factory).renderer(BallRenderer(self.game_factory)) \
            .groups(self.all_sprites) \
            .components([BallMoveComponent(self.pack)]) \
            .create()

    def screenRect(self):
        return Rect(0, 0, self.game_factory.screen.get_size()[0], self.game_factory.screen.get_size()[1])

    def quit(self):
        self.running = False

    def on_update(self, elapsed_time):
        self.pack.update(elapsed_time)
        self.ball.update(elapsed_time)

    def on_render(self):
        self.background.blit(self.game_factory.screen.width / 2, self.game_factory.screen.height / 2)
        self.all_sprites.draw()
