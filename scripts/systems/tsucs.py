def tsucs(t,state, a, b, c, d, e, f):
    x, y, z = state
    dx = a * (y - x) + d * x * z
    dy = b * x - x * z + f * y
    dz = c * z + x * y - e * x ** 2
    return [dx,dy,dz]