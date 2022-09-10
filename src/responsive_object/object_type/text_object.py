"""
text_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from src.effect.font import *
from src.responsive_object.responsive_object import *
from include.objects import COORD_ALIGNEMENT_HORIZONTAL, COORD_ALIGNEMENT_VERTICAL
from include.tools import find_in


class TextObject():
    def __init__(self,
                 font_name: str) -> None:
        self.x: int = 0
        self.y: int = 0
        self.Font: Font = Font(font_name)
        self.required_values: list = [
            "type",
            "name",
            "position_data",
            "text",
            "font",
            "font_size",
            ["position_data", "coords"],
            ["position_data", "coords", "x"],
            ["position_data", "coords", "y"],
        ]

    def CheckRequiredValues(self,
                            config: dict) -> tuple:
        tmp = 0
        missing_value_list: list = []
        for value in self.required_values:
            if (find_in(config, value) == None):
                missing_value_list.append(value)
        return (missing_value_list == [], missing_value_list)

    def SetPosition(self,
                    x: int,
                    y: int) -> None:
        self.x = x
        self.y = y

    def DrawText(self,
                 ws,
                 mouse,
                 game_speed) -> None:
        ws.blit(self.Font.rendered_text, (self.x, self.y))

    def CreateResponsiveObject(self,
                               config: dict,
                               resolution: list[2]) -> ResponsiveObject:
        check_report: tuple = self.CheckRequiredValues(config)
        if (not check_report[0]):
            print(f"Couldn't load a text object because: {check_report[1]} is/are missing.")
            return None
        NewObj: ResponsiveObject = ResponsiveObject(config["name"])

        self.Font.RenderText(config["text"], config["font_size"],
                             find_in(config, "color", WHITE), find_in(config, "back_color"))

        NewObj.object = self
        NewObj.SetObjectPosition = NewObj.object.SetPosition
        NewObj.GetObjectSize = NewObj.object.Font.RenderedTextSize
        NewObj.DrawObject = NewObj.object.DrawText

        coords: dict = find_in(config, ["position_data", "coords"])
        NewObj.position.x.SetCoord(coords["x"], COORD_ALIGNEMENT_HORIZONTAL,
                                   find_in(coords, "x_min"), find_in(coords, "x_max"), find_in(coords, "x_reverse", False))
        NewObj.position.y.SetCoord(coords["y"], COORD_ALIGNEMENT_VERTICAL,
                                   find_in(coords, "y_min"), find_in(coords, "y_max"), find_in(coords, "y_reverse", False))

        offset: dict = find_in(config, ["position_data", "offset"])
        if (offset != None):
            NewObj.offset.x.SetCoord(find_in(offset, "x"), COORD_ALIGNEMENT_HORIZONTAL,
                                     find_in(offset, "x_min"), find_in(offset, "x_max"))
            NewObj.offset.y.SetCoord(find_in(offset, "y"), COORD_ALIGNEMENT_VERTICAL,
                                     find_in(offset, "y_min"), find_in(offset, "y_max"))
        NewObj.UpdateCoordinate(resolution)

        return NewObj
