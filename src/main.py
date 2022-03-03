"""
main.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main program
Copyright (c) 2022
"""

try:
    import pygame
    from pygame.locals import *
except:
    print("Pygame not found.")
    exit()
# import time
# import random
# import ctypes
# import sys

from game import *
from menus.main_menu import *
from menus.settings_menu import *
from menus.stats_menu import *
from menus.game_menu import *
from effect.transition import *

pygame.init()
pygame.font.init()

pygame.display.set_caption("DodgeBOI")

Game = GameClass(pygame, 1280, 720)

Transition = TransitionClass(Game)

clock = pygame.time.Clock()
Game.ws = pygame.display.set_mode(Game.Res.current)

def menu_Interaction(Game):
    match Game.Menu.curr:
        case Game.Menu.MENUS.MAIN:
            main_menu(Game)
        case Game.Menu.MENUS.GAME:
            game_menu(Game)
        case Game.Menu.MENUS.SETTINGS:
            settings_menu(Game)
        case Game.Menu.MENUS.STATS:
            stats_menu(Game)

while Game.launched: #Pour fermer la fenêtre
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            Game.launched = False
    Game.ws.fill(Game.Colors.darker_grey)
    Game.Mouse.updateStatus()
    Game.Keyboard.updateStatus()
    Game.Res.Manager.ToggleFullscreen(Game.Keyboard, Game, K_F11)
    menu_Interaction(Game)
    Game.Menu.curr = Transition.Check(Game)
    Game.speed = Game.fps.update_fps(clock)
    Game.fps.show_fps(Game.ws, Game.Res.Manager.Scale.Pos(5, 5), Game.Fonts.debug)
    pygame.display.flip()

