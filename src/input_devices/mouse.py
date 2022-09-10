"""
mouse.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Mouse manager
"""

import pygame.mouse

class MouseButtonClass():
    def __init__(self):
        i: int = 0
        self.count: int = 5
        self._idle = []
        while i < self.count:
            self._idle.append(False)
            i += 1
        self.pressed = self._idle
        self._previous = self._idle
        self.clicked = self._idle

class MouseClass():
    def __init__(self, pygame_mouse: pygame.mouse):
        self.pygame_mouse: pygame.mouse = pygame_mouse
        self.pos: list = self.pygame_mouse.get_pos()
        self.buttons: MouseButtonClass = MouseButtonClass()
        self.disable: bool = False

    def updateStatus(self):
        if (self.disable):
            self.pos = (-500, -500)
            self.buttons.pressed = self.buttons._idle
            self.buttons._previous = self.buttons._idle
        else:
            i: int = 0

            self.pos = self.pygame_mouse.get_pos()
            self.buttons._previous = self.buttons.pressed
            self.buttons.pressed = self.pygame_mouse.get_pressed(self.buttons.count)
            while (i < self.buttons.count):
                self.buttons.clicked[i] = (self.buttons.pressed[i] and \
                                           not self.buttons._previous[i])
                i += 1

