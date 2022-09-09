"""
button_array.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

import json
from src.buttons.single_button import ButtonClass
from src.mouse import MouseClass

RELATIVE_POS = 0
ABSOLUTE_POS = 1
HORIZONTAL_ALIGNEMENT = 0
VERTICAL_ALIGNEMENT = 1

class ButtonCoordinate():
    def __init__(self,
                 coord: int | float,
                 alignement: int = HORIZONTAL_ALIGNEMENT):
        self.coord: int = int(coord)
        self.relative_coord: float = coord
        self.alignement: int = alignement
        self.position_type: int = RELATIVE_POS
        if (type(coord) == int):
            self.position_type = ABSOLUTE_POS

    def ConvertCoord(self,
                     resolution: list) -> int:
        coord = self.coord
        if (self.position_type == RELATIVE_POS):
            if (self.alignement == HORIZONTAL_ALIGNEMENT):
                coord = self.relative_coord * resolution[0]
            else:
                coord = self.relative_coord * resolution[1]
        return int(coord)


class ButtonConfig():
    def __init__(self):
        self.x: ButtonCoordinate = None
        self.y: ButtonCoordinate = None
        self.w: ButtonCoordinate = None
        self.h: ButtonCoordinate = None
        self.button: ButtonClass = ButtonClass(0,0,0,0)

    def UpdateButtonCoord(self, resolution: list) -> None:
        x = self.x.ConvertCoord(resolution)
        y = self.y.ConvertCoord(resolution)
        w = self.w.ConvertCoord(resolution)
        h = self.h.ConvertCoord(resolution)
        self.button.ChangeAreaValue(x, y, w, h)


class ButtonArray():
    def __init__(self):
        self.file_name = None
        self.array = []
        self.name = {}
        self.selected_button = 0
        self.res: list = [0, 0]

    def DecodePositionValue(self,
                            value: str | int | float) -> int | float:
        if (type(value) == str):
            error_value_copy = value
            value = value.replace("%", "")
            try:
                value = float(value) / 100
            except:
                raise Exception(f"Impossible to format {error_value_copy}, the program expect a percentage value.")
        return value

    def SetupButton(self,
                    button_data: dict,
                    font,
                    resolution: list) -> ButtonConfig:
        value = 0
        button_config = ButtonConfig()

        button_config.button.SetText(font, button_data["text"])
        value = self.DecodePositionValue(button_data["x"])
        button_config.x = ButtonCoordinate(value, HORIZONTAL_ALIGNEMENT)
        value = self.DecodePositionValue(button_data["y"])
        button_config.y = ButtonCoordinate(value, VERTICAL_ALIGNEMENT)
        value = self.DecodePositionValue(button_data["w"])
        button_config.w = ButtonCoordinate(value, HORIZONTAL_ALIGNEMENT)
        value = self.DecodePositionValue(button_data["h"])
        button_config.h = ButtonCoordinate(value, VERTICAL_ALIGNEMENT)
        button_config.UpdateButtonCoord(resolution)
        return (button_config)

    def LoadConfig(self,
                   file_path: str,
                   font):
        i: int = 0

        self.file_name = file_path
        data = open(file_path)
        button_config: dict = json.load(data)
        button_list: list = button_config["Buttons"]
        self.array = []
        while (i < len(button_list)):
            self.array.append(self.SetupButton(button_list[i], font, self.res))
            i += 1

    def ResponsiveReposition(self, resolution) -> None:
        if (self.res != resolution):
            self.res = resolution
            for buttons in self.array:
                buttons.UpdateButtonCoord(self.res)

    def DrawButtons(self,
                   Mouse: MouseClass,
                   pygame,
                   ws,
                   game_speed,
                   resolution) -> None:
        i: int = 0

        self.ResponsiveReposition(resolution)
        while (i < len(self.array)):
            self.array[i].button.DrawButton(Mouse, pygame, ws, game_speed)
            i += 1

