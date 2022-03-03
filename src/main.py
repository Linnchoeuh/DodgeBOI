"""
main.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main program
Copyright (c) 2022
"""

try:
    import pygame
except:
    print("Pygame not found.")
    exit()
from telnetlib import GA
from pygame.locals import *
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
Game.ws = pygame.display.set_mode(Game.ResManager.Res.current)

def menu_Interaction(Game):
    match Game.curr_menu:
        case Game.Menus.MAIN:
            main_menu(Game)
        case Game.Menus.GAME:
            game_menu(Game)
        case Game.Menus.SETTINGS:
            settings_menu(Game)
        case Game.Menus.STATS:
            stats_menu(Game)

while Game.launched: #Pour fermer la fenêtre
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            Game.launched = False
    Game.ws.fill(Game.Colors.darker_grey)
    Game.Mouse.updateStatus()
    Game.Keyboard.updateStatus()
    Game.ResManager.ToggleFullscreen(Game.pygame, Game.Keyboard, Game, K_F11)
    menu_Interaction(Game)
    Game.curr_menu = Transition.Check(Game)
    pygame.display.flip()
    Game.framerate.dt = clock.tick(Game.framerate.fps)/1000
    Game.framerate.speed = Game.framerate.fps / Game.framerate.base_fps