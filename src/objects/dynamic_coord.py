"""
dynamic_coord.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

COORD_TYPE_STATIC = 0
COORD_TYPE_RELATIVE = 1
COORD_ALIGNEMENT_HORIZONTAL = 0
COORD_ALIGNEMENT_VERTICAL = 1

class DynamicCoordObject():
    def __init__(self):
        self.coord: int = 0
        self.coord_type = COORD_TYPE_STATIC

        self.relative_coord: float = 0
        self.coord_alignement: int = COORD_ALIGNEMENT_HORIZONTAL
        self.coord_min: int = 0
        self.coord_max: int = 0

    def ConvertPercentageValue(self,
                               percentage_value: str) -> float:
        error_value_copy = percentage_value
        percentage_value = percentage_value.replace("%", "")
        try:
            percentage_value = float(percentage_value) / 100
        except:
            raise Exception(f"Impossible to format {error_value_copy}, the program expect a percentage value.")
        return percentage_value

    def SetStaticCoord(self,
                 coord: int) -> None:
        self.coord = coord
        self.coord_type = COORD_TYPE_STATIC

    def SetRelativeCoord(self,
                         relative_coord: float | str,
                         coord_alignement: int,
                         coord_min: int = None,
                         coord_max: int = None) -> None:
        self.coord_alignement = coord_alignement
        self.coord_min = None
        self.coord_max = None

        if (type(relative_coord) == str):
            relative_coord = self.ConvertPercentageValue(relative_coord)
        self.relative_coord = relative_coord

        if (coord_min != None):
            self.coord_min = coord_min
        if (self.coord_max != None):
            self.coord_max = coord_max
        self.coord_type = COORD_TYPE_RELATIVE

    def SetCoord(self,
                 coord: int | float | str,
                 coord_alignement: int) -> None:
        if (type(coord) == int):
            self.SetStaticCoord(coord)
        else:
            self.SetRelativeCoord(coord, coord_alignement)

    def GenerateCoord(self,
                      resolution: list) -> int:
        if (self.coord_alignement == COORD_ALIGNEMENT_HORIZONTAL):
            self.coord = self.relative_coord * resolution[0]
        else:
            self.coord = self.relative_coord * resolution[1]

        if (self.coord_max != None and self.coord_max < self.coord):
            self.coord = self.coord_max
        elif (self.coord_min != None and self.coord_min > self.coord):
            self.coord = self.coord_min

        return self.coord