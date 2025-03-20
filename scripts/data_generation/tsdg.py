import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp
import pandas as pd
import os
import matplotlib.animation as animation


class Sistema:

    """
    Clase para resolver ecuaciones diferenciales ordinarias (EDOs).

    Parámetros:
      - f: función que define el sistema de ecuaciones diferenciales (dy/dt = f(t, y)).
      - y0: condición inicial (puede ser un número o un array para sistemas).
      - t: array de tiempos donde se evaluará la solución.
      - metodo: método numérico para la integración (por defecto "RK45").
    """


    def __init__(self, f, y0, t, metodo = "RK45"):
        self.f = f
        self.y0 = np.atleast_1d(y0)
        self.t = t
        self.metodo = metodo
        self.solucion = None

    def set_metodo(self, nuevo_metodo):

        """
        Permite cambiar el método de integración numérica.
        """

        self.metodo = nuevo_metodo
        print(f"Método cambiado a {self.metodo}")

    def resolver(self):

        """Resuelve la EDO utilizando el método numérico definido."""

        self.solucion = solve_ivp(self.f, [self.t[0], self.t[-1]], self.y0,
                                    t_eval=self.t, method=self.metodo)
        return self.solucion
    
    def atractor_animation(self):
        
        sol = self.solucion  
        x, y, z = sol.y  # Extract trajectory data

        # Set up the figure and 3D axis
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlim((np.min(x), np.max(x)))
        ax.set_ylim((np.min(y), np.max(y)))
        ax.set_zlim((np.min(z), np.max(z)))
        ax.set_title("Attractor Animation")

        # Initialize the plot elements
        trail_length = 150  # Number of points in fading trace
        line, = ax.plot([], [], [], 'r-', lw=1)  # Main trajectory
        trace, = ax.plot([], [], [], 'g-', lw=2, alpha=0.7)  # Fading trace
        point, = ax.plot([], [], [], 'bo', markersize=6)  # Moving point

        def update(i):
            if i < trail_length:
                trace_x = x[:i]
                trace_y = y[:i]
                trace_z = z[:i]
            else:
                trace_x = x[i - trail_length:i]
                trace_y = y[i - trail_length:i]
                trace_z = z[i - trail_length:i]

            # 🛠 Fix: Only apply fading if the trace has points
            if len(trace_x) > 0:
                fade_alpha = np.linspace(0.1, 1.0, len(trace_x))  # Gradient fade
                trace.set_alpha(fade_alpha[0])  # Apply fading effect

            # Update the trace
            trace.set_data(trace_x, trace_y)
            trace.set_3d_properties(trace_z)

            # Update main trajectory and moving point
            line.set_data(x[:i], y[:i])
            line.set_3d_properties(z[:i])
            point.set_data(x[i], y[i])
            point.set_3d_properties(z[i])

            return line, trace, point
        # Run animation
        ani = animation.FuncAnimation(fig, update, frames=len(self.t), interval=10, blit=False)

        plt.show()


        return
    def graficar(self, tipo='3d', guardar=False, show_plot=True, filename='plot.png'):
        """
        Genera la gráfica de la solución de la EDO.
        
        Parámetros:
        - tipo: '3d' para la trayectoria en 3D o 'series' para la serie de tiempo.
        - guardar: si True, guarda la gráfica en un archivo.
        - show_plot: si True, muestra la gráfica en pantalla.
        - filename: nombre del archivo donde se guardará la gráfica.
        
        Retorna el objeto figura (fig).
        """
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")

        if tipo == '3d':
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(self.solucion.y[0], self.solucion.y[1], self.solucion.y[2],
                    color='purple', lw=0.5)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.set_title(f'Attractor (3D)')  # {self.f.func.__name__}
            ax.view_init(elev=30, azim=60)

        elif tipo == 'series':
            fig, axs = plt.subplots(self.solucion.y.shape[0], 1, figsize=(10, 8), sharex=True)
            labels = ['x', 'y', 'z']
            colors = ['r', 'g', 'b']

            for i in range(self.solucion.y.shape[0]):
                axs[i].plot(self.solucion.t, self.solucion.y[i], color=colors[i])
                axs[i].set_ylabel(labels[i])
                axs[i].grid()

            axs[-1].set_xlabel("Time")
            fig.suptitle(f"Series de Tiempo de {getattr(self.f, 'func', self.f).__name__}")

        else:
            raise ValueError("Tipo de gráfica no reconocido. Usa '3d' o 'series'.")

        plt.tight_layout()

        if guardar:
            directory = "/path/to/save/directory" 
            os.makedirs(directory, exist_ok=True)  
            full_path = os.path.join(directory, filename)
            fig.savefig(full_path)
            print(f"Gráfica guardada en {full_path}")

        if show_plot:
            plt.show()

        return fig
       
    def csv_or_dataframe(self, filename = None):

        """Devuelve el dataframe de la series de tiempo, o un csv
         si es que le damos un nombre """
        
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")
        
        X = self.solucion.y[0]
        Y = self.solucion.y[1]
        Z = self.solucion.y[2]
     
        df = pd.DataFrame({'x':X,'y':Y,'z':Z })

        if filename:
            df.to_csv(filename, index=False)

        return df
    