"""
responsive_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from typing import Any


COORD_TYPE_ABSOLUTE = 0
COORD_TYPE_RELATIVE = 1
COORD_ALIGNEMENT_HORIZONTAL = 0
COORD_ALIGNEMENT_VERTICAL = 1

class DynamicCoordObject():
    def __init__(self):
        self.coord: int = 0
        self.coord_type = COORD_TYPE_ABSOLUTE

        self.relative_coord: float = 0
        self.coord_alignement: int = COORD_ALIGNEMENT_HORIZONTAL
        self.has_coord_min: bool = False
        self.coord_min: int = 0
        self.has_coord_max: bool = False
        self.coord_max: int = 0

    def ConvertPercentageValue(percentage_value: str) -> float:
        error_value_copy = percentage_value
        percentage_value = percentage_value.replace("%", "")
        try:
            percentage_value = float(percentage_value) / 100
        except:
            raise Exception(f"Impossible to format {error_value_copy}, the program expect a percentage value.")
        return percentage_value

    def SetCoord(self,
                 coord: int) -> None:
        self.coord = coord

    def SetRelativeCoord(self,
                         relative_coord: float | str,
                         coord_alignement: int,
                         coord_min: int = None,
                         coord_max: int = None) -> None:
        self.coord_alignement = coord_alignement
        self.has_coord_min = False
        self.has_coord_max = False

        if (type(relative_coord) == str):
            relative_coord = self.ConvertPercentageValue(relative_coord)
        self.relative_coord = relative_coord

        self.has_coord_min = (coord_min != None)
        if (self.has_coord_min):
            self.coord_min = coord_min
        self.has_coord_max = (coord_max != None)
        if (self.has_coord_max):
            self.coord_max = coord_max

    def GenerateCoord(self,
                      resolution: list) -> int:
        if (self.coord_alignement == COORD_ALIGNEMENT_HORIZONTAL):
            self.coord = self.relative_coord * resolution[0]
        else:
            self.coord = self.relative_coord * resolution[1]

        if (self.has_coord_max and self.coord_max < self.coord):
            self.coord = self.coord_max
        elif (self.has_coord_min and self.coord_min < self.coord):
            self.coord = self.coord_min

        return self.coord

class ObjectPosition():
    def __init__(self):
        self.x: DynamicCoordObject = DynamicCoordObject()
        self.y: DynamicCoordObject = DynamicCoordObject()

    def UpdatePositionValues(self,
                             resolution: list) -> None:
        self.x.GenerateCoord(resolution)
        self.y.GenerateCoord(resolution)

class ResponsiveObject():
    def __init__(self,
                 object: Any = None):
        self.position: ObjectPosition = ObjectPosition()
        self.scale: float = 1
        self.object: Any = None
        self.SetObjectPosition: function = None
        self.SetObjectDimension: function = None
        self.GetObjectPosition: function = None
        self.GetObjectDimension: function = None
        self.DrawObject: function = None

    def SetObject(self,
                 object: Any = None,
                 SetObjectPosition: function = None,
                 SetObjectDimension: function = None,
                 GetObjectPosition: function = None,
                 GetObjectDimension: function = None,
                 DrawObject: function = None) -> None: