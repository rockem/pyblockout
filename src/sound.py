import pyglet


class PygletSoundFactory:

    def __init__(self):
        self._background = pyglet.resource.media('sillylovesongs.wav', streaming=False)

    def play_background(self):
        self._background.play()
