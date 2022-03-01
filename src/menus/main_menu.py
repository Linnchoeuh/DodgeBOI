"""
main_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main menu
Copyright (c) 2022
"""

from tools.button import *

PlayButton = ButtonClass(10,10,100,100)
PlayButton.text = "Play"

def main_menu(Game):
    title_text = Game.Fonts.title.render("DodgeBOI", True, Game.Colors.white)
    Game.ws.blit(title_text, (50,40))
    # print(Game.Mouse.pos)
    print(PlayButton.CheckArea(Game.Mouse))