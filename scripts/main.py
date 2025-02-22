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
#df = edo.dataframe()
#print(df.head())
edo.graficar(tipo='3d', guardar=True, show_plot=True, filename='series_3d.png')



#### okay, esa parte solo es para testear que propiedades le podemos sacar al sistema

# lo que quiero hacer ahora es poder generar el ensamble de sistemas,
# es decir, vamos a generar las condiciones inciales
# estas iran en un diccionario (por ahora) en un .json
# vamos a usar este para checar si existen los archivos en las carpetas, 
# necesitamos las imagenes y el df
# solo eso, pero debemos hacerlo de tal manera que sea organizado y limpio
#no quiero terminar con 242142 imagenes sin sentido

def make_lorenz(sigma, beta, rho, name=None):
    """Genera una función del sistema de Lorenz con parámetros fijos.
    
    Se le puede asignar un nombre opcional para usarlo en títulos, etc.
    """
    def lorenz_fixed(t, y):
        return lorenz(t, y, sigma, beta, rho)
    # Asignamos un atributo al objeto función para identificarlo
    lorenz_fixed.name = name if name is not None else f"Lorenz (σ={sigma}, β={beta}, ρ={rho})"
    return lorenz_fixed

# Ejemplo para un único sistema:
sigma_val = 10.0
beta_val = 8.0 / 3.0
rho_val = 28.0

# Generamos la función con parámetros y nombre
lorenz_func = make_lorenz(sigma_val, beta_val, rho_val, name="Lorenz Base")

# Rango de tiempo e condiciones iniciales
t = np.linspace(0, 100, 10000)
y0 = [1.0, 1.0, 1.0]

# Creamos y resolvemos el sistema
edo = sistema(lorenz_func, y0=y0, t=t, metodo="RK45")
edo.resolver()



# Lista de sets de parámetros (ejemplo)
param_sets = [
    (10.0, 8.0/3.0, 28.0),
    (12.0, 8.0/3.0, 35.0),
    (8.0, 8.0/3.0, 22.0),
    # ... 97 sets más
]

# Para cada set, creamos la función y el objeto sistema
sistemas = []
for sigma, beta, rho in param_sets:
    func = make_lorenz(sigma, beta, rho, name=f"Lorenz (\sigma={sigma}, \beta={beta}, \rho={rho})")
    sys_instance = sistema(func, y0=y0, t=t, metodo="RK45")
    sys_instance.resolver()
    sistemas.append(sys_instance)









# model.py
def lorenz(t, state, sigma, beta, rho):
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]


# simulation.py
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from model import lorenz

def run_simulation(params, initial_conditions, t_span, t_eval, output_dir):
    # Create a unique identifier for the simulation based on parameters and initial conditions
    sim_id = f"sigma={params['sigma']}_beta={params['beta']}_rho={params['rho']}_x0={initial_conditions[0]}_y0={initial_conditions[1]}_z0={initial_conditions[2]}"
    sim_dir = os.path.join(output_dir, sim_id)

    # Check if the simulation has already been run
    if os.path.exists(sim_dir):
        print(f"Simulation {sim_id} already exists. Skipping.")
        return

    # Create directory for this simulation
    os.makedirs(sim_dir, exist_ok=True)

    # Define the system of equations with fixed parameters
    def system(t, state):
        return lorenz(t, state, **params)

    # Solve the system
    solution = solve_ivp(system, t_span, initial_conditions, t_eval=t_eval)

    # Save the solution to a CSV file
    df = pd.DataFrame({
        't': solution.t,
        'x': solution.y[0],
        'y': solution.y[1],
        'z': solution.y[2]
    })
    df.to_csv(os.path.join(sim_dir, 'solution.csv'), index=False)

    # Plot the results
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(solution.y[0], solution.y[1], solution.y[2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Lorenz Attractor')
    plt.savefig(os.path.join(sim_dir, 'plot.png'))
    plt.close()

    # Save the parameters and initial conditions to a JSON file
    config = {
        'parameters': params,
        'initial_conditions': initial_conditions
    }
    with open(os.path.join(sim_dir, 'config.json'), 'w') as f:
        json.dump(config, f, indent=4)

    print(f"Simulation {sim_id} completed and saved.")



# main_script.py
import os
import json
from simulation.py import run_simulation

# Directories
config_dir = 'configurations'
results_dir = 'results'
os.makedirs(config_dir, exist_ok=True)
os.makedirs(results_dir, exist_ok=True)

# Time settings
t_span = (0, 50)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# Load or define parameter sets and initial conditions
parameter_sets = [
    {'sigma': 10.0, 'beta': 8.0 / 3.0, 'rho': 28.0},
    {'sigma': 14.0, 'beta': 8.0 / 3.0, 'rho': 35.0},
    # Add more parameter sets as needed
]
initial_conditions_list = [
    [1.0, 1.0, 1.0],
    [0.1, 0.0, 0.0],
    # Add more initial conditions as needed
]

# Iterate over all combinations of parameters and initial conditions
for params in parameter_sets:
    for initial_conditions in initial_conditions_list:
        run_simulation(params, initial_conditions, t_span, t_eval, results_dir)
