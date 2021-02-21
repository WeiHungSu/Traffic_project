# In[]
gamma = 0
A = 1
PDE_length_domain = 400
ODE_length_domain = PDE_length_domain
PDE_initial_density = 0.05  # number of bins = 1/PDE_initial_density
n_car = 800  # for ODE; This can be varied to any number.
n_time = 5000


# In[]
T_r = 20
rho_m = 1
v_m = 1
car_length = 1/40
CFL = 1
delta_x = car_length
delta_t = CFL * delta_x
if gamma:
    V_ref = 6
else:
    V_ref = 2
C_r = V_ref * (delta_x / rho_m) ** gamma
N_x = int(PDE_initial_density * PDE_length_domain/delta_x)
