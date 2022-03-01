"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

from mouse import *
from keyboard import *
from tools.resolution_manager import *

class ColorPaletteStruct():
    def __init__(self):
        self.black  = (0,	0,	 0)
        self.white  = (255,	255, 255)
        self.red    = (255,	0,	 0)
        self.green  = (0,	255, 0)
        self.blue   = (0,	0,   255)
        self.yellow = (255,	255, 0)
        self.cyan   = (0,	255, 255)
        self.purple = (255,	0,	 255)

class MenusStruct():
    def __init__(self):
        self.MAIN = 0
        self.GAME = 1
        self.SETTING = 2

class FontStruct():
    def __init__(self, pygame, ResManager):
        font_path = "./fonts/VCR_OSD_MONO_1.ttf"
        self.debug = pygame.font.Font(font_path, ResManager.ResScaling(20))
        font_path = "./fonts/arialbd.ttf"
        self.title = pygame.font.Font(font_path, ResManager.ResScaling(100))

class GameClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.ws = 0
        self.Mouse = MouseClass(self.pygame)
        self.Keyboard = KeyboardClass(self.pygame)
        self.Menus = MenusStruct()
        self.menu = self.Menus.MAIN
        self.Colors = ColorPaletteStruct()
        self.ResManager = ResolutionManagerClass(1280, 720)
        self.Fonts = FontStruct(self.pygame, self.ResManager)