"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from include.buttons import *
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

buttons = ButtonArray()

def main_menu(Game):
    if (Game.Menu.Changed()):
        buttons.LoadConfig("./json/menus/main_menu_buttons.json", Game.Fonts.button)
        # PlayButton.ChangeAreaValue(150, 250, 130, 75, Game.Res)
        # SettingButton.ChangeAreaValue(150, 350, 240, 75, Game.Res)
        # StatsButton.ChangeAreaValue(150, 450, 150, 75, Game.Res)
        # QuitButton.ChangeAreaValue(150, 550, 130, 75, Game.Res)
        # TutorialButton.ChangeAreaValue(950, 550, 213, 75, Game.Res)
        Game.pause = False
    title_text = Game.Fonts.title.render("DodgeBOI", True, WHITE)
    Game.ws.blit(title_text, Game.Res.Manager.Scale.Pos(50,40))
    buttons.DrawButtons(Game.Mouse, Game.pygame, Game.ws, Game.speed, Game.Res.current)
    # if PlayButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.GAME
    # if SettingButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.SETTINGS
    # if StatsButton.Style1(Game, Game.Fonts.button):
    #     Game.Menu.curr = Game.Menu.MENUS.STATS
    # if QuitButton.Style1(Game, Game.Fonts.button):
    #     Game.launched = False
    # if TutorialButton.Style1(Game, Game.Fonts.button, True):
    #     pass