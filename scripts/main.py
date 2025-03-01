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

# Print everything nicely
print("\nPLease check the configuration:\n")
for key, value in config_data.items():
    print(f"{key}: {value}")



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





