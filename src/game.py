"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

from mouse import *
from keyboard import *
from fps import *
from game_asset.player import *
from game_asset.map_generator import *
from tools.resolution_manager import *

class ColorPaletteStruct():
    def __init__(self):
        self.black  = (0,	0,	 0)
        self.darker_grey   = (31,	31, 31)
        self.dark_grey   = (63,	63, 63)
        self.grey   = (127,	127, 127)
        self.light_grey   = (191,	191, 191)
        self.white  = (255,	255, 255)
        self.red    = (255,	0,	 0)
        self.green  = (0,	255, 0)
        self.blue   = (0,	0,   255)
        self.yellow = (255,	255, 0)
        self.cyan   = (0,	255, 255)
        self.purple = (255,	0,	 255)

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
        self.Colors = ColorPaletteStruct()
        self.Res = ResolutionClass(width, height)
        self.Fonts = FontStruct(self.pygame, self.Res)
        self.pause = False
        self.Bloc = BlocClass(self.Res)
        self.Player = PlayerClass(self.Res)