import numpy as np
from params import *


def V_bar(rho):
    rho = rho / rho_m
    return v_m*(np.pi/2+np.arctan(11*(rho-.22)/(rho-1)))/(np.pi/2+np.arctan(11*.22))


def P_bar(rho):
    if gamma:
        p = 6 * rho / rho_m
    else:
        p = 2* np.log(rho / rho_m)
    return p


def W(v, rho):
    return v+V_bar(rho)


def Aw_acceleration(x, v):
    a = np.zeros_like(x)
    a[:-1] = C_r*(v[1:]-v[:-1])/(x[1:]-x[:-1])**(gamma+1)+A/T_r*(V_bar(car_length/(x[1:]-x[:-1]))-v[:-1])
    a[-1] = A/T_r*(V_bar(0)-v[-1])
    return a