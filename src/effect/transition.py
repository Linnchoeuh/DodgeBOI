"""
transition.py
Lenny Vigeon (lenny.vigeon@gmail.com)
Transition effect
Copyright (c) 2022
"""

WAIT_TIME = 0.5

class TransitionClass():
    def __init__(self, Game):
        self.current_menu = Game.Menu.curr
        self.prev_menu = Game.Menu.curr
        self.black_color = Game.Colors.black
        self.progression = 0
        self.transition_speed = 0.1
        self.wait = 0
        self.state = 0
        self.rect_size = (Game.Res.current[0], Game.Res.current[1])

    def Check(self, Game):
        if (self.state == 0):
            self.current_menu = Game.Menu.curr
        if (Game.Menu.curr != Game.Menu.prev or self.state != 0):
            match self.state:
                case 0:
                    self.progression = 1
                    self.wait = 0
                    self.state = 1
                    Game.Keyboard.disable = True
                    Game.Mouse.disable = True
                case 1:
                    self.progression -= self.transition_speed / Game.speed
                    if (self.progression <= 0):
                        self.progression = 0
                        self.state = 2
                        self.prev_menu = self.current_menu
                case 2:
                    self.wait += 1
                    if (self.wait >= Game.fps.current * WAIT_TIME):
                        self.state = 3;
                case 3:
                    self.progression -= self.transition_speed / Game.speed
                    if (self.progression < -1):
                        self.state = 0
                        Game.Keyboard.disable = False
                        Game.Mouse.disable = False
            round_progress = round(self.progression * Game.Res.current[0])
            self.rect = Game.pygame.Rect(round_progress, 0, self.rect_size[0], self.rect_size[1])
            Game.pygame.draw.rect(Game.ws, self.black_color, self.rect)
            return (self.prev_menu)
        self.prev_menu = self.current_menu
        return (self.current_menu)
