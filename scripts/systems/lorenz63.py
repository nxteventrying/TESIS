# So, we need to change the order of the parameters, t and state.
# We can solve the problem adding a new function but this is easier and faster.
def lorenz63(sigma, beta, rho, t, state):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x *  y - beta *z 
    return [dx,dy,dz]
