import numpy as np
import Enums
import OBBSAT

collision_tolerance = 1e-2
friction = 1.5
e = 0.2


class State():
    def __init__(self, object_type, material, width, height):
        self.state = np.zeros(9)
        self.state[0:2] = np.zeros(2)
        self.state[2:6] = np.identity(2).reshape([1,4])
        self.state[6:8] = np.zeros(2)
        self.state[8:9] = 0

        self.anchored = False
        self.object_type = object_type
        self.material = material
        self.width = width
        self.height = height

        self.t = 0
        
    def Set_Anchor(self, boolean):
        self.anchored = boolean

    def Calculate_Mass(self):
        if self.object_type == Enums.ObjectType['Circle']:
            radius = self.width
            V = np.pow( radius, 2 ) * np.pi
            return np.sqrt(V * self.material['Value']['Density'] )
        return np.sqrt(self.width * self.height * self.material['Value']['Density'])
    
    def Body_Inertia(self):
        w, h = self.width, self.height
        m = self.Calculate_Mass()

        if self.object_type == Enums.ObjectType['Circle']:
            Ixx = (1/4) * m * w**2
            Iyy = (1/4) * m * w**2
            return np.diag([Ixx, Iyy])
        
        Ixx = (1/12) * m * (h*h)
        Iyy = (1/12) * m * (w*w)
        return np.diag([Ixx, Iyy])
    
    def Body_Inertia_World(self):
        R = self.Get_Rotation()
        Iinverse = R @ self.Body_Inertia() @ R.T
        return Iinverse
    


    def Set_Position(self, x, y):
        if self.anchored:
            return
        self.state[0] = x
        self.state[1] = y

    def Set_Velocity(self, x, y):
        if self.anchored:
            return
        self.state[6] = x
        self.state[7] = y

    def Set_Rotation(self, angle):
        if self.anchored:
            return
        theta = np.deg2rad(angle)
        c = np.cos(theta)
        s = np.sin(theta)
        R = np.array([
            [ c, -s],
            [ s,  c]
        ])
        self.state[2:6] = R.reshape([1,4])


    def Get_Position(self):
        return self.state[0:2]
    def Get_Rotation(self):
        return self.state[2:6].reshape([2,2])
    
    def integrate(self, level_obj, t, state):
        if self.anchored:
            return state
        
        time_current = self.t
        dt = t - time_current
        
        mass = self.Calculate_Mass()
        position = state[0:2]
        rotation = state[2:6]
        rotationMatrix = rotation.reshape([2,2])
        velocity = state[6:8]
        angular_velocity = state[8:9]

        friction_reduction = np.zeros(2)
        if np.linalg.norm(velocity) > 0:
            velocity_direction = velocity / np.linalg.norm(velocity)
            frictionDir = friction * velocity_direction
            friction_reduction = frictionDir * dt * dt

        new_velocity = velocity + dt * np.array([0, -level_obj.gravity]) - friction_reduction
        new_theta = np.atan2(rotationMatrix[1][0], rotationMatrix[0][0]) + (angular_velocity * dt)
        c, s = np.cos(new_theta), np.sin(new_theta)
        rotation_matrix = np.array([
            [c, -s],
            [s,  c]
        ])
        
        
        state = np.zeros(9)
        state[0:2] = position + dt * new_velocity
        state[2:6] = rotation_matrix.reshape([1,4])
        state[6:8] = new_velocity
        state[8:9] = angular_velocity #- angular_velocity * 0.5 * friction * dt * dt
        return state

    def step(self, dt, self_obj, level_obj):
        if self.anchored:
            return
        time_current, time_next = self.t, self.t + dt
        self.state = self.integrate(level_obj, time_next, self.state)
        self.t += dt



def Check_Collision(objA, stateA, objB, stateB):
    a_type = objA.collision_type
    b_type = objB.collision_type

    if a_type == Enums.CollisionType['Box'] and b_type == Enums.CollisionType['Box']:
        posA = stateA[0:2]
        rotA = stateA[2:6].reshape(2, 2)
        halfA = [objA.width / 2, objA.height / 2]

        posB = stateB[0:2]
        rotB = stateB[2:6].reshape(2, 2)
        halfB = [objB.width / 2, objB.height / 2]
        return OBBSAT.obb_collision(posA, rotA, halfA, posB, rotB, halfB)

    # ------------------------
    # Circle vs Circle
    # ------------------------
    if a_type == Enums.CollisionType['Circle'] and b_type == Enums.CollisionType['Circle']:
        p1 = stateA[0:2]
        p2 = stateB[0:2]
        d = p2 - p1
        dist = np.linalg.norm(d)
        r1 = objA.radius
        r2 = objB.radius
        penetration = (r1 + r2) - dist
        if penetration > 0:
            normal = d / dist
            contact_point = p1 + normal * (r1 - penetration / 2.0)
            return True, penetration, normal, contact_point
        
     # ------------------------
    # Box vs Circle
    # ------------------------
    if a_type == Enums.CollisionType['Box'] and b_type == Enums.CollisionType['Circle']:
        posA = stateA[0:2]
        rotA = stateA[2:6].reshape(2, 2)
        halfA = [objA.width / 2, objA.height / 2]

        posB = stateB[0:2]
        rotB = stateB[2:6].reshape(2, 2)
        halfB = [objB.radius / 2, objB.radius / 2]

        d = posB - posA
        local = np.array([
            np.dot(d, rotA[:, 0]),
            np.dot(d, rotA[:, 1]),
        ])
        clamped = np.clip(local, -np.array(halfA), np.array(halfA))
        closest = posA.copy()
        for i in range(2):
            closest += clamped[i] * rotA[:, i]

        v = posB - closest
        dist = np.linalg.norm(v)

        if dist < collision_tolerance:
            normal = np.array([1.0, 0.0])
            penetration = objB.radius
        else:
            normal = v / dist
            penetration = objB.radius - dist
            
        collided = penetration > 0
        contact_point = closest 

        return collided, penetration, normal, contact_point
    
    # ------------------------
    # Circle vs Box
    # ------------------------
    if a_type == Enums.CollisionType['Circle'] and b_type == Enums.CollisionType['Box']:
        collided, penetration, normal, contact_point = Check_Collision(objB, stateB, objA, stateA)
        if collided:
            return True, penetration, -normal, contact_point
    


    return False, 0, np.zeros(3), np.zeros(3)




def Response_Collision(level_obj, objA, stateA, objB, stateB, penetration, normal, contact_point):
    def To3D(vec):
        return np.array([vec[0], vec[1], 0])
    def To3DR(R):
        return np.array([
            [ R[0], -R[1], 0],
            [ R[2],  R[3], 0],
            [    0,     0, 1]
        ])
    def To3DAngular(a):
        return np.array([0, 0, a[0]])
    def To3DBody(B):
        return np.array([
            [ B[1][1] * 0.1, B[0][1] * 0.5, B[0][1] * 0.5],
            [ B[1][0] * 0.5, B[0][0] * 0.1, B[0][1] * 0.5],
            [ B[1][0] * 0.5, B[1][0] * 0.5, B[1][1] * 0.1]
        ])
    
    n = To3D(normal)

    mA = objA.physics_state.Calculate_Mass()
    mB = objB.physics_state.Calculate_Mass()
    IbodyInvA = To3DBody(np.linalg.inv(objA.physics_state.Body_Inertia_World()))
    IbodyInvB = To3DBody(np.linalg.inv(objB.physics_state.Body_Inertia_World()))

    posA = To3D(stateA[0:2])
    posB = To3D(stateB[0:2])
    vA = To3D(stateA[6:8])
    vB = To3D(stateB[6:8])
    wA = To3DBody(np.linalg.inv(objA.physics_state.Body_Inertia())) @ To3DAngular(stateA[8:9])
    wB = To3DBody(np.linalg.inv(objB.physics_state.Body_Inertia())) @ To3DAngular(stateB[8:9])

    rA = To3D(contact_point) - posA
    rB = To3D(contact_point) - posB

    rA_cn = np.cross(rA, n)
    rB_cn = np.cross(rB, n)
    
    v_rel = (vB + np.cross(wB, rB)) - (vA + np.cross(wA, rA))
    vel_along_normal = np.dot(v_rel, n)

    inv_mA = (1 / mA)
    inv_mB = (1 / mB)
    if objA.physics_state.anchored:
        inv_mA = 0
    if objB.physics_state.anchored:
        inv_mB = 0
    total_inv_mass = inv_mA + inv_mB
    if total_inv_mass == 0:
        j = 0
    else:
        j = -(1.0 + e) * vel_along_normal / total_inv_mass
    J = j * n
    angA = -np.cross(rA, J)
    angB = np.cross(rB, J)

    veloA, veloB = vA - j / mA * n, vB + j / mB * n
    omegaA, omegaB = wA + IbodyInvA @ angA, wB + IbodyInvB @ angB

    #debug = contact_point
    #level_obj.Add_Debug_Position(debug[0], debug[1])

    veloA = np.array([ veloA[0], veloA[1]])
    veloB = np.array([ veloB[0], veloB[1]])
    omegaA = omegaA[2]
    omegaB = omegaB[2]

    return veloA, veloB, omegaA, omegaB, (-j / mA * n), (j / mB * n)