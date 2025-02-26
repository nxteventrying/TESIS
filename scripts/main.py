# import numpy as np
# from functools import partial
# from systems.lorenz63 import lorenz
# from pipeline.tsdg import Sistema as sistema

# # Parameters
# sigma_val = 10.0
# beta_val = 8.0 / 3.0
# rho_val = 28.0

# # Fix parameters using lambda, pero asi no me sale el titulo en la plot
# lorenz_fixed = lambda t, y: lorenz(t, y, sigma_val, beta_val, rho_val)

# # Time range
# t = np.linspace(0, 100, 10000)

# # Initial conditions
# y0 = [1.0, 1.0, 1.0]

# # Solve the system
# edo = sistema(lorenz_fixed, y0=y0, t=t, metodo="RK45")
# edo.resolver()
# # edo.graficar_series_tiempo()    
# #edo.graficar()
# #df = edo.dataframe()
# #print(df.head())
# edo.graficar(tipo='3d', guardar=True, show_plot=True, filename='series_3d.png')


from pipeline.binder import Binder 



# if __name__ == "__main__":
#     #binder = Binder()
#     binder.import_module("systems.aizawa")

# # Now you can call it directly without instantiating Binder
# if __name__ == "__main__":
#     Binder.import_module("systems.aizawa")

# if __name__ == "__main__":
#     # Import the module
#     module_name = "systems.aizawa"
#     module = Binder.import_module(module_name)
    
#     # Access a function named 'aizawa' within the imported module
#     function_name = "aizawa"
#     if hasattr(module, function_name):
#         aizawa_function = getattr(module, function_name)
#         print(f"Function '{function_name}' from '{module_name}' is now accessible.")
#     else:
#         print(f"Function '{function_name}' not found in '{module_name}'.")



import json
import os

# ---------- Utility Functions ----------

def load_json(file_path: str) -> dict:
    """
    Reads and returns the JSON content from a file.
    """
    with open(file_path, 'r') as f:
        return json.load(f)

def merge_configs(static_config: dict, dynamic_config: dict) -> dict:
    """
    Merges the static (blueprint) configuration with the dynamic parameters.
    Only the 'parameters' section is updated from the dynamic file.
    """
    merged_config = static_config.copy()
    # Replace the 'parameters' part with the dynamic one
    merged_config['parameters'] = dynamic_config.get('parameters', {})
    return merged_config

# ---------- ED Solver Function ----------

def ed_solver_function(state_vector, initial_conditions, time_frame, method):
    """
    Dummy ED solver function that uses the configuration values.
    In a real application, these values would be used to perform a computation.
    """
    print("Running ED Solver with the following configuration:")
    print("State vector:", state_vector)
    print("Initial conditions:", initial_conditions)
    print("Time frame:", time_frame)
    print("Method:", method)
    # Simulate processing and return a dummy result
    result = {"status": "success", "data": "simulation_result"}
    return result

# ---------- Main Execution Flow ----------

if __name__ == "__main__":
    # 1. Load the mother blueprint (static part)
    blueprint_path = os.path.join("blueprints", "mother_blueprint.json")
    static_config = load_json(blueprint_path)
    print("Static blueprint loaded.")

    # 2. Load the dynamic parameters file (dynamic part)
    dynamic_params_path = "dynamic_params.json"
    dynamic_config = load_json(dynamic_params_path)
    print("Dynamic parameters loaded.")

    # 3. Merge the two configurations:
    #    The merged configuration will have the static parts (like ed_solver)
    #    and the dynamic 'parameters' injected from dynamic_params.json.
    config = merge_configs(static_config, dynamic_config)
    print("\nMerged configuration:")
    print(json.dumps(config, indent=4))

    # 4. Interact with the static ED solver part:
    #    Extract the ed_solver section to use its values.
    ed_solver_config = config.get("ed_solver", {})
    state_vector = ed_solver_config.get("state_vector", [])
    initial_conditions = ed_solver_config.get("initial_conditions", [])
    time_frame = ed_solver_config.get("time_frame", [])
    method = ed_solver_config.get("method", "")

    # 5. Use these values in another function (the ED solver function)
    result = ed_solver_function(state_vector, initial_conditions, time_frame, method)
    print("\nED Solver result:")
    print(result)
