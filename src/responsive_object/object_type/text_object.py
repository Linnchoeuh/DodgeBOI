"""
text_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from src.effect.font import *
from src.responsive_object.responsive_object import \
    ResponsiveObject,\
    COORD_ALIGNEMENT_HORIZONTAL, \
    COORD_ALIGNEMENT_VERTICAL
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
            "x",
            "y",
            "text",
            "font",
            "font_size"
        ]

    def CheckRequiredValues(self,
                            config: dict) -> tuple:
        tmp = 0
        missing_value_list: list = []
        for value in self.required_values:
            try:
                tmp = config[value]
            except:
                missing_value_list.append(value)
        return (missing_value_list == [], missing_value_list)

    def SetPosition(self,
                    x: int,
                    y: int) -> None:
        self.x = x
        self.y = y

    def DrawText(self,
                 ws) -> None:
        ws.blit(self.Font.rendered_font, (self.x, self.y))

    def GetTextSize(self) -> list[2]:
        return [self.Font.rendered_font.get_width(),
                self.Font.rendered_font.get_height()]

    def CreateResponsiveObject(self,
                               config: dict,
                               resolution: list[2]) -> ResponsiveObject:
        check_report: tuple = self.CheckRequiredValues(config)
        if (not check_report[0]):
            print(f"Couldn't load a text object because: [{check_report[1]}] is/are missing.")
            return None
        NewObject: ResponsiveObject = ResponsiveObject(config["name"])
        NewObject.object = self
        NewObject.object.Font.RenderText(
            config["text"], config["font_size"], find_in(config, "color"), find_in(config, "back_color"))
        NewObject.SetObjectPosition = NewObject.object.SetPosition
        NewObject.GetObjectSize = NewObject.object.GetTextSize
        NewObject.DrawObject = NewObject.object.DrawText
        NewObject.position.x.SetCoord(config["x"], COORD_ALIGNEMENT_HORIZONTAL)
        NewObject.position.y.SetCoord(config["y"], COORD_ALIGNEMENT_VERTICAL)
        NewObject.offset.x.SetCoord(find_in(config, "offset_x", 0), COORD_ALIGNEMENT_HORIZONTAL)
        NewObject.offset.y.SetCoord(find_in(config, "offset_y", 0), COORD_ALIGNEMENT_VERTICAL)
        NewObject.UpdateCoordinate(resolution)

        return NewObject
