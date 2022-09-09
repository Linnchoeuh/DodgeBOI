"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from src.responsive_object.responsive_object_array import *
from include.colors import *

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
        ResponsiveArray.ws = Game.ws
        ResponsiveArray.SetResolution(Game.Res.current)
        ResponsiveArray.LoadConfigFile("./json/menus/main_menu.json")
        Game.pause = False
    ResponsiveArray.CheckResolution(Game.Res.current)
    ResponsiveArray.DisplayObjects()
    # ResponsiveArray.ReloadConfig()
    # title_text = Game.Fonts.title.render("DodgeBOI", True, WHITE)
    # Game.ws.blit(title_text, Game.Res.Manager.Scale.Pos(50,40))
    # buttons.DrawButtons(Game.Mouse, Game.pygame, Game.ws, Game.speed, Game.Res.current)
    # # if PlayButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.GAME
    # if SettingButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.SETTINGS
    # if StatsButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.STATS
    # if QuitButton.Style1(Game, Game.Fonts.button):
    #     Game.launched = False
    # if TutorialButton.Style1(Game, Game.Fonts.button, True):
    #     pass