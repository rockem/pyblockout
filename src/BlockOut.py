from component import UserInputComponent, ClampComponent, BallPhysicsComponent, SimpleMoveComponent, \
    SoundOnCollisionComponent
from game import SpriteGameObjectCreator, BlocksGameObjectCreator

from key import SPACE
from sound import PACK, BLOCK


__author__ = 'eli.segal'


class BlockOut:
    def __init__(self):
        self.game_factory = None
        self.input_handler = None
        self.layout_provider = None
        self.sprite_factory = None
        self.screen_rect = None
        self.sound_factory = None

    def init(self):
        self.game_objects = []
        self.background = self.create_background()
        self.win_message = self.game_factory.load_image('win_message.png')
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
            [UserInputComponent(self.input_handler), SimpleMoveComponent(), ClampComponent(self.screen_rect), SoundOnCollisionComponent(PACK, self.sound_factory)]) \
            .create_at(self.screen_rect.width / 2, 20)
        self.game_objects.append(self.pack)

    def create_ball(self):
        self.ball_physics = BallPhysicsComponent(self.pack, self.screen_rect)
        self.ball = SpriteGameObjectCreator(self.sprite_factory.create_ball_sprite()) \
            .components([self.ball_physics, SimpleMoveComponent(), ClampComponent(self.screen_rect)]) \
            .create()
        self.game_objects.append(self.ball)

    def create_blocks(self):
        self.blocks = BlocksGameObjectCreator() \
            .sprite_factory(self.sprite_factory) \
            .sound_factory(self.sound_factory) \
            .create_at(self.screen_rect.center)
        self.game_objects.append(self.blocks)

    def on_update(self, elapsed_time):
        if self.input_handler.key_down(SPACE):
            self.ball_physics.play()
        self.update_game_objects(elapsed_time)
        self.update_layout_if_needed()
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

    def update_layout_if_needed(self):
        if self.blocks.num_of_blocks == 0:
            if not self.layout_provider.current_is_last():
                self.blocks.update_layout(self.layout_provider.get_next_layout())
            self.ball_physics.stay()

    def detect_collisions(self):
        for i in xrange(len(self.game_objects)):
            for j in xrange(i + 1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                if obj_1.active and obj_2.active:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

    def on_render(self):
        self.background.blit(0, 0)
        if self.layout_provider.current_is_last() and self.blocks.num_of_blocks == 0:
            self.win_message.blit(self.screen_rect.width / 2 - self.win_message.width / 2, self.screen_rect.height / 2)
        self.sprite_factory.draw()

