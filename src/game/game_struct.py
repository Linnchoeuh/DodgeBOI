"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

from src.mouse import *
from src.keyboard import *
from src.fps import *
from src.game_asset.player import *
from src.game_asset.map_generator import *
from src.tools.resolution_manager import *

class FontStruct():
    def __init__(self, pygame, Res):
        VCR_OSD_MONO_1 = "VCR_OSD_MONO_1.ttf"
        ARIALBD = "arialbd.ttf"
        try:
            font_path = "./fonts/"
            self.debug = pygame.font.Font(font_path + VCR_OSD_MONO_1, round(Res.Manager.Scale.Val(20)))
        except:
            font_path = "./../fonts/"
            self.debug = pygame.font.Font(font_path + VCR_OSD_MONO_1, round(Res.Manager.Scale.Val(20)))
        self.title = pygame.font.Font(font_path + ARIALBD, round(Res.Manager.Scale.Val(100)))
        self.button = pygame.font.Font(font_path + ARIALBD, round(Res.Manager.Scale.Val(60)))

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
    def __init__(self, pygame, width, height):
        self.pygame = pygame
        self.launched = True
        self.ws = 0
        self.fps = FpsClass()
        self.speed = 1
        self.Menu = MenuManager()
        self.Mouse = MouseClass(self.pygame)
        self.Keyboard = KeyboardClass(self.pygame)
        self.Res = ResolutionClass(width, height)
        self.Fonts = FontStruct(self.pygame, self.Res)
        self.pause = False
        self.Bloc = BlocClass(self.Res)
        self.Player = PlayerClass(self.Res)