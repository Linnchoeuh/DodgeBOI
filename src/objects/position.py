"""
position.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from include.objects import DynamicCoordObject

class PositionObject():
    def __init__(self):
        self.x: DynamicCoordObject = DynamicCoordObject()
        self.y: DynamicCoordObject = DynamicCoordObject()

    def UpdatePositionValues(self,
                             resolution: list) -> None:
        self.x.GenerateCoord(resolution)
        self.y.GenerateCoord(resolution)