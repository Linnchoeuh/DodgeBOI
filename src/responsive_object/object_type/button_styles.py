"""
button_style.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from math import pi as PI, cos
import pygame.surface
import pygame.draw

from include.colors import *
from include.tools import find_in

from src.effect.font import Font
from src.responsive_object.responsive_object import *

class ButtonStyle1():
    def __init__(self):
        self.progression = 0
        self.step = (PI / 8)
        self.line_length = 25
        self.line_width = 5
        self.mirror = False
        self.Font: Font = None
        self.required_values: list = [
            "text",
            "font",
            "font_size"
        ]

    def DrawStyle(self,
                  ws: pygame.surface.Surface,
                  button,
                  game_speed: float) -> None:

        const_pos = button.area.x + (self.Font.rendered_text.get_width() + 10)
        y_line_pos = button.area.y + (self.Font.rendered_text.get_height() + 5)

        if (game_speed == 0):
            game_speed = 0.000000000001
        if (self.Font.rendered_text != None):
            ws.blit(self.Font.rendered_text, button.GetPosition())

        if (button.clicked):
            self.progression = self.progression / 3
        if (self.progression < PI and button.is_over):
            self.progression += self.step / game_speed
        if (self.progression > 0 and not button.is_over):
            self.progression -= self.step / game_speed
        pos1 = [button.area.x, y_line_pos]
        smooth_pos = ((1 - cos(self.progression)) / 2)
        if (self.mirror):
            pos1[0], const_pos = const_pos, pos1[0]
            smooth_pos *= -1
        smooth_pos *= self.line_length
        pos2 = [const_pos + smooth_pos, y_line_pos]
        pygame.draw.line(ws, WHITE, pos1, pos2, self.line_width)

    def CheckRequiredValues(self,
                            config: dict) -> tuple:
        tmp = 0
        missing_value_list: list = []
        for value in self.required_values:
            if (find_in(config, value) == None):
                missing_value_list.append(value)
        return (missing_value_list == [], missing_value_list)

    def CreateResponsiveObject(self,
                               button,
                               config: dict,
                               resolution: list[2]) -> ResponsiveObject:
        check_report: tuple = self.CheckRequiredValues(config)
        if (not check_report[0]):
            print(f"Couldn't load a text object because: {check_report[1]} is/are missing.")
            return None
        NewObj: ResponsiveObject = ResponsiveObject(config["name"])
        self.Font = Font(config["font"])

        self.Font.RenderText(config["text"], config["font_size"],
                             find_in(config, "color", WHITE), find_in(config, "back_color"))
        self.mirror = find_in(config, "mirror", False)
        return NewObj

BUTTON_STYLES = [
    ButtonStyle1
]