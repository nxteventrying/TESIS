from utils.reader import read_config as reader
from data_generation.binder import Binder as binder
from data_generation.tsdg import Sistema as system
import os
import time

# Ask for configuration file

def load_config():

    answer = input("Do you have a configuration file? (Y/N): ").strip().lower()

    if answer == "y":
        file_path = input("Where is your configuration file for this test?\n").strip()
        
        # /home/think/Desktop/TESIS/test_runs/test_1/test1.json

        # Check if file exists
        if not os.path.isfile(file_path):
            print("File not found. Make sure you typed the correct path.")
            exit(1)  # Exit script

        print("\nLoading configuration...")
        time.sleep(1)  # <- Delay for 2 seconds
        config_data = reader(file_path)  # Read JSON
        print("Configuration loaded")

        return config_data

    else:
        print("Go and make one with architect.py you dumbass")
        exit(1)

config_data = load_config()

# # Print everything nicely
# print("\nPLease check the configuration:\n")
# for key, value in config_data.items():
#     print(f"{key}: {value}")


test_number = config_data["test_number"]
parent_model = config_data["parent_model"]
number_of_child_systems = config_data["number_of_child_systems"]
kind_step = config_data["kind_step"]

params = config_data["params"]

initial_conditions = config_data["initial_conditions"]
t_span = config_data["t_span"]
num_points = config_data["num_points"]


# Now one of the main problems is that this code must accept any configuration file,
# i.e, we need to somehow not declare any variables for params


# Dynamically create global variables with their min and max values
for key, value in params.items():
    globals()[f"{key}_test1"] = value
    globals()[f"{key}_min_test1"] = value["min"]
    globals()[f"{key}_max_test1"] = value["max"]

# Automatically print all the dynamically created variables for each key
for key in params.keys():
    var_name = f"{key}_test1"
    min_name = f"{key}_min_test1"
    max_name = f"{key}_max_test1"
    print(f"{var_name}: {globals()[var_name]}")
    print(f"{min_name}: {globals()[min_name]}")
    print(f"{max_name}: {globals()[max_name]}")





# Loop through each key in params and create a variable dynamically.
# for key, value in params.items():
#     var_name = f"{key}_test1"  # e.g., 'sigma_test1'
#     globals()[var_name] = value
#     # Use the variable as needed
#     print(f"{var_name} =", globals()[var_name])
    # If you only need it temporarily, you can delete it after use:
    # del globals()[var_name]

# # Optionally, if you want to clean up after the loop:
# for key in list(params.keys()):
#     var_name = f"{key}_test1"
#     if var_name in globals():
#         del globals()[var_name]























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





