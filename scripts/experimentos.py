# import json
# import numpy as np
# from utils.helpers import sys_params_gen as params_gen
# from utils.helpers import initial_conditions_gen as ic_gen
# from data_generation.binder import Binder  
# from data_generation.tsdg import Sistema  
# import os

# file_path = '/home/think/Desktop/TESIS/test_runs/templates/global_test.json'
# destination_path = "/home/think/Desktop/TESIS/test_runs"

# def genesis_bulk_global(file_path, destination_path):

#     with open(file_path, 'r') as file:
#         config = json.load(file)
#     # Control variables
#     config['run_mode']
#     warden = config['warden']
#     shared_parameters = config['shared_parameters']
#     models = config['models']

#     # Extract the variables we need from the shared_parameters
#     test_number = shared_parameters["test_number"]
#     number_of_child_systems = shared_parameters["number_of_child_systems"]  
#     #t_span = shared_parameters["t_span"]  
#     #t_span = (t_span[0], t_span[1]) 
#     t_span = tuple(shared_parameters["t_span"])
#     num_points = shared_parameters["num_points"]  
#     initial_conditions = shared_parameters["initial_conditions"]  
#     t_eval = np.linspace(t_span[0], t_span[1], num_points)

#     # Initial conditions for each system
#     systems_initial_dict = ic_gen(initial_conditions, number_of_child_systems)
#     # Here we decide which model is allowed to be muahahaha
#     for key, value in warden.items():
#         if value == True:
#             parent_model = key
#             # Extracting parameters (and them ranges)
#             params = {
#                 key: {"min": value[0], "max": value[1]} 
#                 for key, value in models[key]["params"].items()
#                 }
#             # Parameters for each system
#             systems_params_dict = params_gen(params, number_of_child_systems)
#             for i, ((_, v1), (_, v2)) in enumerate(zip(systems_params_dict.items(), systems_initial_dict.items())):

#                 # Initialize the Binder object for dynamic function import
#                 binder = Binder(module_name=f"systems.{parent_model}", 
#                                 function_name=parent_model, 
#                                 params=v1)
                
#                 # Import the module
#                 binder.import_module()
                
#                 # Prepare the function
#                 fixed_function = binder.fixer()
                
#                 if fixed_function:  
#                     # Now we have the fixed function ready, so we can pass it to Sistema
#                     sistema = Sistema(f=fixed_function, 
#                                         y0=v2, 
#                                         t=t_eval, 
#                                         metodo='RK45')
                    
#                     # Solve the system
#                     sistema.resolver()
#                     # Display a nice plot
#                     #sistema.graficar(tipo='3d', guardar=False, show_plot=True)
#                     # Get the DataFrame for the solution
#                     ruta = os.path.join(f"{destination_path}",f"test_{test_number}",f"{parent_model}" ,f"{parent_model}_{i}.csv")
#                     #sistema.csv_or_dataframe(ruta)
#                     print(f'{parent_model}_{i} has been generated \n at {ruta}')

#         else:
#             pass    


# from rich.progress import Progress
# import time

# with Progress() as progress:
#     task = progress.add_task("[cyan]Procesando...", total=100)
#     while not progress.finished:
#         progress.update(task, advance=1)
#         time.sleep(0.1)


# import json
# import numpy as np
# from utils.helpers import sys_params_gen as params_gen
# from utils.helpers import initial_conditions_gen as ic_gen
# from data_generation.binder import Binder  
# from data_generation.tsdg import Sistema  
# import os
# import time
# from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

# file_path = '/home/think/Desktop/TESIS/test_runs/templates/global_test.json'
# destination_path = "/home/think/Desktop/TESIS/test_runs"

# def genesis_bulk_global(file_path, destination_path, user_choice="both"):
#     # Cargar configuración desde JSON
#     with open(file_path, 'r') as file:
#         config = json.load(file)
#     # Variables de control
#     config['run_mode']
#     warden = config['warden']
#     shared_parameters = config['shared_parameters']
#     models = config['models']

#     # Extraer variables necesarias de shared_parameters
#     test_number = shared_parameters["test_number"]
#     number_of_child_systems = shared_parameters["number_of_child_systems"]  
#     t_span = tuple(shared_parameters["t_span"])
#     num_points = shared_parameters["num_points"]  
#     initial_conditions = shared_parameters["initial_conditions"]  
#     t_eval = np.linspace(t_span[0], t_span[1], num_points)

#     # Condiciones iniciales para cada sistema
#     systems_initial_dict = ic_gen(initial_conditions, number_of_child_systems)

#     # Calcular total de iteraciones (modelos activos * sistemas por modelo)
#     total_iterations = sum(1 for key, value in warden.items() if value) * number_of_child_systems

#     # Barra de progreso de Rich, que muestra descripción, barra y ETA
#     progress = Progress(
#         TextColumn("[progress.description]{task.description}"),
#         BarColumn(),
#         TextColumn("{task.completed} of {task.total}"),
#         TimeRemainingColumn(),
#     )
#     progress.start()
#     task = progress.add_task("[cyan]Generando Sistemas...",total=total_iterations)

#     # Aquí decidimos qué modelo está permitido
#     for key, value in warden.items():
#         if value == True:
#             parent_model = key
#             # Extraer parámetros (transforma lista [min, max] en diccionario)
#             params = {
#                 param_key: {"min": param_value[0], "max": param_value[1]} 
#                 for param_key, param_value in models[key]["params"].items()
#             }
#             # Parámetros para cada sistema
#             systems_params_dict = params_gen(params, number_of_child_systems)
#             for i, ((_, v1), (_, v2)) in enumerate(zip(systems_params_dict.items(), systems_initial_dict.items())):
#                 start_time = time.time()  # Tiempo inicial de cada iteración

#                 # Inicializar el Binder para importación dinámica
#                 binder = Binder(module_name=f"systems.{parent_model}", 
#                                 function_name=parent_model, 
#                                 params=v1)
                
#                 # Importar el módulo
#                 binder.import_module()
                
#                 # Preparar la función
#                 fixed_function = binder.fixer()
                
#                 if fixed_function:  
#                     # Ahora tenemos la función fija, se la pasamos a Sistema
#                     sistema = Sistema(f=fixed_function, 
#                                       y0=v2, 
#                                       t=t_eval, 
#                                       metodo='RK45')
                    
#                     # Resolver el sistema
#                     sistema.resolver()

#                     # Dependiendo de la elección del usuario
#                     if user_choice in ["plot", "both"]:
#                         sistema.graficar(tipo='3d', guardar=False, show_plot=True)
                    
#                     if user_choice in ["save", "both"]:
#                         ruta = os.path.join(destination_path, f"test_{test_number}", f"{parent_model}", f"{parent_model}_{i}.csv")
#                         #sistema.csv_or_dataframe(ruta)
#                     else:
#                         ruta = "No se guardó archivo"  # Para actualización en el progress
#                 elapsed_time = time.time() - start_time
#                 progress.update(task,advance=1, description=f"[cyan]{parent_model}_{i}: {elapsed_time:.2f}s")

#     progress.stop()

# # Ejemplo de uso:
# genesis_bulk_global(file_path, destination_path, user_choice="save")


