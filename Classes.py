import pygame, sys
import numpy as np
import Enums
import Physics


def Object_To_Screen(win_width, win_height, x, y):
        return (x, win_height - y)

class Building__Box():
    def __init__(self, material, width, height):
        self.object_type = Enums.ObjectType['Box']
        self.collision_type = Enums.CollisionType['Box']
        self.physics_state = Physics.State(self.object_type, material, width, height)
        self.material = material
        self.width = width
        self.height = height

        self.health = self.material['Value']['Health_Density'] * self.width * self.height

    def Draw(self, screen, screen_width, screen_height):
        pos = self.physics_state.Get_Position()
        rot = self.physics_state.Get_Rotation()
        boxArray = np.array([
            [self.width/2, self.height/2],
            [-self.width/2, self.height/2],
            [-self.width/2, -self.height/2],
            [self.width/2, -self.height/2]
        ])
        box_world = [pos + np.dot(rot, cb) for cb in boxArray]
        box_screen = [Object_To_Screen(screen_width, screen_height, cw[0], cw[1]) for cw in box_world]
        pygame.draw.polygon(screen, self.material['Value']['Color'], box_screen)


class Building__Circle():
    def __init__(self, material, radius):
        self.object_type = Enums.ObjectType['Circle']
        self.collision_type = Enums.CollisionType['Circle']
        self.physics_state = Physics.State(self.object_type, material, radius, radius)
        self.material = material
        self.radius = radius

        self.health = self.material['Value']['Health_Density'] * np.pow( radius, 2 ) * np.pi

    def Draw(self, screen, screen_width, screen_height):
        pos = self.physics_state.Get_Position()
        pygame.draw.circle(screen, self.material['Value']['Color'], Object_To_Screen(screen_width, screen_height, pos[0], pos[1]), self.radius)


class Bird():
    def __init__(self, bird_type, radius):
        self.object_type = Enums.ObjectType['Bird']
        self.collision_type = Enums.CollisionType['Circle']
        self.physics_state = Physics.State(self.object_type, bird_type, radius, radius)
        self.material = bird_type
        self.radius = radius

        self.bird_type = bird_type
        self.health = bird_type['Value']['Health']

    def Draw(self, screen, screen_width, screen_height):
        pos = self.physics_state.Get_Position()
        pygame.draw.circle(screen, self.material['Value']['Color'], Object_To_Screen(screen_width, screen_height, pos[0], pos[1]), self.radius)


class Pig():
    def __init__(self, pig_type, radius):
        self.object_type = Enums.ObjectType['Pig']
        self.collision_type = Enums.CollisionType['Circle']
        self.physics_state = Physics.State(self.object_type, pig_type, radius, radius)
        self.material = pig_type
        self.radius = radius

        self.pig_type = pig_type
        self.health = pig_type['Value']['Health']
        
    def Draw(self, screen, screen_width, screen_height):
        pos = self.physics_state.Get_Position()
        pygame.draw.circle(screen, self.material['Value']['Color'], Object_To_Screen(screen_width, screen_height, pos[0], pos[1]), self.radius)