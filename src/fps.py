"""
fps.py
Lenny Vigeon (lenny.vigeon@gmail.com)
An fps class that work with pygame
"""

from src.effect.font import Font

class FpsClass():
    def __init__(self):
        self.BASE = 60
        self.CAPPED = 165
        self.current = self.CAPPED
        self.Font: Font = Font("VCR_OSD_MONO_1.ttf")
        self.Font.antialiasing_default = False
        self.Font.LoadFontSize(25)
        self.dt = 0

    def update_fps(self, clock):
        self.dt = clock.tick(self.CAPPED) / 1000
        self.current = clock.get_fps()
        return (self.current / self.BASE)

    def show_fps(self, surface, pos):
        text = self.Font.loaded_font.render(str(round(self.current, 2)),
                           True, (255, 0, 0))
        surface.blit(text, pos)