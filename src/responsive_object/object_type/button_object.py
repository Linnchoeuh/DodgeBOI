"""
text_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

import pygame.surface

from include.tools import find_in
from include.input_devices import MouseClass

from src.responsive_object.responsive_object import *
from src.responsive_object.object_type.text_object import *
from src.responsive_object.object_type.button_styles import BUTTON_STYLES

BUTTON_IS_OVER = 0
BUTTON_PRESSED = 1
BUTTON_CLICKED = 2

class ButtonObject():
    def __init__(self,
                 style_id: str) -> None:
        self.is_over: bool = False
        self.pressed: bool = False
        self.clicked: bool = False
        self.area: AreaObject = AreaObject()
        self.space: SpaceObject = SpaceObject()
        self.style = BUTTON_STYLES[style_id]()
        self.required_values: list = [
            "type",
            "name",
            "position_data",
            ["position_data", "coords"],
            ["position_data", "coords", "x"],
            ["position_data", "coords", "y"]
        ]

    def SetPosition(self,
                    x: int,
                    y: int) -> None:
        self.area.SetValues(x, y, self.area.w, self.area.h)
        self.space.SetValuesFromArea(self.area)

    def GetPosition(self) -> tuple[int]:
        return (self.area.x, self.area.y)

    def SetSize(self,
                w: int,
                h: int) -> None:
        self.area.SetValues(self.area.x, self.area.y, w, h)
        self.space.SetValuesFromArea(self.area)

    def GetSize(self) -> tuple[int]:
        return (self.area.w, self.area.h)

    def CheckArea(self,
                  Mouse: MouseClass) -> tuple[bool]:
        self.is_over = False
        self.pressed = False
        self.clicked = False
        pos = Mouse.pos
        if pos[0] >= self.space.x1 and pos[1] >= self.space.y1 and \
            pos[0] < self.space.x2 and pos[1] < self.space.y2:
            self.is_over = True
            self.clicked = Mouse.buttons.clicked[0]
            self.pressed = Mouse.buttons.pressed[0]
        return (self.is_over, self.pressed, self.clicked)

    def CheckRequiredValues(self,
                            config: dict) -> tuple:
        missing_value_list: list = []
        for value in self.required_values:
            if (find_in(config, value) == None):
                missing_value_list.append(value)
        return (missing_value_list == [], missing_value_list)

    def DrawButton(self,
                   ws: pygame.surface.Surface,
                   mouse: MouseClass,
                   game_speed: float) -> tuple[bool]:
        button_output: tuple = self.CheckArea(mouse)
        self.style.DrawStyle(ws, self, game_speed)
        return button_output

    def CreateResponsiveObject(self,
                               config: dict,
                               resolution: list[2]) -> ResponsiveObject:
        check_report: tuple = self.CheckRequiredValues(config)
        if (not check_report[0]):
            print(f"Couldn't load a button object because: {check_report[1]} is/are missing.")
            return None
        NewObj: ResponsiveObject = self.style.CreateResponsiveObject(self, config, resolution)
        NewObj.object = self
        NewObj.DrawObject = self.DrawButton
        NewObj.SetObjectPosition = self.SetPosition
        NewObj.SetObjectSize = self.SetSize
        NewObj.GetObjectSize = self.style.Font.RenderedTextSize

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
