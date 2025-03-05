import numpy as np
import importlib
from functools import partial


class Binder:
    def __init__(self, f,params):
    
        self.f = f
        self.params = params
        self.module = None
        self.prepared_function = None

    @staticmethod
    def import_module(module_name):
        module = importlib.import_module(module_name)
        globals()[module_name] = module
        print(f"Module {module_name} imported and available globally.")
        return module
    
     
    def fixer(self, params):
        if self.module is None:
            print("You have to import_module first :)")
        fixed_function = partial(self.module,*params)

        return fixed_function
   



# def binder(self, function_name, **bind_params):
#     """
#     Retrieve the function from the imported module and bind parameters.
#     This uses functools.partial to "pre-set" parameters.
    
#     The main difficulty in this part is that we need to somehow call the parameters
#     Each module comes with a config file in .json, so there we can store the params
#     We can call both the function and the parameters with the name,
#     first we need to find a way to summon both, then we construct the fixed system
#     """

#     if self.module is None:
#         raise ValueError("No module imported. Call import_module() first.")

#     # Get the function from the module by name.
#     func = getattr(self.module, function_name)
#     # Create a partial function with the provided parameters bound.
#     self.prepared_function = partial(func, **bind_params)
#     print(f"Function {function_name} is now bound with parameters {bind_params}.")
#     return function




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