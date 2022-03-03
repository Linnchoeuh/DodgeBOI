"""
settings_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where all settings are
Copyright (c) 2022
"""

from pygame import K_ESCAPE
from tools.button import *
from tools.draw_rect_alpha import *
base_offset = 150

ResumeButton = ButtonClass(0, 0, 0, 0)
ResumeButton.text = "Resume"
BackButton = ButtonClass(0, 0, 0, 0)
BackButton.text = "Back to main menu"



def pause_menu(Game):
    if (Game.curr_menu != Game.prev_menu):
        ResumeButton.ChangeAreaValue(base_offset + 25, base_offset + 220, 240, 75, Game.ResManager)
        BackButton.ChangeAreaValue(base_offset + 25, base_offset + 320, 550, 75, Game.ResManager)
        Game.prev_menu = Game.curr_menu
    if (Game.Keyboard.key.curr[K_ESCAPE] and Game.Keyboard.key.prev[K_ESCAPE] == False):
        if (Game.pause):
            Game.pause = False
        else:
            Game.pause = True
    if (Game.pause):
        offset = Game.ResManager.Scaling(base_offset)
        rect = Game.pygame.Rect(offset, offset,
                               Game.ResManager.Res.current[0] - offset * 2,
                               Game.ResManager.Res.current[1] - offset * 2)
        draw_rect_alpha(Game.ws, Game.Colors.black, rect, 192)
        title_text = Game.Fonts.title.render("PAUSE", True, Game.Colors.white)
        offset = Game.ResManager.Scaling(base_offset + 25)
        pos = Game.ResManager.PosScaling((Game.ResManager.Res.current[0] - 330) / 2, offset)
        Game.ws.blit(title_text, pos)
        if (ResumeButton.Style1(Game, Game.Fonts.button)):
            Game.pause = False
        if (BackButton.Style1(Game, Game.Fonts.button)):
            Game.curr_menu = Game.Menus.MAIN

def game_menu(Game):
    pause_menu(Game)
