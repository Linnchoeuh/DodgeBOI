"""
mouse.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Mouse manager
Copyright (c) 2022
"""
import pygame

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
    def __init__(self, pygame):
        self.pygame = pygame
        self.pos = self.pygame.mouse.get_pos()
        self.buttons = MouseButtonClass()
        self.disable = False

    def updateStatus(self):
        if (self.disable == False):
            self.pos = self.pygame.mouse.get_pos()
            self.buttons._previous = self.buttons.pressed
            self.buttons.pressed = self.pygame.mouse.get_pressed(self.buttons.count)
            # for i in self.count:
                # self.button.clicked[i] = (self.button.pressed[i] and not self.button._previous[i])
        else:
            self.pos = (-500, -500)
            self.buttons.pressed = self.buttons._idle
            self.buttons._previous = self.buttons._idle

