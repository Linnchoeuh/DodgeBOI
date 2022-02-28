"""
keyboard.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Keyboard manager
Copyright (c) 2022
"""

class KeyboardButtonClass():
    def __init__(self, pygame):
        self.prev = pygame.key.get_pressed()
        self.curr = pygame.key.get_pressed()

class KeyboardClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.buttons = KeyboardButtonClass(self.pygame)

    def updateStatus(self):
        self.pos = self.pygame.mouse.get_pos()
        self.buttons.prev = self.buttons.curr;
        self.buttons.curr = self.pygame.key.get_pressed()
