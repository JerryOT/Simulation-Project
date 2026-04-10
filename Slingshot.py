import pygame, sys
import numpy as np
import Classes

def clamp(n, min_val, max_val):
    return max(min_val, min(n, max_val))

class Slingshot():
    def __init__(self, x, y):
        self.position = np.array([x,y])
        self.assigned_bird = None
        self.dragging = False
        self.max_radius = 50
        self.last_assigned_time = -1000

    def asssign(self, bird, assign_time):
        self.assigned_bird = bird
        if self.assigned_bird is not None:
            self.assigned_bird.physics_state.state[0] = self.position[0]
            self.assigned_bird.physics_state.state[1] = self.position[1]
            self.last_assigned_time = assign_time

    def set_dragging(self, b):
        self.dragging = b

    def update(self, mouse_x, mouse_y):
        if self.assigned_bird:
            if self.dragging:
                p = np.array([mouse_x, mouse_y])
                dir = p - self.position
                length = np.linalg.norm(dir)
                pull = (dir / np.linalg.norm(dir)) * min(self.max_radius, length)
                final_pos = self.position + pull
                
                self.assigned_bird.physics_state.state[0] = final_pos[0]
                self.assigned_bird.physics_state.state[1] = final_pos[1]
            else:
                self.assigned_bird.physics_state.state[0] = self.position[0]
                self.assigned_bird.physics_state.state[1] = self.position[1]

    def release(self, mouse_x, mouse_y):
        if self.assigned_bird and self.dragging:
            p = np.array([mouse_x, mouse_y])
            dir = p - self.position
            length = np.linalg.norm(dir)
            pull_alpha = clamp(min(self.max_radius, length), 0, self.max_radius) / self.max_radius
            velocity_length = pull_alpha * self.assigned_bird.bird_type['Value']['Max_Slingshot_Velocity']
            velocity = (-dir / np.linalg.norm(dir)) * velocity_length
            self.assigned_bird.physics_state.Set_Anchor(False)
            self.assigned_bird.physics_state.Set_Velocity(velocity[0], velocity[1])
           

            self.asssign(None, self.last_assigned_time)
            self.set_dragging(False)

    def draw(self, screen, screen_width, screen_height):
        pos = self.position
        pygame.draw.circle(screen, (255, 255, 255), Classes.Object_To_Screen(screen_width, screen_height, pos[0], pos[1]), 8)