"""
default_interpretor.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from include.tools import find_in
from src.responsive_object.object_type.text_object import *
from src.responsive_object.responsive_object import ResponsiveObject

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
                font_name = find_in(config, "font")
                if (font_name == None):
                    return None
                NewTextObject = TextObject(font_name)
                return NewTextObject.CreateResponsiveObject(config, resolution)
            case "rect":
                return None
            case "button":
                return None
