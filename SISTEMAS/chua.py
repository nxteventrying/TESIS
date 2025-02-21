def chua(t,state, sigma, beta, rho):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x *  y - beta *z 
    return [dx,dy,dz]
