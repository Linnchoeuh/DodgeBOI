"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
"""

from include.colors import *
import pygame.font
import pygame
import os

FONT_PATH = os.path.join(os.path.dirname(__file__), "../../fonts/")
# FONT_PATH = "/home/lenny/Bureau/projets/perso/python/DodgeBOI/fonts/"


if (not pygame.font.get_init()):
    pygame.font.init()

class Font():
    def __init__(self,
                 font_name: str) -> None:
        self.font_name = font_name
        self.loaded_font: pygame.font.Font = None
        self._last_size: int = 0
        self.antialiasing_default: bool = True
        self.color_default: bool = WHITE

        self.rendered_font: pygame.Surface = None

    def LoadFontSize(self,
                     font_size: int) -> pygame.font.Font:
        if (self.loaded_font == None or self._last_size != font_size):
            self.loaded_font = pygame.font.Font(os.path.join(FONT_PATH, self.font_name), font_size)
        return self.loaded_font

    def RenderText(self,
                   text: str,
                   font_size: int,
                   font_color: tuple = WHITE,
                   font_back_color: tuple = None,
                   font_antialiasing: bool = None):
        self.LoadFontSize(font_size)
        if (font_antialiasing == None):
            font_antialiasing = self.antialiasing_default
        self.rendered_font = self.loaded_font.render(text,
                                                     font_antialiasing,
                                                     font_color,
                                                     font_back_color)
        return self.rendered_font


