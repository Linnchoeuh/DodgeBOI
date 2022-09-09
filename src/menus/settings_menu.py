"""
settings_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where all settings are
Copyright (c) 2022
"""

from include.buttons import *

BackButton = ButtonClass(0, 0, 0, 0)
BackButton.text = "Back"

def settings_menu(Game):
    if (Game.Menu.Changed()):
        BackButton.ChangeAreaValue(0, 0, 150, 75, Game.Res)
    if BackButton.Style1(Game, Game.Fonts.button):
        Game.Menu.curr = Game.Menu.MENUS.MAIN
