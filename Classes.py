import Enums
import Component__UI
import Component__Physics

class Bird():
    def __init__(self, mass, color, radius):
        self.object_enum = Enums.Object_Enum()['Circle']
        self.physics_state = Component__Physics.State(mass)
        self.UI_frame = Component__UI.Circle(color, radius)

        # Bird exclusive data
        self.velocity_multiplier = 1

    def Set_Position(self, x,y):
        #TODO
        self.UI_frame.Set_Position(x,y)
        pass

    def Impulse():
        #TODO
        pass

    def step(cur_time, object_list):
        #TODO
        pass

    def Draw(self, screen, screen_width, screen_height):
        self.UI_frame.Draw(screen, screen_width, screen_height)

class Pig():
    def __init__(self, mass, color, radius):
        self.object_enum = Enums.Object_Enum()['Circle']
        self.physics_state = Component__Physics.State(mass)
        self.UI_frame = Component__UI.Circle(color, radius)

        # Pig exclusive data
        self.velocity_threshold = 30

    def Set_Position(self, x,y):
        #TODO
        self.UI_frame.Set_Position(x,y)
        pass

    def Impulse():
        #TODO
        pass

    def step(cur_time, object_list):
        #TODO
        pass

    def Draw(self, screen, screen_width, screen_height):
        self.UI_frame.Draw(screen, screen_width, screen_height)