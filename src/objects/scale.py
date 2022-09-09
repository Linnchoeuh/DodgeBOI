"""
scale.py
Lenny Vigeon (lenny.vigeon@gmail.com)
"""

class ObjectScale():
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
        self.min = min
        self.max = max

    def SetScale(self,
                 new_scale: float) -> float:
        """
        ### Summary:
            Let you set a new scale in variable `val`,
            but it's sensitive to potential scales limits you set.

        ### Args:
            - `float` new_scale: The ne scale you want

        ### Returns:
            - `float`: _description_
        """
        self.val = new_scale



class AllScaleObject()
