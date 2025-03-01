import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp
import pandas as pd
import os

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

        Parámetros:
          - nuevo_metodo: Método de integración (e.g., "RK45", "DOP853").
        """
        self.metodo = nuevo_metodo
        print(f"Método cambiado a {self.metodo}")

    def resolver(self):
        """Resuelve la EDO utilizando el método numérico definido."""
        self.solucion = solve_ivp(self.f, [self.t[0], self.t[-1]], self.y0,
                                    t_eval=self.t, method=self.metodo)
        return self.solucion
    
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
            ax.set_title(f'{self.f.__name__} Attractor (3D)')
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
            fig.suptitle(f"Series de Tiempo de {self.f.__name__}")

        else:
            raise ValueError("Tipo de gráfica no reconocido. Usa '3d' o 'series'.")

        plt.tight_layout()

        if guardar:
            
            fig.savefig(filename)
            print(f"Gráfica guardada en {filename}")

        # Define the directory and filename
        directory = '/path/to/save/directory'
        filename = 'my_plot.png'

        # Ensure the directory exists
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Construct the full path
        full_path = os.path.join(directory, filename)

        # Save the figure
        plt.savefig(full_path)

        if show_plot:
            plt.show()
        return fig
       
    def dataframe(self):
        """Devuelve el dataframe de la series de tiempo """
        if self.solucion is None:
            raise ValueError("Primero debes resolver la ecuación.")
        
        # for i in range(self.solucion.y.shape[0]):
        X = self.solucion.y[0]
        Y = self.solucion.y[1]
        Z = self.solucion.y[2]
     
        df = pd.DataFrame({'x':X,'y':Y,'z':Z })

        return df