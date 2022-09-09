"""
space.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from include.objects import AreaObject

class SpaceObject():
    def __init__(self,
                 x1: int = 0,
				 y1: int = 0,
				 x2: int = 0,
				 y2: int = 0) -> None:
        self.x1: int = 0
        self.y1: int = 0
        self.x2: int = 0
        self.y2: int = 0

    def PrintValues(self) -> None:
        print(f"X1: {self.x1} | Y1: {self.y1} | X2: {self.x2} | Y2: {self.y2}")

    def SetValues(self,
                  x1: int,
                  y1: int,
                  x2: int,
                  y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def SetValuesFromArea(self,
                          area: AreaObject):
        self.SetValues(area.x, area.y, area.x + area.w, area.y + area.h)
        if self.x1 > self.x2:
            self.x1, self.x2 = self.x2, self.x1
        if self.y1 > self.y2:
            self.y1, self.y2 = self.y2, self.y1

    def CopyValues(self,
                   space):
        self.x1 = space.x1
        self.y1 = space.y1
        self.x2 = space.x2
        self.y2 = space.y2
