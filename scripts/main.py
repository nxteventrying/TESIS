import numpy as np
from functools import partial
from sistemas.lorenz63 import lorenz
from pipeline.tsg import Sistema as sistema

# Parameters
sigma_val = 10.0
beta_val = 8.0 / 3.0
rho_val = 28.0

# Fix parameters using lambda, pero asi no me sale el titulo en la plot
lorenz_fixed = lambda t, y: lorenz(t, y, sigma_val, beta_val, rho_val)

# Time range
t = np.linspace(0, 100, 10000)

# Initial conditions
y0 = [1.0, 1.0, 1.0]

# Solve the system
edo = sistema(lorenz_fixed, y0=y0, t=t, metodo="RK45")
edo.resolver()
# edo.graficar_series_tiempo()    
#edo.graficar()
df = edo.dataframe()
print(df.head())
