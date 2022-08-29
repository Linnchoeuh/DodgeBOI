"""
single_button.py
Lenny Vigeon (lenny.vigeon@gmail.com)

Copyright (c) 2022
"""
# from include.buttons import butt
# from tools.is_positive import *
from include.colors import *
from include.struct import AreaStruct, SpaceStruct
from src.mouse import MouseClass
from src.buttons.button_style import BUTTON_STYLES

class ButtonClass():
    def __init__(self,
                 x: int,
                 y: int,
                 w: int,
                 h: int):
        self.clicked: bool = False
        self.over: bool = False
        self.text: str = ""
        self.rendered_text = None
        self.scale_hitbox_to_text = False
        self.area: AreaStruct = AreaStruct()
        self.space: SpaceStruct = SpaceStruct()
        self.ChangeAreaValue(x, y, w, h)
        self.style = None
        self.style = BUTTON_STYLES[0]
        # self.style1data = Style1Struct()

    def SetText(self,
                font,
                text: str,
                color: tuple = WHITE,
                scale_hitbox_to_text: bool = False) -> None:
        self.rendered_text = font.render(text, True, color)
        self.scale_hitbox_to_text = scale_hitbox_to_text
        # print(text.Font.size, text.Font.metrics)

    def ChangeAreaValue(self,
                        x: int,
                        y: int,
                        w: int,
                        h: int,
                        Res = None) -> None:
        if (Res != None and Res.Manager != None):
            x = Res.Manager.Scale.Val(x)
            y = Res.Manager.Scale.Val(y)
            w = Res.Manager.Scale.Val(w)
            h = Res.Manager.Scale.Val(h)
        self.area.SetValues(x, y, w, h)
        self.space.SetValuesFromArea(self.area)

    def CheckArea(self, Mouse) -> tuple:
        self.clicked = False
        self.over = False
        pos = Mouse.pos
        if pos[0] >= self.space.x1 and pos[1] >= self.space.y1 and \
            pos[0] < self.space.x2 and pos[1] < self.space.y2:
            self.over = True
            buttons = Mouse.buttons
            if buttons.pressed[0] and buttons._previous[0] == False:
                self.clicked = True
        return (self.clicked, self.over)

    def DrawButton(self,
                   Mouse: MouseClass,
                   pygame,
                   ws,
                   game_speed) -> bool:
        status = self.CheckArea(Mouse)
        if (self.style != None):
            self.style.DrawStyle(pygame, ws, status[1], self.area, game_speed, self.rendered_text)

    def SetStyle(self, style_id):
        pass

