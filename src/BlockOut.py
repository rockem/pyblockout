from component import UserInputComponent, ClampComponent, BallPhysicsComponent, SimpleMoveComponent
from game import SpriteGameObject

from key import SPACE
from rect import Rect
from sprite import SpriteFactory


__author__ = 'eli.segal'


class SpriteGameObjectCreator:
    def __init__(self, sprite):
        self._sprite = sprite

    def components(self, components):
        self.components = components
        return self

    def batch(self, batch):
        self.batch = batch
        return self

    def create_at(self, x, y):
        go = self.__create_game_object()
        go.x, go.y = x, y
        return go

    def __create_game_object(self):
        go = SpriteGameObject(self._sprite)
        go.components = self.components
        self.batch.append(go)
        return go

    def create(self):
        return self.__create_game_object()


class BlockOut:
    def __init__(self, game_factory, input_handler):
        self.game_factory = game_factory
        self.input_handler = input_handler
        self.background = self.create_background()
        self.game_objects = []
        self.sprites_batch = self.game_factory.create_batch()
        self.sprite_factory = SpriteFactory(self.sprites_batch)
        self.createAllSprites()

    def create_background(self):
        return self.game_factory.load_image('background.png')

    def createAllSprites(self):
        self.pack = SpriteGameObjectCreator(self.sprite_factory.create_pack_sprite()) \
            .components([UserInputComponent(self.input_handler), SimpleMoveComponent(), ClampComponent(self.screenRect())]) \
            .batch(self.game_objects) \
            .create_at(self.screenRect().width / 2, 20)

        self.ball_physics = BallPhysicsComponent(self.pack, self.screenRect())
        self.ball = SpriteGameObjectCreator(self.sprite_factory.create_ball_sprite()) \
            .batch(self.game_objects) \
            .components([self.ball_physics, SimpleMoveComponent(), ClampComponent(self.screenRect())]) \
            .create()

    def screenRect(self):
        return Rect(0, 0, self.game_factory.screen.width, self.game_factory.screen.height)

    def on_update(self, elapsed_time):
        if self.input_handler.key_down(SPACE):
            self.ball_physics.play()
        self.update_game_objects(elapsed_time)
        # self.detect_collisions()

    def update_game_objects(self, elapsed_time):
        for go in self.game_objects:
            go.update(elapsed_time)

    def on_render(self):
        self.background.blit(self.game_factory.screen.width / 2, self.game_factory.screen.height / 2)
        self.sprites_batch.draw()

    def detect_collisions(self):
        for i in xrange(len(self.game_objects)):
            for j in xrange(i + 1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    def create_sprite(self, image_name):
        pass
