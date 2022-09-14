"""
responsive_object_array.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

import json

from include.input_devices import MouseClass

from src.responsive_object.responsive_object import ResponsiveObject
from src.responsive_object.object_type.button_object import ButtonObject
from src.responsive_object.object_type.interpretor.default_interpretor import TypeInterpretor

class ResponsiveObjectArray():
    def __init__(self) -> None:
        self.array: list[ResponsiveObject] = []
        self.config_path: str = ""
        self.res: list[2] = None
        self.ws = None

        self.TypeInterpretor = TypeInterpretor()
        self.button_dict: dict = {}

    def CheckObjectsNames(self) -> None:
        i: int = 0
        k: int = 0
        while (i < len(self.array)):
            k = i + 1
            while (k < len(self.array)):
                if (self.array[i].name == self.array[k].name):
                    raise Exception("Name Checker: Impossible to load json, a name appear twice!")
                k += 1
            i += 1


    def LoadConfigFile(self,
                       file_path: str) -> None:
        if (self.res == None):
            raise Exception("LoadConfigFile: Resolution is not set! Use \"SetResolution\" method before.")
        self.config_path = file_path
        file = open(file_path)
        responsive_array: dict = json.load(file)
        self.array = []
        self.button_dict = {}
        i: int = 0
        while (i < len(responsive_array)):
            NewObject = self.TypeInterpretor.Interpret(responsive_array[i], self.res)
            if (NewObject != None):
                self.array.append(NewObject)
                self.CheckObjectsNames()
            i += 1

    def ReloadConfig(self) -> None:
        self.LoadConfigFile(self.config_path)

    def SetResolution(self,
                      resolution: list[2]):
        self.res = resolution

    def CheckResolution(self,
                        resolution: list[2]) -> None:
        if (self.res != resolution):
            self.SetResolution(resolution)
            i: int = 0
            while (i < len(self.array)):
                self.array[i].UpdateCoordinate(self.res)
                i += 1

    def DisplayObjects(self,
                       mouse: MouseClass,
                       game_speed: float) -> None:
        i: int = 0
        while (i < len(self.array)):
            self.array[i].DrawObject(self.ws, mouse, game_speed)
            i += 1

    def ReturnButtonStatus(self) -> dict:
        i: int = 0
        while (i < len(self.array)):
            if (type(self.array[i].object) == ButtonObject):
                self.button_dict[self.array[i].name] = (self.array[i].object.is_over,
                                                        self.array[i].object.pressed,
                                                        self.array[i].object.clicked)
            i += 1
        return self.button_dict

