import pygame, sys
import numpy as np
import Classes
import Physics
import Enums

class Level():
    def __init__(self, slingshot):
        self.object_list = list()
        self.cur_time = 0
        self.dt = 0.1
        self.debug_set = set()
        self.slingshot = slingshot
        self.gravity = 1
        self.bird_queue = []
        
        self.velocity_damage_minimum = 3
        self.velocity_damage_bird_reduce = 0.8



    def Enqueue_Bird(self, o):
        self.bird_queue.append(o)
    def Dequeue_Bird(self):
        if len(self.bird_queue) == 0:
            return None
        o = self.bird_queue.pop()
        return o
        
    def Add_Object(self, o):
        if o.object_type == Enums.ObjectType['Bird']:
            o.physics_state.Set_Anchor(True)
            self.Enqueue_Bird(o)
        self.object_list.append(o)

    def Add_Debug_Position(self, x, y):
        self.debug_set.add((x,y))

    def Get_Object_On_Position(self, x, y):
        for obj in self.object_list:
            state = obj.physics_state.state

            if obj.collision_type == Enums.CollisionType['Box']:
                position = state[0:2]
                rotation = state[2:6].reshape(2, 2)
                width = obj.width
                height = obj.height
                
                local = np.array([x - position[0], y - position[1]])
                local = rotation.T @ local
                if abs(local[0]) <= width / 2 and abs(local[1]) <= height / 2:
                    return obj

            if obj.collision_type == Enums.CollisionType['Circle']:
                position = state[0:2]
                rotation = state[2:6].reshape(2, 2)
                radius = obj.radius
                
                dx = x - position[0]
                dy = y - position[1]
                if dx*dx + dy*dy <= radius * radius:
                    return obj

        return None

    def Step(self):
        collision_set = set()

        for i in range(len(self.object_list)):
            objA = self.object_list[i]

            for j in range(i + 1, len(self.object_list)):
                objB = self.object_list[j]
                if objA == objB:
                    continue

                currentStateA = objA.physics_state.state
                currentStateB = objB.physics_state.state
                nextStateA = objA.physics_state.integrate(self, objA.physics_state.t + self.dt, objA.physics_state.state)
                nextStateB = objB.physics_state.integrate(self, objB.physics_state.t + self.dt, objB.physics_state.state)
                collided, penetration, normal, contact_point = Physics.Check_Collision(objA, nextStateA, objB, nextStateB)
                if collided:
                    normal = normal / np.linalg.norm(normal)
                    collision_set.add(objA)
                    collision_set.add(objB)
                    veloA, veloB, omegaA, omegaB, veloGainA, veloGainB = Physics.Response_Collision(self, objA, currentStateA, objB, currentStateB, penetration, normal, contact_point)
                    
                    new_theta_A = np.atan2(currentStateA[4], currentStateA[2]) + (omegaA * self.dt / 2)
                    cA, sA = np.cos(new_theta_A), np.sin(new_theta_A)
                    state_A = np.zeros(9)
                    state_A[0:2] = currentStateA[0:2] - normal * 0.1
                    state_A[2:6] = np.array([
                        [cA, -sA],
                        [sA,  cA]
                    ]).reshape([1,4])
                    state_A[6:8] = veloA
                    state_A[8:9] = omegaA

                    new_theta_B = np.atan2(currentStateB[4], currentStateB[2]) + (omegaB * self.dt / 2)
                    cB, sB = np.cos(new_theta_B), np.sin(new_theta_B)
                    state_B = np.zeros(9)
                    state_B[0:2] = currentStateB[0:2] + normal * 0.1
                    state_B[2:6] = np.array([
                        [cB, -sB],
                        [sB,  cB]
                    ]).reshape([1,4])
                    state_B[6:8] = veloB
                    state_B[8:9] = omegaB

                    if not objA.physics_state.anchored:
                        if np.linalg.norm(veloGainA) > self.velocity_damage_minimum:
                            objA.health -= (np.linalg.norm(veloGainA) - self.velocity_damage_minimum) * self.velocity_damage_bird_reduce if objA.object_type == Enums.ObjectType['Bird'] else np.linalg.norm(veloGainA) - self.velocity_damage_minimum
                    if not objB.physics_state.anchored:
                        if np.linalg.norm(veloGainB) > self.velocity_damage_minimum:
                            objB.health -= (np.linalg.norm(veloGainB) - self.velocity_damage_minimum) * self.velocity_damage_bird_reduce if objB.object_type == Enums.ObjectType['Bird'] else np.linalg.norm(veloGainB) - self.velocity_damage_minimum

                    if (not objA.physics_state.anchored) and objB.health > 0:
                        objA.physics_state.state = state_A
                        objA.physics_state.t = objA.physics_state.t
                    if (not objB.physics_state.anchored) and objA.health > 0:
                        objB.physics_state.state = state_B
                        objB.physics_state.t = objB.physics_state.t

        preserved_list = list()
        for i in range(len(self.object_list)):
            obj = self.object_list[i]
            if obj.health > 0:
                preserved_list.append(obj)
        self.object_list = preserved_list

        for obj in self.object_list:
            if obj in collision_set:
                #obj.physics_state.step(-self.dt / 10, obj, self)
                continue
            obj.physics_state.step(self.dt, obj, self)

        

        self.cur_time += self.dt

    def Draw_All(self, screen, screen_width, screen_height):
        for obj in self.object_list:
            obj.Draw(screen, screen_width, screen_height)

        for x,y in self.debug_set:
            pygame.draw.circle(screen, Enums.Color['WHITE'], Classes.Object_To_Screen(screen_width, screen_height, x, y), 4)