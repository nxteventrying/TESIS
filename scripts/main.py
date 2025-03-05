import numpy as np
from utils.helpers import load_config
from utils.helpers import sys_params_gen as params_gen
from utils.helpers import initial_conditions_gen as ic_gen
from data_generation.binder import Binder as binder
from data_generation.tsdg import Sistema as system


# Ask for configuration file, or make one
# /home/think/Desktop/TESIS/test_runs/test_1/test1.json

config_data = load_config()

#we extract the variables we need 

test_number = config_data["test_number"]
parent_model = config_data["parent_model"]
number_of_child_systems = config_data["number_of_child_systems"]
kind_step = config_data["kind_step"]

params = config_data["params"]

initial_conditions = config_data["initial_conditions"]
t_span = config_data["t_span"]
num_points = config_data["num_points"]

#we start using them variables

t_span = (t_span["start"], t_span["end"])
t_eval = np.linspace(t_span[0], t_span[1], num_points)

# parameters for each system
systems_params_dict = params_gen(params,
                                number_of_child_systems)
#initial conditions for each system
systems_initial_dict = ic_gen(initial_conditions,
                                 number_of_child_systems)

for key,value in systems_params_dict.items():
    print(f"{key}:{value}")

for key,value in systems_initial_dict.items():
    print(f"{key}:{value}")
# for (k1, v1), (k2, v2) in zip(systems_params_dict.items(), systems_initial_dict.items()):
#     #v1 is the parameters
#     #v2 is the initial condition


#     # child_function = binder.import_module(parent_model)
#     # binder.fixer(child_function, v1)
#     # # now that we have the fixed function we need to call tsdg
#     # # system.resolver()
#     # # system.csv_or_dataframe()