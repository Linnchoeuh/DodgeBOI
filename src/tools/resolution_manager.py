"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

import pygame

WIDTH = 0
HEIGHT = 1

class ScalerClass():
    def __init__(self, scaling_coef):
        self.scaling_coef = scaling_coef

    def Val(self, value):
        return (value * self.scaling_coef)

    def Pos(self, x, y):
        return (x * self.scaling_coef,
                y * self.scaling_coef)

    def Area(self, x, y, w, h):
        return (x * self.scaling_coef,
                y * self.scaling_coef,
                w * self.scaling_coef,
                h * self.scaling_coef)

class ResolutionManagerClass():
    def __init__(self, res):
        self.scaling_coef = res.current[HEIGHT] / res.native[HEIGHT]
        self.fullscreen = False
        self.res = res.current
        self.Scale = ScalerClass(self.scaling_coef)

    def ToggleFullscreen(self, Keyboard, Game, key_trigger):
        if (Keyboard.KeyOncePressed(key_trigger)):
            if self.fullscreen == True:
                self.fullscreen = False
                Game.ws = pygame.display.set_mode(self.res)
            else:
                self.fullscreen = True
                Game.ws = pygame.display.set_mode(self.res, pygame.FULLSCREEN)

class ResolutionClass():
    def __init__(self, width, height):
        self.native = (1280, 720)
        self.current = [width, height]
        self.Manager = ResolutionManagerClass(self)