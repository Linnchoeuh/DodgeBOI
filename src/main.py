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
from pygame.locals import *
# import time
# import random
# import ctypes
# import sys
# import os

from game import *

pygame.init()
pygame.font.init()
pygame.key.set_repeat(10, 20)

pygame.display.set_caption("DodgeBOI")

clock = pygame.time.Clock()
ws = pygame.display.set_mode((1280, 720))

Game = GameClass(pygame)
launched = True
while launched: #Pour fermer la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    ws.fill(Game.colors["black"])
    Game.Mouse.updateStatus()
    Game.Keyboard.updateStatus()
    pygame.display.flip()
    dt = clock.tick(60)/1000