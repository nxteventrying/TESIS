import numpy as np
class Architect:
    """
    Here we'll decide like the global configurations
    """
    
    # Parameters
    sigma_val = 10.0
    beta_val = 8.0 / 3.0
    rho_val = 28.0
    # Time range
    t = np.linspace(0, 100, 10000)

    # Initial conditions
    y0 = [1.0, 1.0, 1.0]
    
    
    
    pass