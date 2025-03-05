import numpy as np
from utils.helpers import load_config
from utils.helpers import sys_params_gen as params_gen
from utils.helpers import initial_conditions_gen as ic_gen
from utils.all_in_one import df_in_one 


# Ask for configuration file, or make one
# we have one LOL
# /home/think/Desktop/TESIS/test_runs/test_1/test1.json

config_data = load_config()

#we extract the variables we need 

test_number = config_data["test_number"] # coming soon
parent_model = config_data["parent_model"] # se usa
number_of_child_systems = config_data["number_of_child_systems"] # se usa
kind_step = config_data["kind_step"] # coming soon

params = config_data["params"] # se usa

initial_conditions = config_data["initial_conditions"] # se usa
t_span = config_data["t_span"] # se usa
num_points = config_data["num_points"] # se usa

# parameters for each system
systems_params_dict = params_gen(params,
                                number_of_child_systems)
#initial conditions for each system
systems_initial_dict = ic_gen(initial_conditions,
                                 number_of_child_systems)

# now we make the loop for the csv generation
# we will need a place to store this csv, so we can include
# that in the configuration or ask the user directly,
# but he kinda dumbass so we need to make it robust if we want to add it

t_span = (t_span["start"], t_span["end"])
t_eval = np.linspace(t_span[0], t_span[1], num_points)  

# parent_model, cause we need to summon the .py function



#parent_model = "lorenz63"  # Nombre del módulo sin prefijo
package_prefix = "scripts.systems"  # Ruta dentro de tu proyecto
#module_name = f"{package_prefix}.{parent_model}"  # Construcción dinámica
#function_name = parent_model  # Si la función se llama igual que el módulo
#print(module_name)

for (k1, v1), (k2, v2) in zip(systems_params_dict.items(), systems_initial_dict.items()):
     #v1 is the parameters
     #v2 is the initial condition
    cuco = df_in_one(module_name = f"{package_prefix}.{parent_model}", 
                     function_name = parent_model, 
                     params = v1, 
                     t_span = t_span, 
                     y0 = v2, 
                     method='RK45', 
                     t_eval=t_eval)
    cuco.to_csv(f"/home/think/Desktop/TESIS/test_runs/{str(k1)}.csv")
