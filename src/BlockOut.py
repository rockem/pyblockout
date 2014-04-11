from component import UserInputComponent, ClampComponent, BallPhysicsComponent, SimpleMoveComponent
from game import SpriteGameObjectCreator, BlocksGameObjectCreator

from key import SPACE
from rect import Rect
from sprite import SpriteFactory


__author__ = 'eli.segal'


class BlockOut:
    def __init__(self, game_factory, input_handler, layout_provider):
        self.game_factory = game_factory
        self.input_handler = input_handler
        self.layout_provider = layout_provider
        self.background = self.create_background()
        self.game_objects = []
        self.sprites_batch = self.game_factory.create_batch()
        self.sprite_factory = SpriteFactory(self.sprites_batch)
        self.createAllSprites()

    def create_background(self):
        return self.game_factory.load_image('background.png')

    def createAllSprites(self):
        self.create_pack()
        self.create_ball()
        self.create_blocks()

    def create_pack(self):
        self.pack = SpriteGameObjectCreator(self.sprite_factory.create_pack_sprite()) \
            .components(
            [UserInputComponent(self.input_handler), SimpleMoveComponent(), ClampComponent(self.screenRect())]) \
            .create_at(self.screenRect().width / 2, 20)
        self.game_objects.append(self.pack)

    def create_ball(self):
        self.ball_physics = BallPhysicsComponent(self.pack, self.screenRect())
        self.ball = SpriteGameObjectCreator(self.sprite_factory.create_ball_sprite()) \
            .components([self.ball_physics, SimpleMoveComponent(), ClampComponent(self.screenRect())]) \
            .create()
        self.game_objects.append(self.ball)

    def create_blocks(self):
        self.blocks = BlocksGameObjectCreator() \
            .sprite_factory(self.sprite_factory) \
            .create_at(self.screenRect().center)
        self.game_objects.append(self.blocks)
        self.blocks.update_layout(self.layout_provider.current_layout())

    def screenRect(self):
        return Rect(0, 0, self.game_factory.screen.width, self.game_factory.screen.height)

    def on_update(self, elapsed_time):
        if self.input_handler.key_down(SPACE):
            self.ball_physics.play()
        self.update_game_objects(elapsed_time)
        self.detect_collisions()

    def update_game_objects(self, elapsed_time):
        to_add = []
        to_remove = []
        for go in self.game_objects:
            go.update(elapsed_time)
            self.update_added_and_removed(go, to_add, to_remove)

        self.game_objects = [v for v in self.game_objects if v not in to_remove]
        self.game_objects.extend(to_add)

    def update_added_and_removed(self, go, to_add, to_remove):
        if go.alive:
            to_add.extend(go.new_objects)
            go.new_objects = []
        else:
            to_remove.append(go)

    def detect_collisions(self):
        for i in xrange(len(self.game_objects)):
            for j in xrange(i + 1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    def on_render(self):
        self.background.blit(self.game_factory.screen.width / 2, self.game_factory.screen.height / 2)
        self.sprites_batch.draw()
