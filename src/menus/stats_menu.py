"""
stats_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where the stats shows up
Copyright (c) 2022
"""

from tools.button import *

BackButton = ButtonClass(0, 0, 0, 0)
BackButton.text = "Back"

def stats_menu(Game):
    if (Game.Menu.Changed()):
        BackButton.ChangeAreaValue(0, 0, 150, 75, Game.Res)
    title_text = Game.Fonts.title.render("STATS", True, Game.Colors.white)
    pos = Game.Res.Manager.Scale.Pos((Game.Res.current[0] - 310) / 2, 40)
    Game.ws.blit(title_text, pos)
    if BackButton.Style1(Game, Game.Fonts.button):
        Game.Menu.curr = Game.Menu.MENUS.MAIN
