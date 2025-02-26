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

if __name__ == "__main__":
    # Import the module
    module_name = "systems.aizawa"
    module = Binder.import_module(module_name)
    
    # Access a function named 'aizawa' within the imported module
    function_name = "aizawa"
    if hasattr(module, function_name):
        aizawa_function = getattr(module, function_name)
        print(f"Function '{function_name}' from '{module_name}' is now accessible.")
    else:
        print(f"Function '{function_name}' not found in '{module_name}'.")