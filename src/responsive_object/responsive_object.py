"""
responsive_object.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""










class ResponsiveObject():
    def __init__(self,
                 name: str,
                 object = None):
        self.position: ObjectPosition = ObjectPosition()
        self.size: ObjectSize = ObjectSize()
        self.offset: ObjectPosition = ObjectPosition()
        self.scale
        # self.is_position_dominant: bool = True
        # self.is_size_dominant: bool = True

        self.name: str = name

        self.object = object

        self.SetObjectPosition: function = None
        self.SetObjectSize: function = None

        self.GetObjectPosition: function = None
        self.GetObjectSize: function = None

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

