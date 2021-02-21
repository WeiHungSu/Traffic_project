import numpy as np
from params import *
from Aw_model import *

# In[] Set up the initial
PDE_domain = -PDE_length_domain/2+np.array([0, PDE_length_domain])
PDE_x_matrix = np.zeros((N_x, n_time))
PDE_x_matrix[:, 0] = np.linspace(PDE_domain[0], PDE_domain[1], N_x)
PDE_v_matrix = np.zeros((N_x, n_time))
ratio = PDE_domain[1]/PDE_length_domain
PDE_v_matrix[:, 0] = 0.05
PDE_v_matrix[int(np.floor(N_x*(1-ratio))):, 0] = 0.5

tau_matrix = np.zeros((N_x, n_time))
tau_matrix[:, 0] = (PDE_x_matrix[2, 0] - PDE_x_matrix[1, 0]) / delta_x
rho_matrix = np.zeros((N_x, n_time))
rho_matrix[:, 0] = 1/tau_matrix[:, 0]
w_matrix = np.zeros((N_x, n_time))
w_matrix[:, 0] = PDE_v_matrix[:, 0] + P_bar(rho_matrix[:, 0])

# In[] PDE_discretization
for n in range(n_time-1):
    tau_matrix[:, n+1] = tau_matrix[:, n] + CFL * (np.concatenate((PDE_v_matrix[1:, n], PDE_v_matrix[-1:, n]), axis=0) -PDE_v_matrix[:, n])
    rho_matrix[:, n+1] = 1 / tau_matrix[:, n+1]
    if A:
        w_matrix[:, n+1] = w_matrix[:, n] * np.exp(-delta_t/T_r) + (V_bar(rho_matrix[:, n+1]) + P_bar(rho_matrix[:, n+1])) * (1 - np.exp(-delta_t/T_r))
    else:
        w_matrix[:, n+1] = w_matrix[:, n]
    PDE_v_matrix[:, n+1] = w_matrix[:, n+1] - P_bar(rho_matrix[:, n+1])
    PDE_x_matrix[:, n+1] = PDE_x_matrix[:, n] + delta_t * PDE_v_matrix[:, n+1]



