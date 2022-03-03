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
        self.nothing = pygame.mouse.get_pressed(self.count)

class MouseClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.pos = self.pygame.mouse.get_pos()
        self.buttons = MouseButtonClass(self.pygame)
        self.disable = False

    def updateStatus(self):
        if (self.disable == False):
            self.pos = self.pygame.mouse.get_pos()
            self.buttons.prev = self.buttons.curr
            self.buttons.curr = self.pygame.mouse.get_pressed(self.buttons.count)
        else:
            self.pos = (-500, -500)
            self.buttons.curr = self.buttons.nothing
            self.buttons.prev = self.buttons.nothing

