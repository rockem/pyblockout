import pyglet


PACK = "pack"
WALL = "wall"
BLOCK = "block"


class SoundFactory:
    def play_efx(self, sound_name):
        pass


class PygletSoundFactory(SoundFactory):

    def __init__(self):
        self._music = pyglet.resource.media('sillylovesongs.wav', streaming=False)
        self._efx = {
            PACK: pyglet.resource.media('pack_sound.wav', streaming=False),
            WALL: pyglet.resource.media('wall_sound.wav', streaming=False),
            BLOCK: pyglet.resource.media('block_sound.wav', streaming=False)
        }
        self._set_music_volume(80)
        self._set_efx_volume(100)

    def _set_music_volume(self, volume):
        self._music.volume = volume / 100

    def _set_efx_volume(self, volume):
        for e in self._efx:
            self._efx[e].volume = volume / 100

    def play_background(self):
        self._music.play()

    def play_efx(self, sound_name):
        self._efx[sound_name].play()