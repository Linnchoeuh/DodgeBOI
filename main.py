"""
main.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Main program
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

from include.colors import *
from src.game.game_struct import *
from src.menus.main_menu import *
from src.menus.settings_menu import *
from src.menus.stats_menu import *
from src.menus.game_menu import *
from src.effect.transition import *

pygame.init()
pygame.font.init()

pygame.display.set_caption("DodgeBOI")

Game = GameClass(pygame, 1280, 720)

Transition = TransitionClass(Game)
clock = pygame.time.Clock()
Game.Screen.ws = pygame.display.set_mode(Game.Screen.win_res.current,
                                         pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF)

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
    Game.Screen.ToggleFullscreen(Game.Keyboard, K_F11)
    Game.Screen.ResolutionChangerChecker()
    Game.Screen.ws.fill(DARKER_GREY)
    Game.Mouse.updateStatus()
    Game.Keyboard.updateStatus()
    menu_Interaction(Game)
    Game.Menu.curr = Transition.Check(Game)
    Game.speed = Game.fps.update_fps(clock)
    Game.fps.show_fps(Game.Screen.ws, Game.Screen.Scaler.Pos(5, 5))
    pygame.display.flip()

pygame.display.quit()