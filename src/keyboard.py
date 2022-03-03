"""
keyboard.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Keyboard manager
Copyright (c) 2022
"""

class KeyboardKeyClass():
    def __init__(self, pygame):
        self.prev = pygame.key.get_pressed()
        self.curr = pygame.key.get_pressed()
        self.nothing = pygame.key.get_pressed()

class KeyboardClass():
    def __init__(self, pygame):
        self.pygame = pygame
        self.key = KeyboardKeyClass(self.pygame)
        self.disable = False

    def updateStatus(self):
        if (self.disable == False):
            self.key.prev = self.key.curr;
            self.key.curr = self.pygame.key.get_pressed()
        else:
            self.key.curr = self.key.nothing
            self.key.prev = self.key.nothing

    def KeyOncePressed(self, key_ID):
        return (self.key.curr[key_ID] and self.key.prev[key_ID] == False)
