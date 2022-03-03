"""
settings_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where all settings are
Copyright (c) 2022
"""

from tools.button import *

BackButton = ButtonClass(0, 0, 0, 0)
BackButton.text = "Back"

def settings_menu(Game):
    if (Game.curr_menu != Game.prev_menu):
        BackButton.ChangeAreaValue(0, 0, 150, 75, Game.ResManager)
        Game.prev_menu = Game.curr_menu
    if BackButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.MAIN
