import json

def read_config(file_path):
    with open(file_path, 'r') as file:
        config = json.load(file)

    test_number = config["test_number"]
    parent_model = config["parent_model"]
    number_of_child_systems = config["number_of_child_systems"]
    kind_step = config["kind_step"]
    
    # Extracting parameters (sigma, rho, beta ranges)
    params = {
        key: {"min": value[0], "max": value[1]} 
        for key, value in config["params"].items()
    }

    # Extracting initial conditions with min/max values
    initial_conditions = {
        key: {"min": value["min"], "max": value["max"]}
        for key, value in config["initial_conditions"].items()
    }

    t_span = {"start": config["t_span"][0], "end": config["t_span"][1]}
    num_points = config["num_points"]

    return {
        "test_number": test_number,
        "parent_model": parent_model,
        "number_of_child_systems": number_of_child_systems,
        "kind_step": kind_step,
        "params": params,
        "initial_conditions": initial_conditions,
        "t_span": t_span,
        "num_points": num_points
    }




# import json

# def read_config(file_path):
#     """Reads a JSON config file and returns all parameters dynamically."""
#     try:
#         with open(file_path, 'r') as file:
#             config = json.load(file)

#         extracted_values = []

#         def extract_values(obj):
#             """Recursively extracts all numeric values, including ranges."""
#             if isinstance(obj, dict):
#                 for key, value in obj.items():
#                     extract_values(value)
#             elif isinstance(obj, list) and all(isinstance(i, (int, float)) for i in obj):
#                 extracted_values.extend(obj)  # Add all list values
#             elif isinstance(obj, (int, float)):
#                 extracted_values.append(obj)  # Add single values

#         extract_values(config)
#         return tuple(extracted_values)

#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return None
#     except json.JSONDecodeError:
#         print(f"Error: Invalid JSON format in '{file_path}'.")
#         return None
