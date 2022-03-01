"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

class ResolutionObject():
    def __init__(self, width, height):
        self.native = (width, height)
        self.current = [width, height]

class ResolutionManagerClass():
    def __init__(self, width, height):
        self.WIDTH = 0;
        self.HEIGHT = 1;
        self.Res = ResolutionObject(width, height)
        self.scaling_coef = 1
        self.fullscreen = False

    def ResScaling(self, value):
        return (value * self.scaling_coef)

    def ResPosScaling(self, x, y):
        return (x * self.scaling_coef, y * self.scaling_coef)

    def ChangeRes(self, width, height):
        self.Res.current = [width, height]
        self.scaling_coef = self.Res.current[self.HEIGHT] / self.Res.native[self.HEIGHT]

    def ToggleFullscreen(self, pygame, Keyboard, Game):
        key_status = [
            Keyboard.buttons.curr[1073741892],
            Keyboard.buttons.prev[1073741892]
        ]
        if (key_status[0] == True and key_status[1] == False):
            if self.fullscreen == True:
                self.fullscreen = False
                Game.ws = pygame.display.set_mode(self.Res.current)
            else:
                self.fullscreen = True
                Game.ws = pygame.display.set_mode(self.Res.current, pygame.FULLSCREEN)
