"""
button.py
Lenny Vigeon (lenny.vigeon@gmail.com)
To create squared button
Copyright (c) 2022
"""

from math import *

class Style1Struct():
    def __init__(self):
        self.progression = 0;

class AreaStruct():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

class ButtonClass():
    def __init__(self, x, y, w, h):
        self.clicked = False
        self.touched = False
        self.text = ""
        self.area = AreaStruct(x, y, w, h)
        self.style1data = Style1Struct()

    def ChangeAreaValue(self, x, y, w, h):
        self.area.x = x
        self.area.y = y
        self.area.w = w
        self.area.h = h

    def CheckArea(self, Mouse):
        self.clicked = False
        self.touched = False
        x = self.area.x
        y = self.area.y
        w = x + self.area.w
        h = y + self.area.h
        if x > w:
            swap = w
            w = x
            x = swap
        if y > h:
            swap = h
            h = y
            y = swap
        pos = Mouse.pos
        if pos[0] >= x and pos[1] >= y and pos[0] < w and pos[1] < h:
            self.touched = True
            buttons = Mouse.buttons
            if buttons.curr[0] and buttons.prev[0] == False:
                self.clicked = True
        return (self.clicked, self.touched)

    def Style1(self, Game, font):
        status = self.CheckArea(Game.Mouse)
        text = font.render(self.text, True, Game.Colors.white)
        linewidth = round(Game.ResManager.Scaling(5))
        const_pos = self.area.x + self.area.w

        Game.ws.blit(text, (self.area.x, self.area.y))
        if self.style1data.progression < pi and status[1]:
            self.style1data.progression += (pi/8) / Game.framerate.speed
        elif self.style1data.progression > 0 and status[1] == False:
            self.style1data.progression -= (pi/8) / Game.framerate.speed
        pos1 = [self.area.x, self.area.y + self.area.h]
        smooth_pos = (Game.ResManager.Scaling(50) * ((1 + -cos(self.style1data.progression)) / 2))
        pos2 = [const_pos + smooth_pos, self.area.y + self.area.h]
        Game.pygame.draw.line(Game.ws, Game.Colors.white, pos1, pos2, linewidth)
        return (status[0])

