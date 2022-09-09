"""
responsive_object_array.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

import json
from src.responsive_object.responsive_object import ResponsiveObject
from src.responsive_object.object_type.interpretor.default_interpretor import TypeInterpretor


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
