"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from tools.button import *

PlayButton = ButtonClass(0, 0, 0, 0)
PlayButton.text = "Play"
SettingButton = ButtonClass(0, 0, 0, 0)
SettingButton.text = "Settings"
StatsButton = ButtonClass(0, 0, 0, 0)
StatsButton.text = "Stats"
QuitButton = ButtonClass(0, 0, 0, 0)
QuitButton.text = "Quit"

def main_menu(Game):
    if (Game.curr_menu != Game.prev_menu):
        PlayButton.ChangeAreaValue(150, 250, 130, 75, Game.ResManager)
        SettingButton.ChangeAreaValue(150, 350, 240, 75, Game.ResManager)
        StatsButton.ChangeAreaValue(150, 450, 150, 75, Game.ResManager)
        QuitButton.ChangeAreaValue(150, 550, 130, 75, Game.ResManager)
        Game.pause = False
        Game.prev_menu = Game.curr_menu
    title_text = Game.Fonts.title.render("DodgeBOI", True, Game.Colors.white)
    Game.ws.blit(title_text, Game.ResManager.PosScaling(50,40))
    if PlayButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.GAME
    if SettingButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.SETTINGS
    if StatsButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.STATS
    if QuitButton.Style1(Game, Game.Fonts.button):
        Game.launched = False