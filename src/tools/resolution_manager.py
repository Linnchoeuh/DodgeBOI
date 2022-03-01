"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
Copyright (c) 2022
"""

class ResolutionObject():
    def __init__(self, width, height):
        self.native = (1280, 720)
        self.current = [width, height]

class ResolutionManagerClass():
    def __init__(self, width, height):
        self.WIDTH = 0;
        self.HEIGHT = 1;
        self.Res = ResolutionObject(width, height)
        self.scaling_coef = self.Res.current[self.HEIGHT] / self.Res.native[self.HEIGHT]
        self.fullscreen = False

    def Scaling(self, value):
        return (value * self.scaling_coef)

    def PosScaling(self, x, y):
        return (x * self.scaling_coef, y * self.scaling_coef)

    def AreaScaling(self, x, y, w, h):
        return (x * self.scaling_coef, y * self.scaling_coef, w * self.scaling_coef, h * self.scaling_coef)

    def ToggleFullscreen(self, pygame, Keyboard, Game, K_F11):
        key_status = [
            Keyboard.buttons.curr[K_F11],
            Keyboard.buttons.prev[K_F11]
        ]
        if (key_status[0] == True and key_status[1] == False):
            if self.fullscreen == True:
                self.fullscreen = False
                Game.ws = pygame.display.set_mode(self.Res.current)
            else:
                self.fullscreen = True
                Game.ws = pygame.display.set_mode(self.Res.current, pygame.FULLSCREEN)
