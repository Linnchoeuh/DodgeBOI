"""
responsive_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

import json
from src.effect.font import *

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

class ObjectPosition():
    def __init__(self):
        self.x: DynamicCoordObject = DynamicCoordObject()
        self.y: DynamicCoordObject = DynamicCoordObject()

    def UpdatePositionValues(self,
                             resolution: list) -> None:
        self.x.GenerateCoord(resolution)
        self.y.GenerateCoord(resolution)

class ObjectSize():
    def __init__(self):
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


class ResponsiveObject():
    def __init__(self,
                 name: str,
                 object = None):
        self.position: ObjectPosition = ObjectPosition()
        self.size: ObjectSize = ObjectSize()
        self.offset: ObjectPosition = ObjectPosition()
        # self.is_position_dominant: bool = True
        # self.is_size_dominant: bool = True

        self.name: str = name

        self.object = object

        self.SetObjectPosition: function = None
        self.SetObjectSize: function = None
        # self.SetObjectArea: function = None
        # self.SetObjectSpace: function = None

        self.GetObjectPosition: function = None
        self.GetObjectSize: function = None
        # self.GetObjectArea: function = None
        # self.GetObjectSpace: function = None

        self.DrawObject: function = None

    def UpdateCoordinate(self,
                         resolution: list[2]) -> None:
        if (self.SetObjectPosition != None):
            self.position.UpdatePositionValues(resolution)
            self.SetObjectPosition(self.position.x.coord, self.position.y.coord)

class TextObject():
    def __init__(self,
                 font_path: str) -> None:
        self.x: int = 0
        self.y: int = 0
        self.Font: Font = Font(font_path)

    def SetPosition(self,
                    x: int,
                    y: int) -> None:
        self.x = x
        self.y = y

    def DrawText(self,
                 ws) -> None:
        ws.blit(self.Font.rendered_font, (self.x, self.y))

    def GetTextSize(self) -> list[2]:
        return [self.Font.rendered_font.get_width(), self.Font.rendered_font.get_height()]

class TypeInterpretor():
    def __init__(self) -> None:
        self.required_values: list = [
            "type",
            "name",
            "x",
            "y"
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


    def Interpret(self,
                  config: dict,
                  resolution: list[2]) -> ResponsiveObject | None:
        check_report: tuple = self.CheckRequiredValues(config)
        if (not check_report[0]):
            print(f"Couldn't load an object because: [{check_report[1]}] is/are missing.")
            return None
        type_name: str = config["type"]
        match type_name:
            case "text":
                return self.TextType(config, resolution)
            case "rect":
                return None
            case "button":
                return None

    def TextType(self,
                 config: dict,
                 resolution: list[2]) -> ResponsiveObject:
        NewObject: ResponsiveObject = ResponsiveObject(config["name"])
        NewText: TextObject = TextObject(config["font"])
        NewObject.object = NewText
        NewObject.object.Font.RenderText(config["text"], config["font_size"], config["color"])
        NewObject.SetObjectPosition = NewObject.object.SetPosition
        NewObject.DrawObject = NewObject.object.DrawText
        NewObject.position.x.SetCoord(config["x"], COORD_ALIGNEMENT_HORIZONTAL)
        NewObject.position.y.SetCoord(config["y"], COORD_ALIGNEMENT_VERTICAL)
        NewObject.UpdateCoordinate(resolution)

        return NewObject

class ResponsiveObjectArray():
    def __init__(self) -> None:
        self.array: list[ResponsiveObject] = []
        self.config_path: str = ""
        self.res: list[2] = None
        self.ws = None

        self.TypeInterpretor = TypeInterpretor()

    def LoadConfigFile(self,
                       file_path: str) -> None:
        if (self.res == None):
            raise Exception("LoadConfigFile: Resolution is not set! Use \"SetResolution\" method before.")
        self.config_path = file_path
        file = open(file_path)
        responsive_array: dict = json.load(file)
        self.array = []
        i: int = 0
        while (i < len(responsive_array)):
            NewObject = self.TypeInterpretor.Interpret(responsive_array[i], self.res)
            if (NewObject != None):
                self.array.append(NewObject)
            i += 1

    def ReloadConfig(self) -> None:
        self.LoadConfigFile(self.config_path)

    def SetResolution(self,
                      resolution: list[2]):
        self.res = resolution

    def CheckResolution(self,
                        resolution: list[2]) -> None:
        if (self.res != resolution):
            print(f"Resolution changed! {self.res} -> {resolution}")
            self.SetResolution(resolution)
            i: int = 0
            while (i < len(self.array)):
                self.array[i].UpdateCoordinate(self.res)
                i += 1

    def DisplayObjects(self):
        i: int = 0
        while (i < len(self.array)):
            self.array[i].DrawObject(self.ws)
            i += 1
