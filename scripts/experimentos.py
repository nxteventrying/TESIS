import json
import numpy as np
from utils.helpers import sys_params_gen as params_gen
from utils.helpers import initial_conditions_gen as ic_gen
from data_generation.binder import Binder  
from data_generation.tsdg import Sistema  



file_path = '/home/think/Desktop/TESIS/test_runs/templates/global_test.json'
with open(file_path, 'r') as file:
    config = json.load(file)

#config['run_mode']
warden = config['warden']
shared_parameters = config['shared_parameters']
models = config['models']

# Extract the variables we need from the shared_parameters
test_number = shared_parameters["test_number"]
number_of_child_systems = shared_parameters["number_of_child_systems"]  
#t_span = shared_parameters["t_span"]  
#t_span = (t_span[0], t_span[1]) 
t_span = tuple(shared_parameters["t_span"])
num_points = shared_parameters["num_points"]  
initial_conditions = shared_parameters["initial_conditions"]  
t_eval = np.linspace(t_span[0], t_span[1], num_points)

# Initial conditions for each system
systems_initial_dict = ic_gen(initial_conditions, number_of_child_systems)
# Here we decide which model is allowed to be muahahaha
for key, value in warden.items():
    if value == True:
        parent_model = key
        # Extracting parameters (and them ranges)
        params = {
            key: {"min": value[0], "max": value[1]} 
            for key, value in models[key]["params"].items()
            }
        # Parameters for each system
        systems_params_dict = params_gen(params, number_of_child_systems)
        for i, ((_, v1), (_, v2)) in enumerate(zip(systems_params_dict.items(), systems_initial_dict.items())):

            # Initialize the Binder object for dynamic function import
            binder = Binder(module_name=f"systems.{parent_model}", 
                            function_name=parent_model, 
                            params=v1)
            
            # Import the module
            binder.import_module()
            
            # Prepare the function
            fixed_function = binder.fixer()
            
            if fixed_function:  
                # Now we have the fixed function ready, so we can pass it to Sistema
                sistema = Sistema(f=fixed_function, 
                                    y0=v2, 
                                    t=t_eval, 
                                    metodo='RK45')
                
                # Solve the system
                sistema.resolver()
                sistema.graficar(tipo='3d', guardar=False, show_plot=True)
                print(parent_model)
                # Get the DataFrame for the solution
                #sistema.csv_or_dataframe(f"/home/think/Desktop/TESIS/test_runs/test_{str(test_number)}/{i}.csv")
        

    else:
        pass    