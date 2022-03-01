"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from tools.button import *

init = True

PlayButton = ButtonClass(0, 0, 0, 0)
PlayButton.text = "Play"
SettingButton = ButtonClass(0, 0, 0, 0)
SettingButton.text = "Setting"
StatsButton = ButtonClass(0, 0, 0, 0)
StatsButton.text = "Stats"
QuitButton = ButtonClass(0, 0, 0, 0)
QuitButton.text = "Quit"

def main_menu(Game):
    x = Game.ResManager.Scaling(150)
    y = Game.ResManager.Scaling(250)
    w = Game.ResManager.Scaling(130)
    h = Game.ResManager.Scaling(75)
    PlayButton.ChangeAreaValue(x, y, w, h)
    y = Game.ResManager.Scaling(350)
    w = Game.ResManager.Scaling(210)
    SettingButton.ChangeAreaValue(x, y, w, h)
    y = Game.ResManager.Scaling(450)
    w = Game.ResManager.Scaling(150)
    StatsButton.ChangeAreaValue(x, y, w, h)
    y = Game.ResManager.Scaling(550)
    w = Game.ResManager.Scaling(130)
    QuitButton.ChangeAreaValue(x, y, w, h)
    title_text = Game.Fonts.title.render("DodgeBOI", True, Game.Colors.white)
    Game.ws.blit(title_text, Game.ResManager.PosScaling(50,40))
    if PlayButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.GAME
    if SettingButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.SETTING
    if StatsButton.Style1(Game, Game.Fonts.button):
        Game.curr_menu = Game.Menus.STATS
    if QuitButton.Style1(Game, Game.Fonts.button):
        Game.launched = False