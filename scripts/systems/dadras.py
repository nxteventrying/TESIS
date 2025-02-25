def dadras(t,state, a, b, c, d, e):
    x, y, z = state
    dx = y - a * x  + b * y * z
    dy = c * y - x * z + z
    dz = d * x * y - e * z
    return [dx,dy,dz]