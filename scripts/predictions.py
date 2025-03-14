def lorenz(t, state, sigma=10.0, beta=8.0/3.0, rho=28.5):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]

y0 = [1.0, 1.0, 1.0]
t_span = (0, 105)
t_eval = np.linspace(t_span[0], t_span[1], 735)

sol = solve_ivp(lorenz, t_span, y0, method='RK45', t_eval=t_eval)

X = sol.y[0]
Y = sol.y[1]
Z = sol.y[2]

# time_points = sol.t # de por si lo vamos a remplazar entonces no tiene sentido usarlo xd
# entonces vamos a crear el index como si fueran dias, y nuestro starting point sera el unix

df = pd.DataFrame({'x':X,'y':Y,'z':Z })
