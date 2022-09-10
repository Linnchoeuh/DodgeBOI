"""
responsive_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

from include.objects import *

class ResponsiveObject():
    def __init__(self,
                 name: str,
                 object = None):
        self.position: PositionObject = PositionObject()
        self.size: SizeObject = SizeObject()
        self.offset: PositionObject = PositionObject()
        self.scale: AllScaleObject = AllScaleObject()
        # self.is_position_dominant: bool = True
        # self.is_size_dominant: bool = True

        self.name: str = name

        self.object = object

        self.SetObjectPosition: function = None
        self.SetObjectSize: function = None
        self.SetObjectOffset: function = None
        self.SetObjectScale: function = None

        self.GetObjectPosition: function = None
        self.GetObjectSize: function = None
        self.GetObjectOffset: function = None
        self.GetObjectScale: function = None

        self.DrawObject: function = None

    def UpdateCoordinate(self,
                         resolution: list[2]) -> None:
        if (self.SetObjectPosition != None):
            self.position.UpdatePositionValues(resolution)
            self.SetObjectPosition(self.position.x.coord, self.position.y.coord)
        if (self.GetObjectSize != None):
            object_size = self.GetObjectSize()
            self.offset.UpdatePositionValues(object_size)
            self.position.x.coord -= self.offset.x.coord
            self.position.y.coord -= self.offset.y.coord
            self.SetObjectPosition(self.position.x.coord, self.position.y.coord)
        if (self.SetObjectSize != None):
            object_size = self.GetObjectSize()
            self.SetObjectSize(object_size[0], object_size[1])


