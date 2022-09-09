"""
map_generator.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Where the map is created
Copyright (c) 2022
"""

from src.tools.resolution_manager import WIDTH, HEIGHT
import pygame
import time
import random

BID_VOID = 0
BID_FULL = 1
BID_DOWN = 2
BID_UP = 3
BID_BREAK = 4
BID_RED = 5
BID_BLUE = 6
BID_YELLOW = 7

OBS_POS = 0
OBS_BLOC1 = 1
OBS_BLOC2 = 2
OBS_BLOC3 = 3

SHAPES = [
    # contain void
    (BID_FULL,   BID_VOID,   BID_VOID),
    (BID_VOID,   BID_FULL,   BID_VOID),
    (BID_VOID,   BID_VOID,   BID_FULL),
    # contain less void
    (BID_VOID,   BID_FULL,   BID_FULL),
    (BID_FULL,   BID_VOID,   BID_FULL),
    (BID_FULL,   BID_FULL,   BID_VOID),
    # contain down obstacle
    (BID_DOWN,   BID_FULL,   BID_FULL),
    (BID_FULL,   BID_DOWN,   BID_FULL),
    (BID_FULL,   BID_FULL,   BID_DOWN),
    # contain up obstacle
    (BID_UP,     BID_FULL,   BID_FULL),
    (BID_FULL,   BID_UP,     BID_FULL),
    (BID_FULL,   BID_FULL,   BID_UP),
    #contain break obstacle
    (BID_BREAK,  BID_FULL,   BID_FULL),
    (BID_FULL,   BID_BREAK,  BID_FULL),
    (BID_FULL,   BID_FULL,   BID_BREAK),
    #contain red obstacle
    (BID_RED,    BID_RED,    BID_RED),
    (BID_RED,    BID_FULL,   BID_FULL),
    (BID_FULL,   BID_RED,    BID_FULL),
    (BID_FULL,   BID_FULL,   BID_RED),
    #contain blue obstacle
    (BID_BLUE,   BID_BLUE,   BID_BLUE),
    (BID_BLUE,   BID_FULL,   BID_FULL),
    (BID_FULL,   BID_BLUE,   BID_FULL),
    (BID_FULL,   BID_FULL,   BID_BLUE),
    #contain yellow obstacle
    (BID_YELLOW, BID_YELLOW, BID_YELLOW),
    (BID_YELLOW, BID_FULL,   BID_FULL),
    (BID_FULL,   BID_YELLOW, BID_FULL),
    (BID_FULL,   BID_FULL,   BID_YELLOW)
]

class BlocClass():
    def __init__(self, Res):
        self.speed = 1
        self.separation = Res.Manager.Scale.Val(60)
        self.tier = Res.current[HEIGHT] / 3
        self.size = self.tier - self.separation
        self.linewidth = Res.Manager.Scale.Val(5)
        self.start_point = Res.current[WIDTH] + self.size
        self.end_point = -self.size
        self.obstacle = []
        self.shapes = SHAPES
        self.bloc_color = [[None],
                           [(128, 128, 128), (64, 64, 64)],
                           [(128, 128, 128), (64, 64, 64)],
                           [(128, 128, 128), (64, 64, 64)],
                           [(255, 255, 255), (64, 64, 64)],
                           [(255, 0, 0), (128, 0, 0)],
                           [(0, 0, 255), (0, 0, 128)],
                           [(255, 255, 0), (128, 128, 0)]]
        self.got_time = 0
        self.timing_offset = 0

    def Generate(self, shape):
        self.obstacle.append([self.start_point, shape[0], shape[1], shape[2]])

    def Delete(self, pos):
        del self.obstacle[pos]

    def Display(self, surface):
        for i in range(0, len(self.obstacle)):
            for k in range(0, 3):
                bloc = self.obstacle[i][k + 1]
                offset = 0
                thickness = self.size
                if (bloc == BID_DOWN):
                    thickness = (self.size / 2)
                    offset = (self.size / 2) - (self.separation / 2)
                elif (bloc == BID_UP):
                    thickness = (self.size / 2)
                posy = (k * self.tier) + (self.separation / 2) + offset
                rect = pygame.Rect(self.obstacle[i][OBS_POS],
                                        posy, self.size, thickness)
                if (bloc != BID_VOID):
                    pygame.draw.rect(surface, self.bloc_color[bloc][0], rect)

    def Move(self, px_move):
        for i in range(0, len(self.obstacle)):
            self.obstacle[i][OBS_POS] -= px_move

    def Run(self, surface, delay, pause):
        if ((delay / self.speed) < (time.time() - self.got_time)):
            self.got_time = time.time()
            self.Generate(self.shapes[random.randint(0, len(SHAPES) - 1)])
        self.Display(surface)
        if (pause == False):
            self.Move(3 * self.speed)
            if (len(self.obstacle) > 0 and self.obstacle[0][OBS_POS] < self.end_point):
                self.Delete(0)
        else:
            self.timing_offset = time.time() - self.got_time
            self.got_time = time.time() + self.timing_offset

