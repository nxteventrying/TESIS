import numpy as np
import importlib
from functools import partial


class Binder:
    def __init__(self, f,r,params,y0, t, metodo = "RK45"):
    
        self.f = f
        self.r = r
        self.params = params
        self.y0 = np.atleast_1d(y0)
        self.t = t
        self.metodo = metodo
        self.module = None
        self.prepared_function = None

    @staticmethod
    def import_module(module_name):
        module = importlib.import_module(module_name)
        globals()[module_name] = module
        print(f"Module {module_name} imported and available globally.")
        return module

   



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


# # Ejemplo para un único sistema:
# sigma_val = 10.0 
# beta_val = 8.0 / 3.0
# rho_val = 28.0



# # Rango de tiempo e condiciones iniciales
# t = np.linspace(0, 100, 10000)
# y0 = [1.0, 1.0, 1.0]


