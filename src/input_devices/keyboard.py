"""
keyboard.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Keyboard manager
"""

from typing import Sequence
import pygame.key

class KeyboardKeyClass():
    def __init__(self, pygame_keyboard: pygame.key):
        i: int = 0

        self._idle: Sequence = pygame_keyboard.get_pressed()
        self.pressed: Sequence = pygame_keyboard.get_pressed()
        self._previous: Sequence = pygame_keyboard.get_pressed()

class KeyboardClass():
    def __init__(self, pygame_keyboard: pygame.key):
        self.pygame_keyboard = pygame_keyboard
        self.key = KeyboardKeyClass(self.pygame_keyboard)
        self.disable = False

    def updateStatus(self):
        if (self.disable):
            self.key.pressed = self.key._idle
            self.key._previous = self.key._idle
        else:
            i: int = 0

            self.key._previous = self.key.pressed
            self.key.pressed = self.pygame_keyboard.get_pressed()


    def KeyOncePressed(self,
                       key_id: int,
                       ignore_disabling: bool = False) -> bool:
        if (self.disable and not ignore_disabling):
            return False
        return self.key.pressed[key_id] and not self.key._previous[key_id]
