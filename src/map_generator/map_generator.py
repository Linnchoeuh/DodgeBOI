"""
map_generator.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where the map is created
Copyright (c) 2022
"""

BID_VOID = 0
BID_FULL = 1
BID_DOWN = 2
BID_UP = 3
BID_BREAK = 4
BID_RED = 5
BID_BLUE = 6
BID_YELLOW = 7

class ObstacleStruct():
    def __init__(self):
        pass

class BlocClass():
    def __init__(self):
        self.obstacle = [

        ]
        self.shape = [
            # contain void
            [BID_FULL,  BID_VOID,  BID_VOID],
            [BID_VOID,  BID_FULL,  BID_VOID],
            [BID_VOID,  BID_VOID,  BID_FULL],
            # contain less void
            [BID_VOID,  BID_FULL,  BID_FULL],
            [BID_FULL,  BID_VOID,  BID_FULL],
            [BID_FULL,  BID_FULL,  BID_VOID],
            # contain down obstacle
            [BID_DOWN,  BID_FULL,  BID_FULL],
            [BID_FULL,  BID_DOWN,  BID_FULL],
            [BID_FULL,  BID_FULL,  BID_DOWN],
            # contain up obstacle
            [BID_UP,    BID_FULL,  BID_FULL],
            [BID_FULL,  BID_UP,    BID_FULL],
            [BID_FULL,  BID_FULL,  BID_UP],
            #contain break obstacle
            [BID_BREAK, BID_FULL,  BID_FULL],
            [BID_FULL,  BID_BREAK, BID_FULL],
            [BID_FULL,  BID_FULL,  BID_BREAK],
            #contain red obstacle
            [BID_RED,   BID_RED,   BID_RED],
            [BID_RED,   BID_FULL,  BID_FULL],
            [BID_FULL,  BID_RED,   BID_FULL],
            [BID_FULL,  BID_FULL,  BID_RED],
            #contain blue obstacle
            [BID_RED,   BID_RED,   BID_RED],
            [BID_RED,   BID_FULL,  BID_FULL],
            [BID_FULL,  BID_RED,   BID_FULL],
            [BID_FULL,  BID_FULL,  BID_RED]
            #contain yellow obstacle
            [BID_RED,   BID_RED,   BID_RED],
            [BID_RED,   BID_FULL,  BID_FULL],
            [BID_FULL,  BID_RED,   BID_FULL],
            [BID_FULL,  BID_FULL,  BID_RED]
            ]
