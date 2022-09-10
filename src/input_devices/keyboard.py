"""
keyboard.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Keyboard manager
"""

import pygame.key

class KeyboardKeyClass():
    def __init__(self, pygame_keyboard: pygame.key):
        i: int = 0

        self.pressed: list = pygame_keyboard.get_pressed()
        self.clicked: list = []
        self._idle: list = []
        self._previous: list = []
        self.count = len(self.pressed)
        while (i < self.count):
            self.clicked.append(False)
            self._idle.append(False)
            self._previous.append(False)
            i += 1

class KeyboardClass():
    def __init__(self, pygame_keyboard: pygame.key):
        self.pygame_keyboard = pygame_keyboard
        self.key = KeyboardKeyClass(self.pygame_keyboard)
        self.disable = False

    def updateStatus(self):
        if (self.disable):
            self.key.pressed = self.key._idle
            self.key.clicked = self.key._idle
            self.key._previous = self.key._idle
        else:
            i: int = 0

            self.key._previous = self.key.pressed
            self.key.pressed = self.pygame_keyboard.get_pressed()
            while (i < self.key.count):
                self.key.clicked[i] = (self.key.pressed[i] and \
                                       not self.key._previous[i])
                i += 1
