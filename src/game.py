from component import BlockCollisionComponent
from event import EventHook
from rect import Rect

__author__ = 'elisegal'


class GameObject(object):

    def __init__(self):
        self._x = self._y = 0
        self.x_velocity = self.y_velocity = 0
        self.new_objects = []
        self._components = []
        self.alive = True
        self.on_collision = EventHook()

    def set_components(self, value):
        self._components = value
        for c in self._components:
            c.game_object = self

    components = property(lambda self: self._components, set_components)

    def update(self, elapsed_time):
        for c in self.components:
            c.update(elapsed_time)

    x = property(
        lambda self: self._get_x(),
        lambda self, x: self._set_x(x)
    )

    def _get_x(self):
        return self._x

    def _set_x(self, value):
        self._x = value

    y = property(
        lambda self: self._get_y(),
        lambda self, y: self._set_y(y)
    )

    def _get_y(self):
        return self._y

    def _set_y(self, value):
        self._y = value

    def _set_position(self, value):
        self.x = value[0]
        self.y = value[1]

    def _get_position(self):
        return self.x, self.y

    position = property(_get_position, _set_position)

    def get_rect(self):
        return Rect(0, 0, 0, 0)

    def handle_collision_with(self, other_obj):
        self.on_collision.fire(other_obj)


class SpriteGameObject(GameObject):
    def __init__(self, sprite):
        super(SpriteGameObject, self).__init__()
        self._sprite = sprite

    def get_rect(self):
        r = Rect(0, 0, self._sprite.width, self._sprite.height)
        r.center = (self.x, self.y)
        return r

    def _get_x(self):
        return self._sprite.x

    def _set_x(self, value):
        self._sprite.x = value

    def _get_y(self):
        return self._sprite.y

    def _set_y(self, value):
        self._sprite.y = value

    def collides_with(self, other_obj):
        return self.get_rect().intersects(other_obj.get_rect())

    def update(self, elapsed_time):
        super(SpriteGameObject, self).update(elapsed_time)
        if not self.alive:
            self._sprite.batch = None


class GameObjectCreator:
    def components(self, components):
        self._components = components
        return self

    def create_at(self, *pos):
        go = self._create_game_object()
        if type(pos[0]) == tuple:
            go.x, go.y = pos[0][0], pos[0][1]
        else:
            go.x, go.y = pos[0], pos[1]
        return go

    def _create_game_object(self):
        pass

    def create(self):
        return self._create_game_object()


class SpriteGameObjectCreator(GameObjectCreator):

    def __init__(self, sprite):
        self._sprite = sprite

    def _create_game_object(self):
        go = SpriteGameObject(self._sprite)
        go.components = self._components
        return go


class BlocksGameObject(GameObject):
    VERTICAL_GAP = 15
    HORIZONTAL_GAP = 20

    def __init__(self):
        super(BlocksGameObject, self).__init__()
        self.sprite_factory = None
        self.num_of_blocks = 0

    def update_layout(self, layout):
        self._layout = layout
        for i in range(len(layout)):
            for j in range(len(layout[i])):
                self.create_block_sprite(i, j)

    def create_block_sprite(self, i, j):
        sprite_type = self._layout[i][j]
        if sprite_type > 0:
            sprite = SpriteGameObjectCreator(self.create_sprite_of_type(sprite_type)) \
                .components([BlockCollisionComponent()]) \
                .create()
            sprite.position = self.get_position_for(sprite, j, i)
            sprite.on_collision += self.on_block_collision
            self.new_objects.append(sprite)
            self.num_of_blocks += 1

    def create_sprite_of_type(self, type):
        if type == 1:
            return self.sprite_factory.create_white_block()
        return self.sprite_factory.create_red_block()

    def get_position_for(self, sprite_go, x, y):
        return self.x + (x - self.anchor_block()[0]) * (sprite_go.get_rect().width + self.HORIZONTAL_GAP), \
            self.y - (y - self.anchor_block()[1]) * (sprite_go.get_rect().height + self.VERTICAL_GAP)

    def anchor_block(self):
        return len(self._layout[0]) / 2, len(self._layout)

    def on_block_collision(self, other_object):
        self.num_of_blocks -= 1

    def collides_with(self, other_obj):
        return False


class BlocksGameObjectCreator(GameObjectCreator):
    def sprite_factory(self, factory):
        self._sprite_factory = factory
        return self

    def _create_game_object(self):
        game_object = BlocksGameObject()
        game_object.sprite_factory = self._sprite_factory
        return game_object


