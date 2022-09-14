"""
game.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
"""

import pygame

from include.input_devices import KeyboardClass

NATIVE_WINDOW_RESOLUTION = (1280, 720)
WIDTH = 0
HEIGHT = 1
_DEFAULT_WINDOW_PARAMETER = pygame.RESIZABLE | pygame.HWSURFACE | pygame.DOUBLEBUF

class ScalerClass():
    def __init__(self,
                 current_res: list[int],
                 native_res: list[int]):
        self.coef = current_res[HEIGHT] / native_res[HEIGHT]

    def UpdateScalingCoef(self,
                          current_res: list[int],
                          native_res: list[int]) -> None:
        self.coef = current_res[HEIGHT] / native_res[HEIGHT]

    def Val(self,
            value: int | float):
        return (value * self.coef)

    def Pos(self,
            x: int | float,
            y: int | float):
        return (self.Val(x), self.Val(y))

    def Area(self,
             x: int | float,
             y: int | float,
             w: int | float,
             h: int | float):
        return (self.Val(x), self.Val(y), self.Val(w), self.Val(h))

class WindowResolution():
    def __init__(self,
                 width: int,
                 height: int):
        self.native: tuple[int] = NATIVE_WINDOW_RESOLUTION
        self.current: list[int] = [width, height]
        self.windowed: list[int] = [width, height]
        self.fullscreen: list[int] = pygame.display.get_desktop_sizes()[0]
        self._previous: list[int] = self.current

class ScreenClass():
    def __init__(self,
                 width: int,
                 height: int):
        self.ws: pygame.surface.Surface = None

        self.win_res: WindowResolution = WindowResolution(width, height)
        self.is_fullscreen: bool = False
        self.resolution_changed: bool = False
        self.Scaler: ScalerClass = ScalerClass(self.win_res.current, self.win_res.native)

    def ResolutionChangerChecker(self) -> bool:
        self.win_res.current = [self.ws.get_width(), self.ws.get_height()]
        self.resolution_changed = self.win_res.current != self.win_res._previous

        if (self.resolution_changed):

            print(f"Resolution changed! {self.win_res._previous} -> {self.win_res.current}")
            self.Scaler.UpdateScalingCoef(self.win_res.current, self.win_res.native)
        self.win_res._previous = self.win_res.current
        return self.resolution_changed


    def ToggleFullscreen(self,
                         Keyboard: KeyboardClass,
                         key_trigger: int):

        if (Keyboard.KeyOncePressed(key_trigger, True)):
            if (self.is_fullscreen):
                self.is_fullscreen = False
                self.win_res.current = self.win_res.windowed
                print(pygame.display.Info())
                self.ws = pygame.display.set_mode(self.win_res.current,
                    _DEFAULT_WINDOW_PARAMETER)
            else:
                self.is_fullscreen = True
                self.win_res.windowed = self.win_res.current
                self.win_res.current = pygame.display.get_desktop_sizes()[0]
                self.ws = pygame.display.set_mode(self.win_res.current,
                    _DEFAULT_WINDOW_PARAMETER | pygame.FULLSCREEN)

