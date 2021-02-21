import numpy as np
import matplotlib.pyplot as plt
from params import *
from PDE_solver import *
from ODE_solver import *


# In[]

T = 4000
size_window = ODE_length_domain*PDE_initial_density
n_window = 80
window = np.linspace(-size_window*n_window/2, size_window*n_window/2, n_window+1)
weights = np.ones_like(ODE_x_matrix[:, T])/n_car

# plt.hist(ODE_x_matrix[:, T], window, weights=weights, label='ODE', align='right')
# plt.plot(PDE_x_matrix[:, T], rho_matrix[:, T], label='PDE')

counts, center = np.histogram(ODE_x_matrix[:, T], window-size_window/2)
plt.bar(window[:-1], counts/n_car, width=size_window)
plt.plot(PDE_x_matrix[:, T], rho_matrix[:, T], 'r', label='PDE')
plt.ylim([0, 0.07])
plt.xlim(-250, 250)
plt.legend()
plt.title(f'T={T*delta_t}')
plt.grid()
plt.show()




