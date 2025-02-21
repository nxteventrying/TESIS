import numpy as np
from functools import partial
from sistemas.lorenz63 import lorenz
from pipeline.tsg import Sistema as sistema

# from tsg import Sistema as sistema
# import numpy as np

# # Ejemplo de uso:
# # Resolver la EDO: dy/dt = -2y, con y(0)=1
# def ecuacion(t, y):
#     return -2 * y

# t = np.linspace(0, 5, 100)
# edo = sistema(ecuacion, y0=1, t=t, metodo="RK45")
# print(edo.resolver())
# #edo.graficar()




# Parameters
sigma_val = 10.0
beta_val = 8.0 / 3.0
rho_val = 28.0

# Fix parameters using lambda
lorenz_fixed = lambda t, y: lorenz(t, y, sigma_val, beta_val, rho_val)

# Time range
t = np.linspace(0, 5, 100)

# Initial conditions
y0 = [1.0, 1.0, 1.0]

# Solve the system
edo = sistema(lorenz_fixed, y0=y0, t=t, metodo="RK45")
edo.resolver()
edo.graficar()
