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
        self.static_coord: int = 0
        self.coord_type = COORD_TYPE_STATIC

        self.relative_coord: float = 0
        self.coord_alignement: int = COORD_ALIGNEMENT_HORIZONTAL
        self.reverse: bool = False
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

    def SetCoord(self,
                 coord: int | float | str,
                 coord_alignement: int = COORD_ALIGNEMENT_HORIZONTAL,
                 coord_min: int = None,
                 coord_max: int = None,
                 reverse: bool = False) -> None:
        if (coord == None):
            return
        self.coord_alignement = coord_alignement
        self.coord_min = None
        self.coord_max = None
        self.reverse = reverse

        if (type(coord) == int):
            self.coord_type = COORD_TYPE_STATIC
            self.static_coord = coord
        else:
            self.coord_type = COORD_TYPE_RELATIVE
            if (type(coord) == str):
                relative_coord = self.ConvertPercentageValue(coord)
            self.relative_coord = relative_coord

        if (coord_min != None):
            self.coord_min = coord_min
        if (coord_max != None):
            self.coord_max = coord_max

    def GenerateCoord(self,
                      resolution: list) -> int:
        if (self.coord_type == COORD_TYPE_RELATIVE):
            self.coord = self.relative_coord * resolution[self.coord_alignement]
        else:
            self.coord = self.static_coord

        if (self.reverse):
            self.coord = resolution[self.coord_alignement] - self.coord

        if (self.coord_max != None and self.coord_max < self.coord):
            self.coord = self.coord_max
        elif (self.coord_min != None and self.coord_min > self.coord):
            self.coord = self.coord_min

        return self.coord