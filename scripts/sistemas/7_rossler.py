def rossler(t,state, a,b,c):
    x, y, z = state
    dx = - y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return [dx,dy,dz]
