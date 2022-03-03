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

class MenusStruct():
    def __init__(self):
        self.MAIN = 0
        self.GAME = 1
        self.SETTINGS = 2
        self.STATS = 3

class FontStruct():
    def __init__(self, pygame, ResManager):
        font_path = "./fonts/VCR_OSD_MONO_1.ttf"
        self.debug = pygame.font.Font(font_path, round(ResManager.Scaling(20)))
        font_path = "./fonts/arialbd.ttf"
        self.title = pygame.font.Font(font_path, round(ResManager.Scaling(100)))
        font_path = "./fonts/arialbd.ttf"
        self.button = pygame.font.Font(font_path, round(ResManager.Scaling(60)))

class FramerateStruct():
    def __init__(self):
        self.dt = 0;
        self.speed = 1;
        self.base_fps = 60
        self.fps = 60;

class GameClass():
    def __init__(self, pygame, width, height):
        self.pygame = pygame
        self.launched = True
        self.ws = 0
        self.framerate = FramerateStruct()
        self.Mouse = MouseClass(self.pygame)
        self.Keyboard = KeyboardClass(self.pygame)
        self.Menus = MenusStruct()
        self.prev_menu = -1
        self.curr_menu = self.Menus.MAIN
        self.Colors = ColorPaletteStruct()
        self.ResManager = ResolutionManagerClass(width, height)
        self.Fonts = FontStruct(self.pygame, self.ResManager)
        self.pause = False