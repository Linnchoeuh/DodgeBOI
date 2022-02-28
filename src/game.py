"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

from mouse import *
from keyboard import *

COLOR_PALETTE = {"black"	: (0,	0,	0),
                 "white"	: (255,	255,255),
                 "red" 		: (255,	0,	0),
                 "green" 	: (0,	255,0),
                 "blue" 	: (0,	0,	255),
                 "yellow"	: (255,	255,0),
                 "cyan" 	: (0,	255,255),
                 "purple"	: (255,	0,	255)}

class Menus():
    def __init__(self):
        self.MAIN = 0
        self.GAME = 1
        self.SETTING = 2

class GameClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.Mouse = MouseClass(self.pygame)
        self.Keyboard = KeyboardClass(self.pygame)
        self.Menus = Menus()
        self.menu = self.Menus.MAIN
        self.colors = COLOR_PALETTE