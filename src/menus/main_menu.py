"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from src.responsive_object.responsive_object_array import *
from src.responsive_object.object_type.button_object import BUTTON_IS_OVER, BUTTON_PRESSED, BUTTON_CLICKED
from include.colors import *
from pygame.locals import *
from include.tools import find_in

# PlayButton = ButtonClass(0, 0, 0, 0)
# PlayButton.text = "Play"
# SettingButton = ButtonClass(0, 0, 0, 0)
# SettingButton.text = "Settings"
# StatsButton = ButtonClass(0, 0, 0, 0)
# StatsButton.text = "Stats"
# QuitButton = ButtonClass(0, 0, 0, 0)
# QuitButton.text = "Quit"
# TutorialButton = ButtonClass(0, 0, 0, 0)
# TutorialButton.text = "Tutorial"

ResponsiveArray: ResponsiveObjectArray = ResponsiveObjectArray()


def main_menu(Game):
    if (Game.Menu.Changed()):
        ResponsiveArray.ws = Game.Screen.ws
        ResponsiveArray.SetResolution(Game.Screen.win_res.current)
        ResponsiveArray.LoadConfigFile("./json/menus/main_menu.json")
        Game.pause = False
    ResponsiveArray.CheckResolution(Game.Screen.win_res.current)
    ResponsiveArray.DisplayObjects(Game.Mouse, Game.speed)
    buttons: dict = ResponsiveArray.ReturnButtonStatus()

    if find_in(buttons, ["play", BUTTON_CLICKED], False):
        Game.Menu.curr = Game.Menu.MENUS.GAME
    if find_in(buttons, ["settings", BUTTON_CLICKED], False):
        Game.Menu.curr = Game.Menu.MENUS.SETTINGS
    if find_in(buttons, ["stats", BUTTON_CLICKED], False):
        Game.Menu.curr = Game.Menu.MENUS.STATS
    if find_in(buttons, ["exit", BUTTON_CLICKED], False):
        Game.launched = False
    if find_in(buttons, ["tutorial", BUTTON_CLICKED], False):
        pass