"""
settings_menu.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where all settings are
Copyright (c) 2022
"""

from pygame import K_ESCAPE
from include.buttons import *
from src.tools.draw_rect_alpha import *
base_offset = 150

ResumeButton = ButtonClass(0, 0, 0, 0)
ResumeButton.text = "Resume"
BackButton = ButtonClass(0, 0, 0, 0)
BackButton.text = "Back to main menu"

MAX_SPEED = 2.5

def pause_menu(Game):
    ResumeButton.ChangeAreaValue(base_offset + 25, base_offset + 220, 240, 75, Game.Res)
    BackButton.ChangeAreaValue(base_offset + 25, base_offset + 320, 550, 75, Game.Res)
    if (Game.Keyboard.KeyOncePressed(K_ESCAPE)):
        if (Game.pause):
            Game.pause = False
        else:
            Game.pause = True
    if (Game.pause):
        offset = Game.Res.Manager.Scale.Val(base_offset)
        rect = Game.pygame.Rect(offset, offset,
                               Game.Res.current[0] - offset * 2,
                               Game.Res.current[1] - offset * 2)
        draw_rect_alpha(Game.ws, Game.Colors.black, rect, 192)
        title_text = Game.Fonts.title.render("PAUSE", True, Game.Colors.white)
        offset = Game.Res.Manager.Scale.Val(base_offset + 25)
        pos = Game.Res.Manager.Scale.Pos((Game.Res.current[0] - 330) / 2, offset)
        Game.ws.blit(title_text, pos)
        if (ResumeButton.Style1(Game, Game.Fonts.button)):
            Game.pause = False
        if (BackButton.Style1(Game, Game.Fonts.button)):
            Game.Menu.curr = Game.Menu.MENUS.MAIN

def game_menu(Game):
    if (Game.Menu.Changed()):
        Game.Bloc.speed = 1
    Game.Bloc.Run(Game.ws, 1.2, Game.pause)
    if (Game.pause == False):
        Game.Player.Movement(Game.Player.KeyboardInput(Game.Keyboard))
    Game.Player.Display(Game.ws)
    pause_menu(Game)
    if (Game.Bloc.speed < MAX_SPEED):
        Game.Bloc.speed += 0.00005 / Game.speed
    else:
        Game.Bloc.speed = MAX_SPEED
    print(Game.Bloc.speed)
