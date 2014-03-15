import pygame
from pygame.constants import KEYDOWN, QUIT, KEYUP

__author__ = 'elisegal'


class PyGameInputHandler:
    def __init__(self):
        self.input_state = {}

    def update(self, events):
        self.input_state.pop(QUIT, None)
        for event in events:
            if event.type == KEYDOWN:
                self.__add_event(KEYDOWN, event.key)
            elif event.type == KEYUP:
                self.input_state[KEYDOWN].remove(event.key)
            elif event.type == QUIT:
                self.__add_event(QUIT)

    def __add_event(self, type, value=None):
        if not type in self.input_state:
            self.input_state[type] = []
        self.input_state[type].append(value)

    def key_down(self, key):
        if not KEYDOWN in self.input_state:
            return False
        return key in self.input_state[KEYDOWN]

    def input_type(self, type):
        return type in self.input_state.keys()

