"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

import pygame

from include.input_devices import *

from src.fps import *
from src.game_asset.player import *
from src.game_asset.map_generator import *
from src.tools.resolution_manager import *

class MenusStruct():
    def __init__(self):
        self.MAIN = 0
        self.GAME = 1
        self.SETTINGS = 2
        self.STATS = 3

class MenuManager():
    def __init__(self):
        self.MENUS = MenusStruct()
        self.prev = -1
        self.curr = self.MENUS.MAIN

    def Changed(self):
        state = (self.curr != self.prev)
        if (state):
            self.prev = self.curr
        return (state)

class GameClass():
    def __init__(self, pygame_class, width, height):
        self.pygame: pygame = pygame_class
        self.launched = True
        self.ws = None
        self.fps = FpsClass()
        self.speed = 1
        self.Menu = MenuManager()
        self.Mouse = MouseClass(self.pygame.mouse)
        self.Keyboard = KeyboardClass(self.pygame.key)
        self.Res = ResolutionClass(width, height)
        self.pause = False
        self.Bloc = BlocClass(self.Res)
        self.Player = PlayerClass(self.Res)