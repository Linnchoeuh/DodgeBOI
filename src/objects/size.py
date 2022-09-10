"""
size.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from include.objects import DynamicCoordObject

class SizeObject():
    def __init__(self) -> None:
        self.w: DynamicCoordObject = DynamicCoordObject()
        self.h: DynamicCoordObject = DynamicCoordObject()
        self.scale: float = 1
        self.scale_min: float = None
        self.scale_max: float = None

    def SetScaleLimit(self,
                 scale_min: float = None,
                 scale_max: float = None) -> None:
        self.scale_min = scale_min
        self.scale_max = scale_max

    def SetScale(self,
                 scale: float) -> float:
        self.scale: float = scale
        if (self.scale_max != None and self.scale_max < self.scale):
            self.scale = self.scale_max
        elif (self.scale_min != None and self.scale_min > self.scale):
            self.scale = self.scale_min
        return (self.scale)


    def UpdateDimensionValue(self,
                             resolution: list) -> None:
        self.w.GenerateCoord(resolution)
        self.h.GenerateCoord(resolution)