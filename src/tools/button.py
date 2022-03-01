"""
button.py
Lenny Vigeon (lenny.vigeon@gmail.com)
To create squared button
Copyright (c) 2022
"""

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
            if buttons.curr[0] == True and buttons.prev[0] == False:
                self.clicked = True
        return (self.clicked, self.touched)

    def Style1(self, Game, Font):
        status = CheckArea()