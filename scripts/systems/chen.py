def chen(t,state, alpha, beta, delta):
    x, y, z = state
    dx = alpha * x - y * z
    dy = beta * y + x * z
    dz = delta * z + (x * y)/3
    return [dx,dy,dz]