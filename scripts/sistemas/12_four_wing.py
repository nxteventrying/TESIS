def four_wing(t,state, a, b, c):
    x, y, z = state
    dx = a * x + y * z
    dy = b * x + c * y - x * z
    dz = -z - x * y
    return [dx,dy,dz]