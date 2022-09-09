"""
scale.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

class ScaleObject():
    """
    ### Summary:
        - A class made for to manipulate scale value with limits.

    ### Avalaible methods:
        - SetScaleLimit
        - SetScale
    """
    def __init__(self) -> None:
        self.val: float = 1
        self.min: float = None
        self.max: float = None

    def SetScaleLimit(self,
                      min: float = None,
                      max: float = None) -> None:
        """
        ### Summary:
            - Let you set max scale and min scale,
            if you don't set any arguments it will remove all scale limit.
            If `min` is bigger than `max` changes will not apply.

        ### Optional Args:
            - `float` min: Minimum authorized scale you want. (None in case you don't want any limit)
            - `float` max: Maximum authorized scale you want. (None in case you don't want any limit)
        """
        if (min == None or max == None):
            self.min = min
            self.max = max
        elif (min <= max):
            self.min = min
            self.max = max

    def SetScale(self,
                 new_scale: float) -> float:
        """
        ### Summary:
            - Let you set a new scale in variable `val`,
            but it's sensitive to scales limits you set.

        ### Args:
            - `float` new_scale: The new scale you want

        ### Returns:
            - `float`: returns `self.val`
        """
        self.val = new_scale
        if (self.max <= self.val):
            self.val = self.max
        elif (self.min >= self.val):
            self.val = self.min



class AllScaleObject():
    """
    ### Summary:
        - A set of `ScaleObject` for scaling to x, y or both.
    """
    def __init__(self) -> None:
        self.all: ScaleObject = ScaleObject()
        self.x: ScaleObject = ScaleObject()
        self.y: ScaleObject = ScaleObject()