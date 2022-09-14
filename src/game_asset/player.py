"""
player.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Game element
"""

from include.output_devices import *
import random
import pygame

P_RED = 0
P_BLUE = 1
P_YELLOW = 2

class PlayerActionStruct():
    def __init__(self):
        self.up = False
        self.down = False
        self.kick = False
        self.slide = False
        self.jump = False
        self.color = random.randint(0, P_YELLOW)

class PlayerClass():
    def __init__(self,
                 Screen: ScreenClass):
        split_pos = Screen.current_res[HEIGHT] / 6
        self.snap_pos = 1
        self.x = Screen.Scaler.Val(100)
        self.y = Screen.Scaler.Val(split_pos * 3)
        self.coords_pos = ((self.x, split_pos),
                           (self.x, self.y),
                           (self.x, split_pos * 5))
        self.action = PlayerActionStruct()
        self.trigger_key = [pygame.K_z,
                            pygame.K_s,
                            pygame.K_SPACE,
                            pygame.K_a,
                            pygame.K_e,
                            pygame.K_k,
                            pygame.K_l,
                            pygame.K_m]

    def KeyboardInput(self, Keyboard):
        action_list = []
        action_list.append(Keyboard.KeyOncePressed(self.trigger_key[0]))
        action_list.append(Keyboard.KeyOncePressed(self.trigger_key[1]))
        action_list.append(Keyboard.key.curr[self.trigger_key[2]])
        action_list.append(Keyboard.key.curr[self.trigger_key[3]])
        action_list.append(Keyboard.key.curr[self.trigger_key[4]])
        if (Keyboard.key.curr[self.trigger_key[5]]):
            self.action.color = P_RED
        elif (Keyboard.key.curr[self.trigger_key[6]]):
            self.action.color = P_BLUE
        elif (Keyboard.key.curr[self.trigger_key[7]]):
            self.action.color = P_YELLOW
        action_list.append(self.action.color)
        return (action_list)

    def Movement(self, action_list):
        self.up = action_list[0]
        self.down = action_list[1]
        self.kick = action_list[2]
        self.slide = action_list[3]
        self.jump = action_list[4]
        self.color = action_list[5]
        if (self.snap_pos > 0 and self.up == True):
            self.snap_pos -= 1
        if (self.snap_pos < 2 and self.down == True):
            self.snap_pos += 1

    def Display(self, surface):
        self.x = self.coords_pos[self.snap_pos][0]
        self.y = self.coords_pos[self.snap_pos][1]
        match self.color:
            case 0:
                color = (255,0,0)
            case 1:
                color = (0,0,255)
            case 2:
                color = (255,255,0)
        if (self.kick):
            color = (0,255,0)
        if (self.slide):
            color = (0,255,255)
        if (self.jump):
            color = (255,0,255)
        pygame.draw.line(surface, color,
                         self.coords_pos[self.snap_pos],
                         (self.x + 50, self.y), 5)



