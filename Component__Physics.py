import numpy as np
from scipy.integrate import ode

class State():
    def __init__(self, mass):
        self.mass = mass
        self.Ibody = np.identity(3)
        self.IbodyInv = np.linalg.inv(self.Ibody)

        self.state = np.zeros(19)
        self.state[0:3] = np.zeros(3)                     # position
        self.state[3:12] = np.identity(3).reshape([1,9])  # rotation
        self.state[12:15] = self.mass * np.zeros(3)            # linear momentum
        self.state[15:18] = np.zeros(3)                   # angular momentum

        self.solver = ode(self.f)
        self.solver.set_integrator('dop853')
        #self.solver.set_f_params()
    def f():
        #TODO
        pass
    
    def step(cur_time, object_list):
        #TODO
        pass