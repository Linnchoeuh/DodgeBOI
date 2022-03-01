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
import os.path as path
# import time
# import random
# import ctypes
# import sys

from game import *
from menus.main_menu import *

pygame.init()
pygame.font.init()

pygame.display.set_caption("DodgeBOI")

Game = GameClass(pygame, path)
Game.ResManager.ChangeRes(1280, 720)

clock = pygame.time.Clock()
Game.ws = pygame.display.set_mode(Game.ResManager.Res.current)

def menu_Interaction(Game):
    if Game.menu == Game.Menus.MAIN:
        main_menu(Game)

launched = True
while launched: #Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    Game.ws.fill(Game.Colors.black)
    Game.Mouse.updateStatus()
    Game.Keyboard.updateStatus()
    Game.ResManager.ToggleFullscreen(Game.pygame, Game.Keyboard, Game)
    menu_Interaction(Game)
    pygame.display.flip()
    dt = clock.tick(60)/1000