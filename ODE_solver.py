import numpy as np
from params import *
from Aw_model import *

# In[] Sep up the initial
ODE_domain = -ODE_length_domain/2+np.array([0, ODE_length_domain])
ODE_x_matrix = np.zeros((n_car, n_time))
ODE_x_matrix[:, 0] = np.linspace(ODE_domain[0], ODE_domain[1], n_car)
ratio_2 = ODE_domain[1]/ODE_length_domain
ODE_v_matrix = np.zeros((n_car, n_time))
ODE_v_matrix[:, 0] = 0.05
ODE_v_matrix[int(np.floor(n_car*(1-ratio_2))):, 0] = 0.5

# In[] ODE_discretization
for n in range(n_time-1):
    a = Aw_acceleration(ODE_x_matrix[:, n], ODE_v_matrix[:, n])
    ODE_v_matrix[:, n+1] = ODE_v_matrix[:, n] + a * delta_t
    ODE_x_matrix[:, n+1] = ODE_x_matrix[:, n] + ODE_v_matrix[:, n+1] * delta_t




