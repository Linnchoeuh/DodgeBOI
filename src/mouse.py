"""
mouse.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Mouse manager
Copyright (c) 2022
"""

class MouseButtonClass():
    def __init__(self, pygame):
        self.count = 5
        self.prev = pygame.mouse.get_pressed(self.count)
        self.curr = pygame.mouse.get_pressed(self.count)

class MouseClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.pos = self.pygame.mouse.get_pos()
        self.buttons = MouseButtonClass(self.pygame)

    def updateStatus(self):
        self.pos = self.pygame.mouse.get_pos()
        self.buttons.prev = self.buttons.curr;
        self.buttons.curr = self.pygame.mouse.get_pressed(self.buttons.count)
