"""
transition.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Transition effect
Copyright (c) 2022
"""

WAIT_TIME = 0.5

class TransitionClass():
    def __init__(self, Game):
        self.current_menu = Game.curr_menu
        self.prev_menu = Game.curr_menu
        self.black_color = Game.Colors.black
        self.progression = 0
        self.transition_speed = 0.1
        self.wait = 0
        self.state = 0
        self.rect = Game.pygame.Rect(0,0, Game.ResManager.Res.current[0], Game.ResManager.Res.current[1])

    def Check(self, Game):
        if (self.state == 0):
            self.current_menu = Game.curr_menu
        if (self.prev_menu != self.current_menu or self.state != 0):
            match self.state:
                case 0:
                    self.progression = 1
                    self.wait = 0
                    self.state = 1
                    Game.Keyboard.disable = True
                    Game.Mouse.disable = True
                case 1:
                    self.progression -= self.transition_speed / Game.framerate.speed
                    if (self.progression <= 0):
                        self.progression = 0
                        self.state = 2
                        self.prev_menu = self.current_menu
                case 2:
                    self.wait += 1
                    if (self.wait >= Game.framerate.fps * WAIT_TIME):
                        self.state = 3;
                case 3:
                    self.progression -= self.transition_speed / Game.framerate.speed
                    if (self.progression < -1):
                        self.state = 0
                        Game.Keyboard.disable = False
                        Game.Mouse.disable = False
            self.rect = Game.pygame.Rect(
                round(self.progression * Game.ResManager.Res.current[0]),
                0,
                self.rect.width,
                self.rect.height)
            Game.pygame.draw.rect(Game.ws, self.black_color, self.rect)
            return (self.prev_menu)
        self.prev_menu = self.current_menu
        return (self.current_menu)
