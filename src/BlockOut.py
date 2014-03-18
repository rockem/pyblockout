import pygame
from pygame.constants import QUIT, K_ESCAPE

from component.image import PackImageComponent, BallImageComponent
from component.input import UserInputComponent
from component.move import ClampComponent, BallMoveComponent
from input.pygame_input_handler import PyGameInputHandler
from pygame_util import load_image
from sprite.sprite_object import SpriteObject


__author__ = 'eli.segal'


class SpriteCreator:
    def __init__(self):
        pass

    def components(self, components):
        self.components = components
        return self

    def groups(self, groups):
        self.groups = groups
        return self

    def create_at(self, rect_properties):
        sprite = self.__create_sprite()
        for p in rect_properties:
            setattr(sprite.rect, p, rect_properties[p])
        return sprite

    def __create_sprite(self):
        sprite = SpriteObject(self.groups)
        sprite.components = self.components
        return sprite

    def create(self):
        return self.__create_sprite()


class BlockOut:
    def __init__(self, screen):
        self.screen = screen
        self.background = self.create_background()
        self.input_handler = PyGameInputHandler()
        self.running = True
        self.createAllSprites()

    def create_background(self):
        return load_image('background.png')[0]

    def createAllSprites(self):
        self.all_sprites = pygame.sprite.Group()
        self.pack = SpriteCreator().groups(self.all_sprites) \
            .components(
            [UserInputComponent(self.input_handler), ClampComponent(self.screenRect()), PackImageComponent()]) \
            .create_at({'midbottom': (self.screenRect().width / 2, self.screenRect().height - 2)})

        self.ball = SpriteCreator().groups(self.all_sprites) \
            .components([BallMoveComponent(self.pack), BallImageComponent()]) \
            .create()

    def screenRect(self):
        return self.screen.get_rect()

    def on_events(self, events):
        self.input_handler.update(events)
        if self.should_quit():
            self.quit()

    def should_quit(self):
        return self.input_handler.input_type(QUIT) or self.input_handler.key_down(K_ESCAPE)

    def quit(self):
        self.running = False

    def on_update(self, elapsed_time):
        self.all_sprites.update(elapsed_time / 1000.0)

    def on_render(self):
        self.screen.blit(self.background, (0, 0))
        self.all_sprites.draw(self.screen)
        pygame.display.update()
