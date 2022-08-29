"""
area.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

class AreaStruct():
    def __init__(self,
                 x: int = 0,
                 y: int = 0,
                 w: int = 0,
                 h: int = 0) -> None:
        self.x: int = x
        self.y: int = y
        self.w: int = w
        self.h: int = h

    def PrintValues(self) -> None:
        print(f"X: {self.x} | Y: {self.y} | WIDTH: {self.w} | HEIGHT: {self.h}")

    def SetValues(self,
                  x: int,
                  y: int,
                  w: int,
                  h: int) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def CopyValues(self,
                   area) -> None:
        self.x = area.x
        self.y = area.y
        self.w = area.w
        self.h = area.h
