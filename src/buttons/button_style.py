"""
button_style.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from math import pi, cos
from include.colors import *
from include.struct import AreaStruct

class ButtonStyle1():
    def __init__(self):
        self.progression = 0
        self.step = (pi/8)
        self.line_length = 50
        self.line_width = 5
        self.mirror = False

    def DrawStyle(self,
                  pygame,
                  ws,
                  is_over: bool,
                  area: AreaStruct,
                  game_speed: float,
                  rendered_text) -> None:
        const_pos = area.x + (rendered_text.get_width() * 1.2)
        y_line_pos = area.y + (rendered_text.get_height() * 1.1)

        if (rendered_text != None):
            ws.blit(rendered_text, (area.x, area.y))
        if self.progression < pi and is_over:
            self.progression += self.step / game_speed
        elif self.progression > 0 and is_over == False:
            self.progression -= self.step / game_speed
        pos1 = [area.x, y_line_pos]
        smooth_pos = ((1 + -cos(self.progression)) / 2)
        if (self.mirror):
            pos1[0], const_pos = const_pos, pos1[0]
            smooth_pos *= -1
        smooth_pos *= self.line_length
        pos2 = [const_pos + smooth_pos, y_line_pos]
        pygame.draw.line(ws, WHITE, pos1, pos2, self.line_width)

BUTTON_STYLES = [
    ButtonStyle1()
]